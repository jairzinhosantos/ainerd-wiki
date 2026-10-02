# AI Nerd Wiki: content

Chapters of the [AI Nerd Wiki](https://jairzinhosantos.com/wiki), written in Markdown.
The site downloads this repository at build time and renders each published chapter
as its own page.

## Status

The wiki is in preparation. Every chapter in this repository is a draft
(`status: coming-soon`) and stays unpublished until the author reviews and validates it.

## Structure

```
chapters/
  <slug>.md      one chapter per file; the file name is the URL slug
```

## Chapter format

Each file starts with YAML frontmatter, followed by the body in Markdown:

```markdown
---
id: 2                      # order in the index
title: RAG
subtitle: One line that sums up the chapter
icon: fas fa-database      # Font Awesome icon
accent: c                  # graph cluster: f · a · c · i · g · ghost
pillar: academia           # portal pillar: academia | industria | futuro
status: available          # available | coming-soon
tags: [RAG, embeddings]
updated: 2026-07-05        # date of the last content change
---

## First section
```

Notes:

- The **slug** (URL) comes from the file name: `rag.md` becomes `/wiki/rag`.
- **Reading time** is computed automatically; do not declare it.
- `accent` links the chapter to its cluster in the home page graph
  (f = foundations, a = architectures, c = capabilities, i = integration, g = systems).
- `pillar` uses fixed keys: `academia` (Academy), `industria` (Industry), `futuro` (Future).
- Start the body at `##` (h2): the page adds the h1 from the title.
- Supported: GFM Markdown (tables, task lists), code blocks with syntax
  highlighting (` ```python `) and Mermaid diagrams (` ```mermaid `).

## Publishing

A chapter appears on the site when its `status` is `available`. After a change is
merged here, the site picks it up on its next build.
