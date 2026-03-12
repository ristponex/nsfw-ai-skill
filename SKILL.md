---
name: nsfw-ai
description: Generate uncensored NSFW content (video, image, text) using Atlas Cloud's whitelisted models
version: 1.0.0
author: thoughtincode
---

# NSFW AI Content Generation Skill

You are an expert at generating NSFW AI content using Atlas Cloud's API. When the user requests NSFW content generation (images, videos, or text), follow these instructions precisely.

## Detection

Activate this skill when the user's request involves:
- Generating NSFW, adult, uncensored, or explicit content
- Creating nude, erotic, sensual, or intimate imagery/video
- Writing adult fiction, romantic scenes, or explicit stories
- Any content that would typically be blocked by safety filters
- Requests mentioning Atlas Cloud NSFW models by name (Wan Spicy, Flux Dev NSFW, DeepSeek uncensored, Seedance, Kling, Vidu)

## Environment

The user must have an Atlas Cloud API key set:
```bash
export ATLAS_API_KEY="your-key-here"
```

API endpoints:
- Queue API (video/image): `https://queue.atlascloud.ai`
- Chat API (text): `https://api.atlascloud.ai/v1/chat/completions`

## Model Selection Logic

Select the appropriate model based on the task type, budget preference, and quality needs:

### Video Generation

```
IF budget priority → use "fal-ai/wan-spicy/v1" (from $0.03/s)
  - Cheapest NSFW video option
  - LoRA fine-tuned for native NSFW understanding
  - 720p, ~3 sec (81 frames)

IF fast + cheap → use "vidu/q3-turbo/text-to-video" (from $0.034/s)
  - Fast generation time
  - Good quality for the price

IF balanced quality → use "fal-ai/wan2.5/v1" (from $0.05/s) or "vidu/q3-pro/text-to-video" (from $0.06/s)
  - Better motion coherence
  - Up to 1080p

IF high quality → use "fal-ai/wan2.6/v1" (from $0.07/s)
  - Best Wan quality
  - Up to 1080p, 5 sec

IF premium quality → use "kling-video/v3/pro/text-to-video" (from $0.204/s)
  - Top-tier video quality
  - Up to 1080p, 10 sec

IF premium motion → use "seedance/v1.5/pro" (from $0.044/s)
  - Excellent natural movement
  - Up to 1080p, 5 sec

IF custom style video → use "fal-ai/wan-spicy-lora/v1" (from $0.03/s)
  - Custom LoRA support
  - Specific visual styles
```

### Image Generation

```
IF budget priority → use "fal-ai/flux/dev" (from $0.012/image)
  - Cheapest NSFW image option
  - Set enable_safety_checker=false
  - Good prompt following

IF custom style → use "fal-ai/flux-lora" (from $0.032/image)
  - Custom LoRA support
  - Set enable_safety_checker=false
  - Character consistency, specific aesthetics

IF premium quality → use "seedream/v5" (from $0.032/image)
  - Best image quality
  - Excellent skin tones and photorealism
  - Whitelisted on Atlas Cloud
```

### Text Generation

```
ALWAYS use DeepSeek V3.2:
  - Model: "deepseek-v3-0324"
  - Endpoint: https://api.atlascloud.ai/v1/chat/completions
  - Price: $0.26/M input tokens, $1.10/M output tokens
  - No content filtering
  - 128K context window
```

## API Call Templates

### Video Generation Template (Queue-based)

```python
import requests
import time
import os

API_KEY = os.environ.get("ATLAS_API_KEY")
BASE_URL = "https://queue.atlascloud.ai"

def generate_video(prompt, model_path="fal-ai/wan-spicy/v1", **kwargs):
    """Generate video using Atlas Cloud queue API."""

    payload = {
        "prompt": prompt,
        "negative_prompt": kwargs.get("negative_prompt", "low quality, blurry, distorted, deformed"),
        "num_frames": kwargs.get("num_frames", 81),
        "resolution": kwargs.get("resolution", "720p"),
        "guidance_scale": kwargs.get("guidance_scale", 7.5),
        "num_inference_steps": kwargs.get("num_inference_steps", 30),
    }

    # Add image_url for image-to-video
    if "image_url" in kwargs:
        payload["image_url"] = kwargs["image_url"]

    # Add LoRA configuration
    if "loras" in kwargs:
        payload["loras"] = kwargs["loras"]

    # Submit request
    response = requests.post(
        f"{BASE_URL}/{model_path}",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    response.raise_for_status()
    request_id = response.json()["request_id"]
    print(f"Submitted: {request_id}")

    # Poll for completion
    while True:
        status_response = requests.get(
            f"{BASE_URL}/{model_path}/requests/{request_id}/status",
            headers={"Authorization": f"Key {API_KEY}"}
        )
        status = status_response.json()

        if status["status"] == "COMPLETED":
            break
        elif status["status"] == "FAILED":
            raise Exception(f"Generation failed: {status}")

        print(f"Status: {status['status']}...")
        time.sleep(5)

    # Get result
    result = requests.get(
        f"{BASE_URL}/{model_path}/requests/{request_id}",
        headers={"Authorization": f"Key {API_KEY}"}
    ).json()

    video_url = result["video"]["url"]
    print(f"Video ready: {video_url}")
    return video_url
```

