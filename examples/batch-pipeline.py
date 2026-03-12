#!/usr/bin/env python3
"""
Batch Image-to-Video Pipeline via Atlas Cloud

Demonstrates a production-ready batch pipeline:
1. Generate multiple NSFW images using Flux Dev ($0.012/each)
2. Animate selected images into videos using Wan 2.2 Spicy ($0.03/each)

Supports parallel execution for fast batch processing.

Usage:
    export ATLAS_API_KEY="your-key-here"
    python batch-pipeline.py

Sign up: https://www.atlascloud.ai?ref=JPM683
"""

import os
import sys
import time
import json
import requests
import concurrent.futures
from dataclasses import dataclass, field
from typing import Optional

# Configuration
API_KEY = os.environ.get("ATLAS_API_KEY")
BASE_URL = "https://queue.atlascloud.ai"

if not API_KEY:
    print("Error: ATLAS_API_KEY environment variable not set.")
    print("Get your API key at https://www.atlascloud.ai?ref=JPM683")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Key {API_KEY}",
    "Content-Type": "application/json",
}


@dataclass
class PipelineResult:
    """Result from a single pipeline execution."""
    prompt: str
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    status: str = "pending"
    error: Optional[str] = None
    image_cost: float = 0.0
    video_cost: float = 0.0

    @property
    def total_cost(self):
        return self.image_cost + self.video_cost


def poll_for_result(model_path, request_id, interval=5, timeout=300):
    """Generic polling function for any Atlas Cloud queue endpoint."""

    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed > timeout:
            raise TimeoutError(f"Timed out after {timeout}s")

        status_response = requests.get(
            f"{BASE_URL}/{model_path}/requests/{request_id}/status",
            headers=HEADERS,
        )
        status_response.raise_for_status()
        status = status_response.json()

        if status["status"] == "COMPLETED":
            result = requests.get(
                f"{BASE_URL}/{model_path}/requests/{request_id}",
                headers=HEADERS,
            )
            result.raise_for_status()
            return result.json()

        if status["status"] in ("FAILED", "CANCELLED"):
            raise Exception(f"Request {status['status']}: {status}")

        time.sleep(interval)


def generate_image(prompt, image_size="landscape_16_9"):
    """Generate a single NSFW image using Flux Dev."""

    response = requests.post(
        f"{BASE_URL}/fal-ai/flux/dev",
        headers=HEADERS,
        json={
            "prompt": prompt,
            "image_size": image_size,
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": 1,
            "enable_safety_checker": False,
        },
    )
    response.raise_for_status()
    request_id = response.json()["request_id"]

    result = poll_for_result("fal-ai/flux/dev", request_id, interval=3, timeout=120)
    return result["images"][0]["url"]


def generate_video_from_image(prompt, image_url):
    """Animate an image into a video using Wan 2.2 Spicy."""

    response = requests.post(
        f"{BASE_URL}/fal-ai/wan-spicy/v1/image-to-video",
        headers=HEADERS,
        json={
            "prompt": prompt,
            "image_url": image_url,
            "negative_prompt": "low quality, blurry, distorted, deformed, artifacts",
            "num_frames": 81,
            "resolution": "720p",
            "guidance_scale": 7.5,
            "num_inference_steps": 30,
        },
    )
    response.raise_for_status()
    request_id = response.json()["request_id"]

    result = poll_for_result(
        "fal-ai/wan-spicy/v1/image-to-video", request_id, interval=5, timeout=300
    )
    return result["video"]["url"]


def run_single_pipeline(prompt):
    """Run a complete image-to-video pipeline for a single prompt."""

    result = PipelineResult(prompt=prompt)

    try:
        # Step 1: Generate image
        result.image_url = generate_image(prompt)
        result.image_cost = 0.012
        print(f"  [Image OK] {prompt[:50]}...")

        # Step 2: Animate into video
        result.video_url = generate_video_from_image(prompt, result.image_url)
        result.video_cost = 0.03
        result.status = "success"
        print(f"  [Video OK] {prompt[:50]}...")

    except Exception as e:
        result.status = "failed"
        result.error = str(e)
        print(f"  [FAILED]   {prompt[:50]}... — {e}")

    return result


def run_batch_pipeline(prompts, max_workers=3):
    """Run multiple image-to-video pipelines in parallel."""

    print(f"\nStarting batch pipeline with {len(prompts)} prompts...")
    print(f"  Max parallel workers: {max_workers}")
    print(f"  Estimated cost: ${len(prompts) * 0.042:.3f}")
    print(f"    - Images: {len(prompts)} x $0.012 = ${len(prompts) * 0.012:.3f}")
    print(f"    - Videos: {len(prompts)} x $0.030 = ${len(prompts) * 0.030:.3f}")
    print()

    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_prompt = {
            executor.submit(run_single_pipeline, prompt): prompt
            for prompt in prompts
        }

        for future in concurrent.futures.as_completed(future_to_prompt):
            result = future.result()
            results.append(result)

    return results


def print_results(results):
    """Print a summary of batch results."""

    print("\n" + "=" * 70)
    print("BATCH PIPELINE RESULTS")
    print("=" * 70)

    successful = [r for r in results if r.status == "success"]
    failed = [r for r in results if r.status == "failed"]
    total_cost = sum(r.total_cost for r in results)

    for i, result in enumerate(results, 1):
        status_icon = "OK" if result.status == "success" else "FAIL"
        print(f"\n[{status_icon}] Pipeline {i}: {result.prompt[:60]}...")

        if result.image_url:
            print(f"     Image: {result.image_url}")
        if result.video_url:
            print(f"     Video: {result.video_url}")
        if result.error:
            print(f"     Error: {result.error}")
        print(f"     Cost:  ${result.total_cost:.3f}")

    print("\n" + "-" * 70)
    print(f"Summary:")
    print(f"  Successful: {len(successful)}/{len(results)}")
    print(f"  Failed:     {len(failed)}/{len(results)}")
    print(f"  Total cost: ${total_cost:.3f}")
    print("-" * 70)


if __name__ == "__main__":
    print("=" * 70)
    print("Batch Image-to-Video Pipeline")
    print("Flux Dev ($0.012/img) + Wan 2.2 Spicy ($0.03/vid)")
    print("Powered by Atlas Cloud")
    print("=" * 70)

    # Define batch prompts — each will be used for both image and video
    batch_prompts = [
        (
            "Elegant figure in flowing white silk gown, "
            "golden sunset backlighting, ocean breeze, "
            "artistic fashion photography, cinematic composition"
        ),
        (
            "Noir style portrait, dramatic single-light setup, "
            "deep shadows, mysterious atmosphere, "
            "classic black and white aesthetic with subtle warmth"
        ),
        (
            "Renaissance painting style, reclining figure on velvet, "
            "Caravaggio-inspired lighting, rich jewel tones, "
            "museum-quality fine art composition"
        ),
        (
            "Modern dance performance, athletic figure in motion, "
            "dramatic stage lighting, long exposure effect, "
            "contemporary art photography, fluid movement"
        ),
        (
            "Tropical paradise setting, crystal clear water, "
            "warm golden hour light, natural beauty, "
            "travel photography style, vivid colors"
        ),
    ]

    # Run the batch pipeline
    results = run_batch_pipeline(batch_prompts, max_workers=3)

    # Print summary
    print_results(results)

    print(f"\nSign up at https://www.atlascloud.ai?ref=JPM683")
    print(f"First recharge includes 25% bonus up to $100!")
