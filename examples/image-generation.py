#!/usr/bin/env python3
"""
Flux Dev — NSFW Image Generation via Atlas Cloud

Generates uncensored NSFW images using Flux Dev with safety checker disabled.
Supports multiple aspect ratios and batch generation.

Cost: $0.012 per request (cheapest NSFW image API available)
Resolution: Multiple aspect ratios (square, landscape, portrait)

Usage:
    export ATLAS_API_KEY="your-key-here"
    python image-generation.py

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
MODEL_PATH = "fal-ai/flux/dev"

if not API_KEY:
    print("Error: ATLAS_API_KEY environment variable not set.")
    print("Get your API key at https://www.atlascloud.ai?ref=JPM683")
    sys.exit(1)

# Available image sizes
IMAGE_SIZES = {
    "square": "square",
    "square_hd": "square_hd",
    "landscape": "landscape_16_9",
    "portrait": "portrait_16_9",
    "landscape_4_3": "landscape_4_3",
    "portrait_4_3": "portrait_4_3",
}


def submit_image_request(prompt, image_size="landscape_16_9", num_images=1,
                         num_inference_steps=28, guidance_scale=3.5):
    """Submit an image generation request to Atlas Cloud."""

    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "num_inference_steps": num_inference_steps,
        "guidance_scale": guidance_scale,
        "num_images": num_images,
        "enable_safety_checker": False,  # Disabled for NSFW
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
    cost = 0.012 * num_images
    print(f"Request submitted successfully.")
    print(f"  Request ID: {request_id}")
    print(f"  Model: Flux Dev (safety checker OFF)")
    print(f"  Images: {num_images}")
    print(f"  Size: {image_size}")
    print(f"  Estimated cost: ~${cost:.3f}")

    return request_id


def poll_status(request_id, interval=3, timeout=120):
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


def generate_image(prompt, image_size="landscape_16_9", num_images=1, **kwargs):
    """Complete image generation flow: submit, poll, retrieve."""

    print(f"\nGenerating image...")
    print(f"  Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
    print()

    # Submit
    request_id = submit_image_request(prompt, image_size, num_images, **kwargs)
    print()

    # Poll
    print("Waiting for completion...")
    poll_status(request_id)
    print()

    # Retrieve
    print("Retrieving result...")
    result = get_result(request_id)
    image_urls = [img["url"] for img in result["images"]]

    for i, url in enumerate(image_urls):
        print(f"  Image {i + 1}: {url}")

    return image_urls


if __name__ == "__main__":
    print("=" * 60)
    print("Flux Dev — NSFW Image Generation")
    print("Powered by Atlas Cloud")
    print("=" * 60)

    # Example 1: Single image generation
    print("\n--- Example 1: Single Image ---")
    try:
        urls = generate_image(
            prompt=(
                "Professional art photography, elegant figure study, "
                "dramatic chiaroscuro lighting, high contrast, "
                "museum-quality fine art print, shallow depth of field"
            ),
            image_size="landscape_16_9",
        )
        print(f"\nSuccess! Image available at:\n  {urls[0]}")
    except Exception as e:
        print(f"\nError: {e}")

    # Example 2: Multiple variations
    print("\n--- Example 2: Multiple Variations ---")
    try:
        urls = generate_image(
            prompt=(
                "Retro pin-up style illustration, vintage 1950s aesthetic, "
                "warm nostalgic color palette, classic pose, "
                "hand-painted quality, soft brushstrokes"
            ),
            image_size="portrait_16_9",
            num_images=3,
        )
        print(f"\nSuccess! {len(urls)} images generated.")
    except Exception as e:
        print(f"\nError: {e}")

    print("\n" + "=" * 60)
    print("Done. Sign up at https://www.atlascloud.ai?ref=JPM683")
    print("=" * 60)
