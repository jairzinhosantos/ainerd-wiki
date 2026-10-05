# AI Nerd Wiki

Conocimiento de ingeniería de sistemas de IA: conceptos, implementaciones, arquitecturas y pruebas conectados por sus fuentes. El primer recorrido es **Harness Engineering**.

**Estado: estructura inicial y piloto editorial.** Los tres documentos iniciales son borradores de trabajo. Vamos a iterar con Jairzinho el tono, la prosa, la profundidad, los diagramas y la lectura antes de publicar artículos en la web. Incluyen fuentes primarias y una lectura estática de Pi en una revisión fija; siguen pendientes de aceptación y no constituyen un benchmark.

## Primer recorrido

1. [Harness](concepts/harness/README.md): alcance, perspectivas y responsabilidades.
2. [Ensamblaje de contexto](concepts/harness/context/context-assembly.md): la pregunta que conecta memoria, recuperación y llamada al modelo.
3. [Pi](tech/pi/README.md): primera implementación que estudiaremos con una versión identificada.

## Áreas de trabajo

| Área | Responsabilidad |
|---|---|
| [Conceptos](concepts/README.md) | Explicaciones de mecanismos y perspectivas, independientes de productos. |
| [Tecnologías](tech/README.md) | Componentes, versiones, decisiones y evidencia de implementaciones concretas. |
| [Arquitecturas](architectures/README.md) | Patrones, composiciones y escenarios propios. |
| [Comparativas](benchmarks/README.md) | Preguntas comparables, criterios, entradas conservadas y resultados. |
| [Laboratorios](labs/README.md) | Código pequeño, instrucciones y evidencia ejecutada. |
| [Catálogo](catalog/README.md) | Páginas y relaciones generadas; incluye el estado editorial. |

Las áreas se abren con contenido real. El [mapa de expansión](docs/structure.md) registra dónde crecer, sin crear un artículo vacío por cada término.

## Gestión

[Kanban y planificación](https://github.com/users/jairzinhosantos/projects/3) · [Modelo operativo](docs/project-management.md).

## Cómo participar y continuar

Lee [CONTRIBUTING.md](CONTRIBUTING.md), el [flujo de trabajo](docs/workflow.md) y las [convenciones](docs/conventions.md). El trabajo de investigación puede empezar desde una conversación existente o directamente en un agente con acceso al workspace. La wiki pública no depende de archivos privados para poder leerse o compilarse.

Las decisiones de tono y diseño siguen abiertas en el [piloto editorial](docs/editorial-pilot.md). [Cambios](log.md).

## Validación local

Python 3.11 o posterior:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/catalog.py
.venv/bin/python scripts/check.py
.venv/bin/python -m unittest discover -s tests -v
```

El catálogo no se edita a mano. CI comprueba enlaces, metadatos, identidades, relaciones y sincronización; no certifica la veracidad de una afirmación ni llama a modelos.

## Conexión con la web

El sitio actual aún utiliza `chapters/`. Esa carpeta se conserva temporalmente como compatibilidad de solo mantenimiento: no recibe contenido nuevo. Los nuevos borradores no están conectados al renderizador actual. La [migración web](docs/migration.md) define la transición y sus criterios de aceptación.
