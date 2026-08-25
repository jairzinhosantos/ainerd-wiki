# AI Nerd Wiki — contenido

Capítulos de la [AI Nerd Wiki](https://jairzinhosantos.com/wiki), escritos en Markdown.
Este directorio está pensado para convertirse en un repositorio público: cualquier
persona puede proponer mejoras vía pull request; los cambios aprobados se publican
automáticamente en el sitio.

## Estructura

```
chapters/
  <slug>.md      ← un capítulo por archivo; el nombre del archivo es el slug de la URL
```

## Formato de un capítulo

Cada archivo empieza con frontmatter YAML seguido del cuerpo en Markdown:

```markdown
---
id: 2                      # orden en el índice
title: RAG
subtitle: Una línea que resume el capítulo
icon: fas fa-database      # icono Font Awesome
accent: c                  # clúster del grafo: f · a · c · i · g · ghost
status: available          # available | coming-soon
tags: [RAG, embeddings]
updated: 2026-07-05        # fecha del último cambio de contenido
---

## Primera sección…
```

Notas:

- El **slug** (URL) sale del nombre del archivo: `rag.md` → `/wiki/rag`.
- El **tiempo de lectura** se calcula automáticamente; no se declara.
- `accent` enlaza el capítulo con su clúster en el grafo de la portada
  (f = fundamentos, a = arquitecturas, c = capacidades, i = integración, g = sistemas).
- Empieza el cuerpo en `##` (h2): el h1 lo pone la página con el título.
- Soportado: Markdown GFM (tablas, listas de tareas), bloques de código con
  resaltado (` ```python `) y diagramas Mermaid (` ```mermaid `).

## Cómo contribuir

1. Haz un fork y edita o crea un capítulo en `chapters/`.
2. Abre un pull request describiendo el cambio.
3. Tras la revisión y el merge, el sitio se reconstruye y publica solo.
