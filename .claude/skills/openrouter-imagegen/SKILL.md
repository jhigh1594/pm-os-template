---
name: openrouter-imagegen
description: Use when generating or editing images via OpenRouter API. Triggers: generate image, create image, image from prompt, edit image, product mockup, logo generation. Alternative to gemini-imagegen when using OpenRouter models (Gemini, Flux, etc.) with OPENROUTER_API_KEY.
---

# OpenRouter Image Generation

Generate and edit images using OpenRouter's unified API. Access multiple image models (Gemini, Flux, etc.) through one endpoint. The environment variable `OPENROUTER_API_KEY` must be set.

## When to Use

- Jon requests image generation and OpenRouter is preferred (or GEMINI_API_KEY is unavailable)
- Programmatic image generation from scripts or automation
- Need to compare outputs across providers (Gemini vs Flux)
- Single API key for multiple image models

## Default Model

| Model | Modalities | Best For |
|-------|------------|----------|
| `google/gemini-2.5-flash-preview-05-20` | image, text | Fast, good quality (default) |
| `bytedance-seed/seedream-4.5` | image | Editing, portraits, text-in-image, multi-image ([docs](https://openrouter.ai/bytedance-seed/seedream-4.5)) |
| `black-forest-labs/flux-1.1-pro` | image | Image-only, high fidelity |
| `google/gemini-2.0-flash-exp:free` | image, text | Free tier |

**Seedream 4.5** (ByteDance): $0.04/image. Strong editing consistency, subject preservation, portrait refinement, small-text rendering. Use `modalities: ["image"]`.

## Quick Reference

- **Endpoint:** `https://openrouter.ai/api/v1/chat/completions`
- **Auth:** `Authorization: Bearer {OPENROUTER_API_KEY}`
- **Request:** `model`, `messages`, `modalities` (use `["image"]` for image-only models like Seedream/Flux, `["image","text"]` for Gemini)
- **Response:** `choices[0].message.images[].imageUrl.url` (base64 data URL)

## Python Client (Preferred)

Use the workspace client from `🔧 Automation/scripts/openrouter_imagegen`:

```python
# Run from 🔧 Automation/scripts, or add that directory to PYTHONPATH
from openrouter_imagegen import generate_from_prompt

# Basic generation
generate_from_prompt(
    "A kawaii-style sticker of a happy red panda",
    output_path="output.png",
)

# With specific model (e.g. Seedream 4.5 for editing/portraits/text)
generate_from_prompt(
    "Minimalist logo for Acme Corp",
    output_path="logo.png",
    model="bytedance-seed/seedream-4.5",
)

# Image editing (pass reference image)
generate_from_prompt(
    "Add a sunset to this scene",
    output_path="edited.png",
    reference_image_path="input.png",
)
```

### CLI

```bash
cd "🔧 Automation/scripts"
python -m openrouter_imagegen "Your prompt" -o output.png
python -m openrouter_imagegen "Alps fresco at dawn" -o alps.png -m bytedance-seed/seedream-4.5
python -m openrouter_imagegen "Edit this" -o result.png -r input.png
```

## Inline API Pattern (When Client Unavailable)

If the Python client cannot be used, call the API directly:

```python
import os
import base64
import re
import httpx

def openrouter_generate_image(prompt: str, output_path: str, model: str = "google/gemini-2.5-flash-preview-05-20"):
    key = os.environ["OPENROUTER_API_KEY"]
    # Image-only models (Seedream, Flux) need modalities: ["image"]; Gemini uses ["image","text"]
    modalities = ["image"] if "bytedance-seed" in model or "flux" in model or "sourceful" in model else ["image", "text"]
    resp = httpx.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}],
            "modalities": modalities,
        },
        timeout=60.0,
    )
    resp.raise_for_status()
    data = resp.json()
    images = data["choices"][0]["message"].get("images", [])
    if not images:
        raise ValueError("No images in response")
    url = images[0].get("imageUrl", {}).get("url") or images[0].get("image_url", {}).get("url")
    match = re.match(r"data:image/[^;]+;base64,(.+)", url)
    if not match:
        raise ValueError("Invalid image URL")
    Path(output_path).write_bytes(base64.b64decode(match.group(1)))
```

## Model Selection

| Use Case | Model | Notes |
|----------|-------|------|
| General purpose | `google/gemini-2.5-flash-preview-05-20` | Default, fast |
| Editing, portraits, text-in-image | `bytedance-seed/seedream-4.5` | $0.04/image, strong consistency ([OpenRouter](https://openrouter.ai/bytedance-seed/seedream-4.5)) |
| Image-only, high fidelity | `black-forest-labs/flux-1.1-pro` | Use `modalities: ["image"]` |
| Free tier | `google/gemini-2.0-flash-exp:free` | Rate limited |
| High quality | `google/gemini-3-pro-image-preview` | Slower, best quality |

Filter by `output_modalities` on [openrouter.ai/models](https://openrouter.ai/models) to find image-capable models.

## Prompting Best Practices

### Photorealistic Scenes
Include camera details: lens type, lighting, angle, mood.
> "A photorealistic close-up portrait, 85mm lens, soft golden hour light, shallow depth of field"

### Stylized Art
Specify style explicitly:
> "A kawaii-style sticker of a happy red panda, bold outlines, cel-shading, white background"

### Text in Images
Be explicit about font style and placement:
> "Create a logo with text 'Daily Grind' in clean sans-serif, black and white, coffee bean motif"

### Product Mockups
Describe lighting setup and surface:
> "Studio-lit product photo on polished concrete, three-point softbox setup, 45-degree angle"

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `OPENROUTER_API_KEY is required` | Missing env var | Set in `.env` or environment |
| `No images in response` | Model doesn't support image output | Use model with `image` in output_modalities |
| 401 Unauthorized | Invalid or expired key | Verify key at openrouter.ai/keys |
| 429 Rate limit | Too many requests | Wait or upgrade OpenRouter tier |

## Image Editing

Pass a reference image path to edit existing images:

```python
generate_from_prompt(
    "Make the sky more dramatic",
    output_path="edited.jpg",
    reference_image_path="photo.jpg",
)
```

The client encodes the reference as base64 and includes it in the message content.

## Notes

- Response format varies by model: JPEG or PNG. Use `.png` for output; decoder handles both.
- OpenRouter normalizes provider-specific schemas to OpenAI Chat API format.
- For multi-turn refinement, make sequential calls with the previous output as reference_image_path.

## Self-Learning

Before responding, read `LEARNED.md` in this skill directory when it exists and treat it as compact runtime guidance that sharpens this skill.

Rules for self-improvement:
- Keep `SKILL.md` human-owned; do not rewrite it directly from normal usage.
- Propose broader instruction changes through the central skill-learning review queue.
- Only promote specific, reusable, evidence-backed lessons into `LEARNED.md`.