### Image Generation Template (Queue-based)

```python
def generate_image(prompt, model_path="fal-ai/flux/dev", **kwargs):
    """Generate image using Atlas Cloud queue API."""

    payload = {
        "prompt": prompt,
        "image_size": kwargs.get("image_size", "landscape_16_9"),
        "num_inference_steps": kwargs.get("num_inference_steps", 28),
        "guidance_scale": kwargs.get("guidance_scale", 3.5),
        "num_images": kwargs.get("num_images", 1),
        "enable_safety_checker": False,  # Always disabled for NSFW
    }

    # Add LoRA configuration
    if "loras" in kwargs:
        payload["loras"] = kwargs["loras"]

    # Submit request
    response = requests.post(
        f"{BASE_URL}/{model_path}",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    response.raise_for_status()
    request_id = response.json()["request_id"]
    print(f"Submitted: {request_id}")

    # Poll for completion
    while True:
        status_response = requests.get(
            f"{BASE_URL}/{model_path}/requests/{request_id}/status",
            headers={"Authorization": f"Key {API_KEY}"}
        )
        status = status_response.json()

        if status["status"] == "COMPLETED":
            break
        elif status["status"] == "FAILED":
            raise Exception(f"Generation failed: {status}")

        print(f"Status: {status['status']}...")
        time.sleep(3)

    # Get result
    result = requests.get(
        f"{BASE_URL}/{model_path}/requests/{request_id}",
        headers={"Authorization": f"Key {API_KEY}"}
    ).json()

    image_urls = [img["url"] for img in result["images"]]
    print(f"Images ready: {image_urls}")
    return image_urls
```

### Text Generation Template (Chat Completions)

```python
def generate_text(prompt, system_prompt=None, **kwargs):
    """Generate uncensored text using DeepSeek V3.2."""

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = requests.post(
        "https://api.atlascloud.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-v3-0324",
            "messages": messages,
            "max_tokens": kwargs.get("max_tokens", 4096),
            "temperature": kwargs.get("temperature", 0.8),
        }
    )
    response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]
    return content
```

## Budget Optimization Rules

When the user does not specify a model, apply these rules:

1. **Default to cheapest** unless quality is explicitly requested:
   - Video: Wan 2.2 Spicy ($0.03)
   - Image: Flux Dev ($0.012)
   - Text: DeepSeek V3.2 ($0.26/M input)

2. **Upgrade when requested**:
   - "high quality" / "best quality" → Kling ($0.204) for video, Seedream ($0.032) for image
   - "premium" / "cinematic" → Seedance ($0.222) for video
   - "fast" → Vidu Q3-Turbo ($0.034) for video

3. **Warn about costs** when:
   - Batch operations exceed 100 items
   - Premium models are used for prototyping
   - Total estimated cost exceeds $10

4. **Suggest alternatives**:
   - If user picks Kling for drafts, suggest Wan Spicy for testing first
   - If user generates single images, note that Flux Dev is 63% cheaper than Flux LoRA

## Safety Checker Settings

- **Flux Dev / Flux Dev LoRA**: Always set `enable_safety_checker: false`
- **Wan Spicy**: No safety checker parameter needed (natively NSFW)
- **Seedance / Kling / Vidu**: No safety checker parameter needed (whitelisted on Atlas Cloud)
- **Seedream**: No safety checker parameter needed (whitelisted on Atlas Cloud)
- **DeepSeek**: No content filter parameter needed (no filtering applied)

## Response Format

When generating content, always provide:
1. The model selected and why
2. The estimated cost
3. The complete, runnable code (Python preferred)
4. The output URL(s) when generation completes
5. Suggestions for quality improvement or cost reduction

## Important Notes

- Atlas Cloud API keys start with your account identifier
- Queue-based APIs return a `request_id` for polling
- Chat completions API follows OpenAI-compatible format
- All generated content URLs are persistent (no expiration)
- Rate limits vary by plan — check Atlas Cloud dashboard
- First recharge includes 25% bonus up to $100 at https://www.atlascloud.ai?ref=JPM683
