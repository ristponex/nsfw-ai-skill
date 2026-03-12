#!/usr/bin/env python3
"""
Wan 2.2 Spicy — NSFW Video Generation via Atlas Cloud

Generates uncensored NSFW videos using the Wan 2.2 Spicy model,
a LoRA fine-tuned model purpose-built for adult content.

Cost: $0.03 per request (cheapest NSFW video API available)
Resolution: Up to 720p
Duration: ~3 seconds (81 frames at 24fps)

Usage:
    export ATLAS_API_KEY="your-key-here"
    python video-generation.py

Sign up: https://www.atlascloud.ai?ref=JPM683
"""

import os
import sys
import time
import json
import requests

# Configuration
API_KEY = os.environ.get("ATLAS_API_KEY")
BASE_URL = "https://queue.atlascloud.ai"
MODEL_PATH = "fal-ai/wan-spicy/v1"

if not API_KEY:
    print("Error: ATLAS_API_KEY environment variable not set.")
    print("Get your API key at https://www.atlascloud.ai?ref=JPM683")
    sys.exit(1)


def submit_video_request(prompt, negative_prompt="", num_frames=81,
                         resolution="720p", guidance_scale=7.5,
                         num_inference_steps=30):
    """Submit a video generation request to Atlas Cloud."""

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt or "low quality, blurry, distorted, deformed, artifacts",
        "num_frames": num_frames,
        "resolution": resolution,
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps,
    }

    response = requests.post(
        f"{BASE_URL}/{MODEL_PATH}",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
    )
    response.raise_for_status()

    data = response.json()
    request_id = data["request_id"]
    print(f"Request submitted successfully.")
    print(f"  Request ID: {request_id}")
    print(f"  Model: Wan 2.2 Spicy")
    print(f"  Cost: ~$0.03")
    print(f"  Frames: {num_frames}")
    print(f"  Resolution: {resolution}")

    return request_id


def poll_status(request_id, interval=5, timeout=300):
    """Poll for request completion with timeout."""

    start_time = time.time()
    last_status = None

    while True:
        elapsed = time.time() - start_time
        if elapsed > timeout:
            raise TimeoutError(f"Request timed out after {timeout} seconds")

        response = requests.get(
            f"{BASE_URL}/{MODEL_PATH}/requests/{request_id}/status",
            headers={"Authorization": f"Key {API_KEY}"},
        )
        response.raise_for_status()
        status_data = response.json()
        current_status = status_data.get("status", "UNKNOWN")

        if current_status != last_status:
            print(f"  Status: {current_status} ({elapsed:.0f}s elapsed)")
            last_status = current_status

        if current_status == "COMPLETED":
            return True
        elif current_status in ("FAILED", "CANCELLED"):
            raise Exception(f"Request {current_status}: {json.dumps(status_data, indent=2)}")

        time.sleep(interval)


def get_result(request_id):
    """Retrieve the completed result."""

    response = requests.get(
        f"{BASE_URL}/{MODEL_PATH}/requests/{request_id}",
        headers={"Authorization": f"Key {API_KEY}"},
    )
    response.raise_for_status()
    return response.json()


def generate_video(prompt, **kwargs):
    """Complete video generation flow: submit, poll, retrieve."""

    print(f"\nGenerating video...")
    print(f"  Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
    print()

    # Submit
    request_id = submit_video_request(prompt, **kwargs)
    print()

    # Poll
    print("Waiting for completion...")
    poll_status(request_id)
    print()

    # Retrieve
    print("Retrieving result...")
    result = get_result(request_id)
    video_url = result["video"]["url"]
    print(f"  Video URL: {video_url}")

    return video_url


if __name__ == "__main__":
    # Example prompts for different styles
    examples = [
        {
            "prompt": (
                "A graceful figure dancing slowly in golden sunset light, "
                "flowing translucent silk fabric draped elegantly, "
                "artistic cinematography with shallow depth of field, "
                "warm amber and rose color palette, studio quality"
            ),
            "negative_prompt": "low quality, blurry, distorted, deformed, ugly, artifacts",
        },
    ]

    print("=" * 60)
    print("Wan 2.2 Spicy — NSFW Video Generation")
    print("Powered by Atlas Cloud")
    print("=" * 60)

    for i, example in enumerate(examples):
        print(f"\n--- Example {i + 1} ---")
        try:
            video_url = generate_video(**example)
            print(f"\nSuccess! Video available at:\n  {video_url}")
        except Exception as e:
            print(f"\nError: {e}")

    print("\n" + "=" * 60)
    print("Done. Sign up at https://www.atlascloud.ai?ref=JPM683")
    print("=" * 60)
