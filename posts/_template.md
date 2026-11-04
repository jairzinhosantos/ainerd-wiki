---
title: Post template
date: 2026-01-01
excerpt: Copy this file to posts/<slug>.md and replace everything. It shows what the engine renders.
tag: Template
cover: covers/<slug>.png
status: draft
---

The first paragraph is the hook. Keep it short.

## Text

Plain text, **bold**, *italic*, `inline code`, a [link](https://jairzinhosantos.com) and a footnote[^1]. Lists work as usual:

- one idea per bullet
- or numbered steps

1. first
2. second

> A quote, for a sentence worth keeping.

## Images, SVG and animations

A paragraph with a single image becomes a figure. The quoted title is the caption.

![Diagram of the loop](media/<slug>/figure.svg "Figure 1. Caption under the image.")

![An animated GIF works the same way](media/<slug>/animation.gif "Short animation.")

Two or more images in one paragraph become a gallery:

![First](media/<slug>/a.png) ![Second](media/<slug>/b.png)

## Video

A short clip from `media/` (mp4, webm or mov) gets a player:

![Blender test](media/<slug>/clip.mp4 "A clip rendered in Blender.")

A paragraph with only a YouTube URL becomes an embedded video:

https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Diagrams

```mermaid
flowchart LR
  A[Idea] --> B[Draft] --> C[Published]
```

## Code

```python
def harness(prompt: str) -> str:
    return prompt.strip()
```

## Table

| Column | Meaning |
|---|---|
| date | sorts the list |
| status | draft or published |

[^1]: References go at the end, like this.
