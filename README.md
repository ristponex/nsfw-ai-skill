# NSFW AI Skill — Uncensored AI Content Generation via Atlas Cloud

An **open agent skill** for generating uncensored NSFW content — video, image, and text — using [Atlas Cloud](https://www.atlascloud.ai?ref=JPM683)'s whitelisted models. Skip the censorship walls. Get production-ready results at a fraction of the cost.

> **What is an Agent Skill?** A skill is a reusable instruction set that extends AI coding agents' capabilities. Skills work with 15+ platforms including Claude Code, Cursor, OpenAI Codex, GitHub Copilot, Gemini CLI, Windsurf, OpenCode, Kiro, and more. Install this skill and your agent will automatically know how to generate NSFW content using the best available models and APIs.

---

## Table of Contents

- [Why Atlas Cloud for NSFW?](#why-atlas-cloud-for-nsfw)
- [Features](#features)
- [Supported Models](#supported-models)
- [Price Comparison vs fal.ai](#price-comparison-vs-falai)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [API Integration Guide](#api-integration-guide)
  - [Video Generation](#video-generation)
  - [Image Generation](#image-generation)
  - [Text Generation](#text-generation)
  - [Image-to-Video Pipeline](#image-to-video-pipeline)
  - [Batch Generation](#batch-generation)
- [Usage Examples (Natural Language)](#usage-examples-natural-language)
- [Model Deep Dive](#model-deep-dive)
  - [Video Models](#video-models)
  - [Image Models](#image-models)
  - [Text Models](#text-models)
- [LoRA Support](#lora-support)
- [Multi-Model Pipelines](#multi-model-pipelines)
- [Budget Optimization](#budget-optimization)
- [Trust & Security](#trust--security)
- [FAQ](#faq)
- [Take This to Production](#-take-this-to-production-today)
- [License](#license)

---

## Why Atlas Cloud for NSFW?

Most AI platforms block NSFW content outright. The few that allow it charge premium prices and offer limited model selection. Atlas Cloud solves both problems:

- **Whitelisted Models** — Seedance, Kling, Vidu, and more are specifically enabled for NSFW on Atlas Cloud
- **No Safety Checker Overhead** — Models like Flux Dev run with `enable_safety_checker=false` by default
- **80%+ Cost Savings** — Compared to fal.ai and other providers
- **Exclusive Access** — Wan 2.2 Spicy is only available through Atlas Cloud
- **Enterprise Security** — SOC I & II Certified, HIPAA Compliant, US-based

---

## Features

### NSFW Video Generation
- **Wan 2.2 Spicy** — LoRA fine-tuned model purpose-built for NSFW video, only $0.03/request
- **Wan 2.2 Spicy LoRA** — Custom LoRA variants for specific styles and aesthetics
- **Wan 2.5/2.6** — High-quality uncensored video generation with extended duration support
- **Seedance v1.5 Pro** — Premium video quality, whitelisted exclusively on Atlas Cloud
- **Kling v3.0 Pro** — Top-tier video generation, 82% cheaper than fal.ai
- **Vidu Q3-Pro / Q3-Turbo** — Fast, affordable NSFW video at scale

### NSFW Image Generation
- **Flux Dev** — Industry-standard image generation with `enable_safety_checker=false`
- **Flux Dev LoRA** — Custom LoRA models for specific styles, characters, and aesthetics
- **Seedream v5.0** — Next-generation image model, whitelisted on Atlas Cloud

### Uncensored Text Generation
- **DeepSeek V3.2** — Full uncensored text generation with no content filtering
- Story writing, dialogue, scene descriptions, character development
- System prompt support for consistent character voice

### Advanced Pipelines
- **Image-to-Video** — Generate a still image, then animate it into video
- **Text-to-Image-to-Video** — Full pipeline from text description to final video
- **Batch Generation** — Generate multiple variations in parallel
- **LoRA Chaining** — Combine multiple LoRA models for unique styles

---

## Supported Models

### Complete Model Reference

| Model | Type | Price | Method | Best For |
|:------|:-----|:------|:-------|:---------|
| Wan 2.2 Spicy | Video | $0.03/req | LoRA fine-tuned, native NSFW | Budget NSFW video |
| Wan 2.2 Spicy LoRA | Video | $0.03/req | Custom LoRA variants | Styled NSFW video |
| Wan 2.5 | Video | $0.05/req | Uncensored mode | Mid-range video |
| Wan 2.6 | Video | $0.07/req | Uncensored mode | High-quality video |
| Seedance v1.5 Pro | Video | $0.222/req | Whitelisted on Atlas Cloud | Premium video |
| Kling v3.0 Pro | Video | $0.204/req | Whitelisted on Atlas Cloud | Top-tier video |
| Vidu Q3-Pro | Video | $0.06/req | Whitelisted on Atlas Cloud | Quality + value |
| Vidu Q3-Turbo | Video | $0.034/req | Whitelisted on Atlas Cloud | Fast + cheap |

> ⚠️ **Note:** Vidu Q3 models may add mosaic/blur to certain NSFW scenes due to training data limitations. Not guaranteed 100% uncensored. For reliable uncensored output, use **Wan 2.2 Spicy** ($0.03) or **Wan 2.6** ($0.07).
| Flux Dev | Image | $0.012/req | enable_safety_checker=false | Budget NSFW image |
| Flux Dev LoRA | Image | $0.032/req | Custom LoRA + safety off | Styled NSFW image |
| Seedream v5.0 | Image | $0.032/req | Whitelisted on Atlas Cloud | Premium image |
| DeepSeek V3.2 | Text | $0.26/M input | No content filtering | Stories & dialogue |

### Model Selection Guide

```
Budget Video     → Wan 2.2 Spicy ($0.03)
Quality Video    → Wan 2.6 ($0.07) or Vidu Q3-Pro ($0.06)*
Premium Video    → Kling v3.0 Pro ($0.204) or Seedance v1.5 Pro ($0.222)
Fast Video       → Vidu Q3-Turbo ($0.034)*

* Vidu Q3 may add mosaic/blur to certain NSFW scenes. Use Wan models for reliable uncensored output.
Budget Image     → Flux Dev ($0.012)
Styled Image     → Flux Dev LoRA ($0.032)
Premium Image    → Seedream v5.0 ($0.032)
Text/Stories     → DeepSeek V3.2 ($0.26/M input tokens)
```

---

## Price Comparison vs fal.ai

| Model | fal.ai | Atlas Cloud | Savings |
|:------|:-------|:------------|:--------|
| Wan 2.2 Spicy | N/A (not available) | $0.03/req | **Atlas Exclusive** |
| Wan 2.2 Spicy LoRA | N/A (not available) | $0.03/req | **Atlas Exclusive** |
| Wan 2.5 (5sec) | $0.25/req | $0.05/req | **80% cheaper** |
| Wan 2.6 (5sec) | $0.35/req | $0.07/req | **80% cheaper** |
| Seedance v1.5 Pro | N/A (not available) | $0.222/req | **Atlas Exclusive** |
| Kling v3.0 (5sec) | $1.12/req | $0.204/req | **82% cheaper** |
| Vidu Q3-Pro | N/A (not available) | $0.06/req | **Atlas Exclusive** |
| Vidu Q3-Turbo | N/A (not available) | $0.034/req | **Atlas Exclusive** |
| Flux Dev | $0.025/req | $0.012/req | **52% cheaper** |
| Flux Dev LoRA | $0.050/req | $0.032/req | **36% cheaper** |
| Seedream v5.0 | N/A (not available) | $0.032/req | **Atlas Exclusive** |

> **Bottom line**: Atlas Cloud is 36-82% cheaper on shared models, and offers 6+ exclusive models not available anywhere else.

---

## Quick Start

### 1. Get Your API Key

Sign up at [Atlas Cloud](https://www.atlascloud.ai?ref=JPM683) and grab your API key from the dashboard.

```bash
export ATLAS_API_KEY="your-api-key-here"
```

### 2. Install the Skill

Add this skill to your agent:

```
npx skills add https://github.com/thoughtincode/nsfw-ai-skill
```

### 3. Start Generating

Just tell Claude what you want:

```
Generate an artistic nude video with soft lighting using Wan Spicy
```

---

## Installation

### As an Agent Skill

Works with Claude Code, Cursor, OpenAI Codex, GitHub Copilot, Gemini CLI, Windsurf, OpenCode, Kiro, and 15+ AI coding agents.

```bash
# Add the skill to your agent
npx skills add https://github.com/thoughtincode/nsfw-ai-skill
```

### Manual Setup

```bash
# Clone the repository
git clone https://github.com/thoughtincode/nsfw-ai-skill.git
cd nsfw-ai-skill

# Set your API key
export ATLAS_API_KEY="your-api-key-here"

# Run examples
python examples/video-generation.py
python examples/image-generation.py
python examples/batch-pipeline.py
```

### Dependencies

```bash
pip install requests
```

No other dependencies required. The skill uses Atlas Cloud's REST API directly.

---

## API Integration Guide

### Base URL and Authentication

All Atlas Cloud API requests use the same base pattern:

```
Base URL: https://queue.atlascloud.ai
Auth Header: Authorization: Key {ATLAS_API_KEY}
```

The API follows a queue-based pattern:
1. **Submit** a request → get a `request_id`
2. **Poll** for status → get the result when complete

---

### Video Generation

#### Wan 2.2 Spicy — Budget NSFW Video ($0.03/req)

**cURL:**

```bash
# Submit video generation request
curl -X POST "https://queue.atlascloud.ai/fal-ai/wan-spicy/v1" \
  -H "Authorization: Key ${ATLAS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A graceful figure dancing in golden sunset light, flowing silk fabric, artistic cinematography, warm color palette",
    "negative_prompt": "low quality, blurry, distorted, deformed",
    "num_frames": 81,
    "resolution": "720p",
    "guidance_scale": 7.5,
    "num_inference_steps": 30
  }'

# Response: {"request_id": "abc123..."}

# Poll for result
curl -X GET "https://queue.atlascloud.ai/fal-ai/wan-spicy/requests/abc123/status" \
  -H "Authorization: Key ${ATLAS_API_KEY}"

# When complete, get result
curl -X GET "https://queue.atlascloud.ai/fal-ai/wan-spicy/requests/abc123" \
  -H "Authorization: Key ${ATLAS_API_KEY}"
```

**Python:**

```python
import requests
import time

API_KEY = "your-api-key"
BASE_URL = "https://queue.atlascloud.ai"

def generate_video_wan_spicy(prompt, negative_prompt="", num_frames=81):
    """Generate NSFW video using Wan 2.2 Spicy model."""

    # Submit request
    response = requests.post(
        f"{BASE_URL}/fal-ai/wan-spicy/v1",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "negative_prompt": negative_prompt or "low quality, blurry, distorted",
            "num_frames": num_frames,
            "resolution": "720p",
            "guidance_scale": 7.5,
            "num_inference_steps": 30
        }
    )
    request_id = response.json()["request_id"]
    print(f"Request submitted: {request_id}")

    # Poll for completion
    while True:
        status = requests.get(
            f"{BASE_URL}/fal-ai/wan-spicy/requests/{request_id}/status",
            headers={"Authorization": f"Key {API_KEY}"}
        ).json()

        if status["status"] == "COMPLETED":
            break
        elif status["status"] == "FAILED":
            raise Exception(f"Generation failed: {status}")

        print(f"Status: {status['status']}...")
        time.sleep(5)

    # Get result
    result = requests.get(
        f"{BASE_URL}/fal-ai/wan-spicy/requests/{request_id}",
        headers={"Authorization": f"Key {API_KEY}"}
    ).json()

    return result["video"]["url"]


video_url = generate_video_wan_spicy(
    prompt="Elegant figure in flowing dress, artistic dance movement, golden hour lighting",
)
print(f"Video URL: {video_url}")
```

**JavaScript:**

```javascript
const API_KEY = "your-api-key";
const BASE_URL = "https://queue.atlascloud.ai";

async function generateVideoWanSpicy(prompt, options = {}) {
  // Submit request
  const submitRes = await fetch(`${BASE_URL}/fal-ai/wan-spicy/v1`, {
    method: "POST",
    headers: {
      "Authorization": `Key ${API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      prompt,
      negative_prompt: options.negativePrompt || "low quality, blurry, distorted",
      num_frames: options.numFrames || 81,
      resolution: options.resolution || "720p",
      guidance_scale: options.guidanceScale || 7.5,
      num_inference_steps: options.numInferenceSteps || 30
    })
  });

  const { request_id } = await submitRes.json();
  console.log(`Request submitted: ${request_id}`);

  // Poll for completion
  while (true) {
    const statusRes = await fetch(
      `${BASE_URL}/fal-ai/wan-spicy/requests/${request_id}/status`,
      { headers: { "Authorization": `Key ${API_KEY}` } }
    );
    const status = await statusRes.json();

    if (status.status === "COMPLETED") break;
    if (status.status === "FAILED") throw new Error(`Generation failed: ${JSON.stringify(status)}`);

    console.log(`Status: ${status.status}...`);
    await new Promise(r => setTimeout(r, 5000));
  }

  // Get result
  const resultRes = await fetch(
    `${BASE_URL}/fal-ai/wan-spicy/requests/${request_id}`,
    { headers: { "Authorization": `Key ${API_KEY}` } }
  );
  const result = await resultRes.json();

  return result.video.url;
}

// Usage
const videoUrl = await generateVideoWanSpicy(
  "Elegant figure in flowing dress, artistic dance movement, golden hour lighting"
);
console.log(`Video URL: ${videoUrl}`);
```

#### Kling v3.0 Pro — Premium Video ($0.204/req)

```python
def generate_video_kling(prompt, image_url=None, duration=5):
    """Generate premium NSFW video using Kling v3.0 Pro."""

    payload = {
        "prompt": prompt,
        "negative_prompt": "low quality, blurry, distorted",
        "duration": duration,
        "aspect_ratio": "16:9"
    }

    if image_url:
        payload["image_url"] = image_url

    response = requests.post(
        f"{BASE_URL}/kling-video/v3/pro/text-to-video",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    request_id = response.json()["request_id"]

    # Poll and return (same pattern as above)
    return poll_for_result(f"kling-video/v3/pro/text-to-video", request_id)
```

#### Seedance v1.5 Pro — Premium Video ($0.222/req)

```python
def generate_video_seedance(prompt, image_url=None):
    """Generate premium NSFW video using Seedance v1.5 Pro."""

    payload = {
        "prompt": prompt,
        "negative_prompt": "low quality, blurry, distorted",
        "duration": 5,
        "seed": -1
    }

    if image_url:
        payload["image_url"] = image_url

    response = requests.post(
        f"{BASE_URL}/seedance/v1.5/pro",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    request_id = response.json()["request_id"]

    return poll_for_result("seedance/v1.5/pro", request_id)
```

#### Vidu Q3 — Fast & Affordable ($0.034-0.06/req)

> ⚠️ **Note:** Vidu Q3 models may add mosaic/blur to certain NSFW scenes due to training data limitations. Not guaranteed 100% uncensored. For reliable uncensored output, use **Wan 2.2 Spicy** ($0.03) or **Wan 2.6** ($0.07).

```python
def generate_video_vidu(prompt, turbo=True):
    """Generate NSFW video using Vidu Q3. Use turbo=True for speed, False for quality."""

    model = "vidu/q3-turbo" if turbo else "vidu/q3-pro"

    response = requests.post(
        f"{BASE_URL}/{model}/text-to-video",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "duration": 5,
            "aspect_ratio": "16:9"
        }
    )
    request_id = response.json()["request_id"]

    return poll_for_result(f"{model}/text-to-video", request_id)
```

---

### Image Generation

#### Flux Dev — Budget NSFW Image ($0.012/req)

**cURL:**

```bash
curl -X POST "https://queue.atlascloud.ai/fal-ai/flux/dev" \
  -H "Authorization: Key ${ATLAS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Professional art photography, elegant figure study, dramatic studio lighting, high contrast, museum quality",
    "image_size": "landscape_16_9",
    "num_inference_steps": 28,
    "guidance_scale": 3.5,
    "num_images": 1,
    "enable_safety_checker": false
  }'
```

**Python:**

```python
def generate_image_flux(prompt, image_size="landscape_16_9", num_images=1):
    """Generate NSFW image using Flux Dev with safety checker disabled."""

    response = requests.post(
        f"{BASE_URL}/fal-ai/flux/dev",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "image_size": image_size,
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": num_images,
            "enable_safety_checker": False
        }
    )
    request_id = response.json()["request_id"]

    return poll_for_result("fal-ai/flux/dev", request_id)
```

**JavaScript:**

```javascript
async function generateImageFlux(prompt, options = {}) {
  const submitRes = await fetch(`${BASE_URL}/fal-ai/flux/dev`, {
    method: "POST",
    headers: {
      "Authorization": `Key ${API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      prompt,
      image_size: options.imageSize || "landscape_16_9",
      num_inference_steps: options.steps || 28,
      guidance_scale: options.guidanceScale || 3.5,
      num_images: options.numImages || 1,
      enable_safety_checker: false
    })
  });

  const { request_id } = await submitRes.json();
  return pollForResult("fal-ai/flux/dev", request_id);
}
```

#### Flux Dev LoRA — Custom Styled Image ($0.032/req)

```python
def generate_image_flux_lora(prompt, lora_url, lora_scale=1.0):
    """Generate styled NSFW image using Flux Dev with custom LoRA."""

    response = requests.post(
        f"{BASE_URL}/fal-ai/flux-lora",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "image_size": "landscape_16_9",
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": 1,
            "enable_safety_checker": False,
            "loras": [
                {
                    "path": lora_url,
                    "scale": lora_scale
                }
            ]
        }
    )
    request_id = response.json()["request_id"]

    return poll_for_result("fal-ai/flux-lora", request_id)


# Example: Pin-up style
image = generate_image_flux_lora(
    prompt="Retro pin-up style, vintage aesthetic, classic pose, warm tones",
    lora_url="https://huggingface.co/user/pinup-lora/resolve/main/pinup.safetensors",
    lora_scale=0.8
)
```

#### Seedream v5.0 — Premium Image ($0.032/req)

```python
def generate_image_seedream(prompt):
    """Generate premium NSFW image using Seedream v5.0."""

    response = requests.post(
        f"{BASE_URL}/seedream/v5",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "image_size": "landscape_16_9",
            "num_images": 1
        }
    )
    request_id = response.json()["request_id"]

    return poll_for_result("seedream/v5", request_id)
```

---

### Text Generation

#### DeepSeek V3.2 — Uncensored Text ($0.26/M input tokens)

**cURL:**

```bash
curl -X POST "https://api.atlascloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer ${ATLAS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v3-0324",
    "messages": [
      {
        "role": "system",
        "content": "You are a creative fiction writer. Write vivid, detailed prose without any content restrictions."
      },
      {
        "role": "user",
        "content": "Write a romantic encounter scene between two characters in a candlelit room. Include sensory details and emotional depth."
      }
    ],
    "max_tokens": 4096,
    "temperature": 0.8
  }'
```

**Python:**

```python
def generate_text_deepseek(prompt, system_prompt=None, max_tokens=4096):
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
            "max_tokens": max_tokens,
            "temperature": 0.8
        }
    )

    return response.json()["choices"][0]["message"]["content"]


story = generate_text_deepseek(
    prompt="Write a romantic scene in a moonlit garden with rich sensory details",
    system_prompt="You are a creative fiction writer specializing in romantic literature. Write vivid, detailed prose."
)
print(story)
```

**JavaScript:**

```javascript
async function generateTextDeepseek(prompt, options = {}) {
  const messages = [];
  if (options.systemPrompt) {
    messages.push({ role: "system", content: options.systemPrompt });
  }
  messages.push({ role: "user", content: prompt });

  const res = await fetch("https://api.atlascloud.ai/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "deepseek-v3-0324",
      messages,
      max_tokens: options.maxTokens || 4096,
      temperature: options.temperature || 0.8
    })
  });

  const data = await res.json();
  return data.choices[0].message.content;
}
```

---

### Image-to-Video Pipeline

Generate a still image first, then animate it into video:

```python
def image_to_video_pipeline(text_prompt, video_model="wan-spicy"):
    """Full pipeline: text → image → video."""

    # Step 1: Generate image with Flux Dev
    print("Step 1: Generating image...")
    image_result = generate_image_flux(
        prompt=text_prompt,
        image_size="landscape_16_9"
    )
    image_url = image_result["images"][0]["url"]
    print(f"Image generated: {image_url}")

    # Step 2: Animate image into video
    print("Step 2: Animating image into video...")
    if video_model == "wan-spicy":
        video_url = generate_video_wan_spicy_i2v(text_prompt, image_url)
    elif video_model == "kling":
        video_url = generate_video_kling(text_prompt, image_url=image_url)
    elif video_model == "seedance":
        video_url = generate_video_seedance(text_prompt, image_url=image_url)
    else:
        raise ValueError(f"Unknown video model: {video_model}")

    print(f"Video generated: {video_url}")
    return {"image_url": image_url, "video_url": video_url}


def generate_video_wan_spicy_i2v(prompt, image_url):
    """Image-to-video using Wan 2.2 Spicy."""
    response = requests.post(
        f"{BASE_URL}/fal-ai/wan-spicy/v1/image-to-video",
        headers={
            "Authorization": f"Key {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": prompt,
            "image_url": image_url,
            "negative_prompt": "low quality, blurry, distorted",
            "num_frames": 81,
            "resolution": "720p",
            "guidance_scale": 7.5,
            "num_inference_steps": 30
        }
    )
    request_id = response.json()["request_id"]
    return poll_for_result("fal-ai/wan-spicy/v1/image-to-video", request_id)


# Usage
result = image_to_video_pipeline(
    text_prompt="Graceful figure in flowing silk, gentle movement, warm studio lighting",
    video_model="wan-spicy"
)
```

---

### Batch Generation

Generate multiple variations efficiently:

```python
import concurrent.futures

def batch_generate_images(prompts, max_workers=5):
    """Generate multiple images in parallel."""

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(generate_image_flux, prompt): prompt
            for prompt in prompts
        }
        for future in concurrent.futures.as_completed(futures):
            prompt = futures[future]
            try:
                result = future.result()
                results.append({
                    "prompt": prompt,
                    "url": result["images"][0]["url"],
                    "status": "success"
                })
            except Exception as e:
                results.append({
                    "prompt": prompt,
                    "error": str(e),
                    "status": "failed"
                })

    return results


# Generate 10 variations
prompts = [
    f"Artistic figure study, pose variation {i}, dramatic lighting, studio photography"
    for i in range(1, 11)
]
results = batch_generate_images(prompts)

for r in results:
    if r["status"] == "success":
        print(f"✓ {r['prompt'][:50]}... → {r['url']}")
    else:
        print(f"✗ {r['prompt'][:50]}... → {r['error']}")
```

---

## Usage Examples (Natural Language)

Once the skill is installed, just tell Claude what you want in plain English:

### Video Generation
```
"Generate an artistic nude video with soft lighting using Wan Spicy"
"Create a 5-second dance video with flowing fabric, use Kling for best quality"
"Make a quick NSFW video test with Vidu Turbo to keep costs low"
"Generate a cinematic intimate scene with Seedance v1.5"
```

### Image Generation
```
"Create a pin-up style image in retro aesthetic using Flux Dev"
"Generate an artistic nude photograph with dramatic chiaroscuro lighting"
"Make a series of 5 boudoir-style images with consistent character"
"Create a fantasy art piece with a sensual theme using Seedream"
```

### Text Generation
```
"Write a romantic scene with detailed descriptions using DeepSeek"
"Create a steamy dialogue between two characters meeting at a masquerade"
"Write 5 variations of a seduction scene in different settings"
"Generate a detailed character description for an adult visual novel"
```

### Pipeline & Batch
```
"Generate 10 variations of this character in different poses"
"Create an image of a sunset figure and then animate it into a video"
"Write a scene description, generate an image from it, then make it a video"
"Batch generate 20 images and pick the best 5 for video animation"
```

---

## Model Deep Dive

### Video Models

#### Wan 2.2 Spicy
- **Price**: $0.03/request
- **Method**: LoRA fine-tuned specifically for NSFW content
- **Resolution**: Up to 720p
- **Duration**: ~3 seconds (81 frames at 24fps)
- **Strengths**: Native NSFW understanding, cheapest option, fast generation
- **Best for**: Budget production, rapid prototyping, bulk generation
- **Exclusive**: Only available on Atlas Cloud

#### Wan 2.2 Spicy LoRA
- **Price**: $0.03/request
- **Method**: Custom LoRA variants on top of Wan Spicy base
- **Strengths**: Specialized styles (anime, realistic, artistic)
- **Best for**: Consistent style across multiple generations

#### Wan 2.5 / 2.6
- **Price**: $0.05-0.07/request
- **Method**: Uncensored mode enabled on Atlas Cloud
- **Resolution**: Up to 1080p
- **Duration**: Up to 5 seconds
- **Strengths**: Higher quality than Wan 2.2, better motion coherence
- **Best for**: Mid-range quality needs

#### Seedance v1.5 Pro
- **Price**: $0.222/request
- **Method**: Whitelisted on Atlas Cloud for NSFW
- **Resolution**: Up to 1080p
- **Duration**: Up to 5 seconds
- **Strengths**: Excellent motion quality, natural movement
- **Best for**: Premium content, professional production

#### Kling v3.0 Pro
- **Price**: $0.204/request
- **Method**: Whitelisted on Atlas Cloud for NSFW
- **Resolution**: Up to 1080p
- **Duration**: Up to 10 seconds
- **Strengths**: Best overall video quality, longest duration
- **Best for**: Top-tier content, client deliverables

#### Vidu Q3-Pro / Q3-Turbo
- **Price**: $0.06 (Pro) / $0.034 (Turbo) per request
- **Method**: Whitelisted on Atlas Cloud for NSFW
- **Strengths**: Fast generation, good quality-to-price ratio
- **Best for**: Production workloads, cost-effective quality

> ⚠️ **Note:** Vidu Q3 models may add mosaic/blur to certain NSFW scenes due to training data limitations. Not guaranteed 100% uncensored. For reliable uncensored output, use **Wan 2.2 Spicy** ($0.03) or **Wan 2.6** ($0.07).

### Image Models

#### Flux Dev
- **Price**: $0.012/request
- **Method**: `enable_safety_checker=false`
- **Resolution**: Multiple aspect ratios supported
- **Strengths**: Industry standard, excellent prompt following
- **Best for**: General NSFW image generation, budget production

#### Flux Dev LoRA
- **Price**: $0.032/request
- **Method**: Custom LoRA + `enable_safety_checker=false`
- **Strengths**: Custom styles, character consistency
- **Best for**: Branded content, specific aesthetics, character sheets

#### Seedream v5.0
- **Price**: $0.032/request
- **Method**: Whitelisted on Atlas Cloud
- **Strengths**: Next-gen image quality, excellent skin tones
- **Best for**: Photorealistic content, premium stills

### Text Models

#### DeepSeek V3.2
- **Price**: $0.26/M input tokens, $1.10/M output tokens
- **Method**: No content filtering applied
- **Context**: 128K tokens
- **Strengths**: Excellent creative writing, nuanced character voice
- **Best for**: Story writing, scene descriptions, dialogue, scripts

---

## LoRA Support

### Using Custom LoRAs with Flux Dev

```python
# Single LoRA
result = generate_image_flux_lora(
    prompt="Your prompt here",
    lora_url="https://huggingface.co/user/model/resolve/main/model.safetensors",
    lora_scale=0.8
)

# Multiple LoRAs
response = requests.post(
    f"{BASE_URL}/fal-ai/flux-lora",
    headers={
        "Authorization": f"Key {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "prompt": "Your prompt here",
        "enable_safety_checker": False,
        "loras": [
            {
                "path": "https://huggingface.co/user/style-lora/resolve/main/style.safetensors",
                "scale": 0.7
            },
            {
                "path": "https://huggingface.co/user/character-lora/resolve/main/char.safetensors",
                "scale": 0.5
            }
        ]
    }
)
```

### Using Custom LoRAs with Wan Spicy

```python
response = requests.post(
    f"{BASE_URL}/fal-ai/wan-spicy-lora/v1",
    headers={
        "Authorization": f"Key {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "prompt": "Your prompt here",
        "loras": [
            {
                "path": "https://huggingface.co/user/video-lora/resolve/main/video.safetensors",
                "scale": 0.8
            }
        ],
        "num_frames": 81,
        "resolution": "720p"
    }
)
```

### Finding LoRAs

- **Hugging Face**: Search for NSFW/uncensored LoRAs on [huggingface.co](https://huggingface.co)
- **CivitAI**: Browse community LoRAs at [civitai.com](https://civitai.com)
- **Custom Training**: Train your own LoRA using tools like kohya_ss

---

## Multi-Model Pipelines

### Text → Image → Video (Full Pipeline)

```python
def full_pipeline(description, style="realistic"):
    """Complete pipeline from text description to final video."""

    # Step 1: Generate detailed scene description with DeepSeek
    print("Step 1: Generating detailed scene description...")
    detailed_prompt = generate_text_deepseek(
        prompt=f"Write a detailed visual description (2-3 sentences) of this scene for image generation: {description}. Style: {style}. Focus on lighting, composition, colors, and mood.",
        system_prompt="You are a prompt engineer for AI image generation. Write concise, vivid visual descriptions.",
        max_tokens=200
    )
    print(f"Enhanced prompt: {detailed_prompt}")

    # Step 2: Generate image with Flux Dev
    print("Step 2: Generating image...")
    image_result = generate_image_flux(detailed_prompt)
    image_url = image_result["images"][0]["url"]
    print(f"Image: {image_url}")

    # Step 3: Animate with Wan Spicy (cheapest) or Kling (best quality)
    print("Step 3: Animating video...")
    video_result = generate_video_wan_spicy_i2v(detailed_prompt, image_url)
    print(f"Video: {video_result}")

    return {
        "description": description,
        "enhanced_prompt": detailed_prompt,
        "image_url": image_url,
        "video_url": video_result
    }


result = full_pipeline(
    description="A mysterious figure emerging from shadows in a candlelit room",
    style="noir cinematic"
)
```

### Batch Image → Video Pipeline

```python
def batch_image_to_video(prompts, image_model="flux", video_model="wan-spicy", max_workers=3):
    """Generate multiple image-to-video pipelines in parallel."""

    results = []

    # Step 1: Generate all images in parallel
    print(f"Generating {len(prompts)} images...")
    images = batch_generate_images(prompts, max_workers=max_workers)

    # Step 2: Animate successful images into videos
    successful_images = [img for img in images if img["status"] == "success"]
    print(f"Animating {len(successful_images)} images into videos...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for img in successful_images:
            future = executor.submit(
                generate_video_wan_spicy_i2v,
                img["prompt"],
                img["url"]
            )
            futures[future] = img

        for future in concurrent.futures.as_completed(futures):
            img = futures[future]
            try:
                video_url = future.result()
                results.append({
                    "prompt": img["prompt"],
                    "image_url": img["url"],
                    "video_url": video_url,
                    "status": "success"
                })
            except Exception as e:
                results.append({
                    "prompt": img["prompt"],
                    "image_url": img["url"],
                    "error": str(e),
                    "status": "failed"
                })

    return results
```

---

## Budget Optimization

### Cost Tiers

```
TIER 1 — Budget ($0.01-0.04/req)
├── Flux Dev Image:        $0.012/req  ← Cheapest image
├── Wan 2.2 Spicy Video:   $0.030/req  ← Cheapest NSFW video
├── Flux Dev LoRA Image:   $0.032/req
├── Seedream v5.0 Image:   $0.032/req
└── Vidu Q3-Turbo Video:   $0.034/req  ← Cheapest fast video

TIER 2 — Mid-Range ($0.05-0.07/req)
├── Wan 2.5 Video:         $0.050/req
├── Vidu Q3-Pro Video:     $0.060/req
└── Wan 2.6 Video:         $0.070/req

TIER 3 — Premium ($0.20+/req)
├── Kling v3.0 Pro Video:  $0.204/req  ← Best quality
└── Seedance v1.5 Pro:     $0.222/req  ← Best motion
```

### Budget Calculator

```python
def estimate_cost(num_images=0, num_videos=0, num_text_tokens=0,
                  image_model="flux", video_model="wan-spicy"):
    """Estimate total cost for a generation batch."""

    prices = {
        "flux": 0.012,
        "flux-lora": 0.032,
        "seedream": 0.032,
        "wan-spicy": 0.03,
        "wan-2.5": 0.05,
        "wan-2.6": 0.07,
        "vidu-turbo": 0.034,
        "vidu-pro": 0.06,
        "kling": 0.204,
        "seedance": 0.222,
    }

    image_cost = num_images * prices.get(image_model, 0.012)
    video_cost = num_videos * prices.get(video_model, 0.03)
    text_cost = (num_text_tokens / 1_000_000) * 0.26  # input tokens

    total = image_cost + video_cost + text_cost

    print(f"Image cost:  ${image_cost:.3f} ({num_images} × ${prices.get(image_model, 0.012)})")
    print(f"Video cost:  ${video_cost:.3f} ({num_videos} × ${prices.get(video_model, 0.03)})")
    print(f"Text cost:   ${text_cost:.3f} ({num_text_tokens:,} tokens)")
    print(f"─────────────────────")
    print(f"Total:       ${total:.3f}")

    return total


# Example: 100 images + 50 videos + 500K tokens
estimate_cost(
    num_images=100,
    num_videos=50,
    num_text_tokens=500_000,
    image_model="flux",
    video_model="wan-spicy"
)
# Image cost:  $1.200 (100 × $0.012)
# Video cost:  $1.500 (50 × $0.03)
# Text cost:   $0.130 (500,000 tokens)
# ─────────────────────
# Total:       $2.830
```

### Optimization Tips

1. **Start with Wan Spicy** ($0.03) for video prototyping, upgrade to Kling ($0.204) only for final renders
2. **Use Flux Dev** ($0.012) for image drafts, switch to Seedream ($0.032) for hero images
3. **Batch process** during off-peak hours for faster queue times
4. **Cache results** — Atlas Cloud URLs are persistent, no need to regenerate
5. **Use LoRAs** to get better first-attempt results, reducing the need for re-generation

---

## Trust & Security

> **Enterprise-Grade Security** — Atlas Cloud is SOC I & II Certified | HIPAA Compliant | US-based company. Your data and usage are protected.

### Security Features

- **SOC I & II Certified** — Annual audits by independent third parties
- **HIPAA Compliant** — Healthcare-grade data protection standards
- **US-Based** — Data stored and processed in the United States
- **API Key Authentication** — Secure key-based access control
- **No Data Retention** — Generated content is not stored or used for training
- **Encrypted Transit** — All API calls over HTTPS/TLS 1.3
- **Usage Logging** — Full audit trail of all API requests

### Compliance

Atlas Cloud maintains compliance with:
- SOC Type I and Type II
- HIPAA (Health Insurance Portability and Accountability Act)
- CCPA (California Consumer Privacy Act)
- GDPR (General Data Protection Regulation)

---

## FAQ

### Is this legal?

Yes. Generating AI content for adults is legal in most jurisdictions. You are responsible for complying with local laws regarding the distribution and use of generated content.

### Why can't I use fal.ai or Replicate for NSFW?

Most providers block NSFW content at the API level. Even when models technically support it, the safety checkers and content filters prevent generation. Atlas Cloud whitelists specific models for NSFW use, removing these restrictions.

### How fast is generation?

- **Image (Flux Dev)**: 5-15 seconds
- **Video (Wan Spicy)**: 30-90 seconds
- **Video (Kling)**: 60-180 seconds
- **Text (DeepSeek)**: 2-10 seconds (streaming)

### Can I use my own LoRAs?

Yes. Both Flux Dev LoRA and Wan Spicy LoRA support custom LoRA models hosted on Hugging Face or any public URL. See the [LoRA Support](#lora-support) section.

### What resolution are the videos?

- Wan 2.2 Spicy: Up to 720p
- Wan 2.5/2.6: Up to 1080p
- Seedance v1.5 Pro: Up to 1080p
- Kling v3.0 Pro: Up to 1080p
- Vidu Q3: Up to 720p

### Is there a free tier?

Atlas Cloud offers a pay-as-you-go model with no minimum spend. Your first recharge includes a 25% bonus (up to $100), effectively giving you free credits.

### Can I use this commercially?

Yes. Atlas Cloud's API is designed for commercial use. You own the generated content. Check the specific model licenses for any restrictions.

---

## Take This to Production Today

This workflow is optimized for Atlas Cloud. Move from experiment to enterprise-ready scale.

- **Production-Ready**: Wan 2.2 Spicy at only $0.03/video — cheapest NSFW API available
- **Enterprise Security**: SOC I & II Certified | HIPAA Compliant
- **Exclusive Models**: Whitelisted Seedance, Kling, Vidu for NSFW — only on Atlas Cloud
- **25% Bonus**: First recharge up to $100

[**Start Building on Atlas Cloud**](https://www.atlascloud.ai?ref=JPM683)

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Links

- [Atlas Cloud](https://www.atlascloud.ai?ref=JPM683) — API Provider
- [Atlas Cloud Documentation](https://docs.atlascloud.ai) — Full API Docs
- [Claude Code](https://claude.ai/code) — AI Coding Agent
- [Hugging Face](https://huggingface.co) — LoRA Model Hub

---

*Built for the open agent skills ecosystem — works with Claude Code, Cursor, Codex, Copilot, Gemini CLI, Windsurf, OpenCode, Kiro, and 15+ AI coding agents. Powered by Atlas Cloud.*
