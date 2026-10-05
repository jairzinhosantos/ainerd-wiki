# Gestión del proyecto

El [Project de AI Nerd](https://github.com/users/jairzinhosantos/projects/3) reúne wiki, web e investigación. Es privado porque también organiza estudios del notebook privado. La visibilidad de cada repositorio se mantiene independiente.

## De la idea al resultado

Idea → issue → Backlog → To do → In progress → Review → Done.

| Estado | Criterio |
|---|---|
| Backlog | Pregunta o mejora identificada; falta priorizar o delimitar. |
| To do | Resultado, alcance y aceptación claros; dependencias resueltas. |
| In progress | Hay trabajo activo. Registrar Start date al empezar. |
| Review | Existe un resultado revisable con evidencia, límites y PR cuando corresponde. |
| Done | Jairzinho revisó y aceptó el resultado, integró el PR cuando corresponde y movió manualmente la tarjeta. Solo él registra Completed date y decide el cierre de la issue. |

**El agente llega como máximo a Review.** Prepara el PR y sus comprobaciones; no lo fusiona, no habilita auto-merge, no cierra issues como completadas ni asigna Completed date. La revisión, integración y transición manual a Done corresponden a Jairzinho.

Una revisión puede devolver trabajo a In progress. Una tarea bloqueada conserva su estado y registra causa, dependencia y siguiente acción en la issue. No abrir otra tarjeta para representar el mismo trabajo. WIP inicial: una tarea técnica y un estudio editorial.

El Project es la fuente del estado; la issue es la fuente de alcance y aceptación; el PR contiene cambios y validación. No duplicar el backlog en Markdown. Vincular los PRs a su issue y mover la tarjeta al iniciar y al presentar resultados. Una idea descartada se presenta a Jairzinho para que decida su cierre; descartarla no equivale a validar su hipótesis.

## Issue o PRD

Una corrección, lectura acotada o prueba puede usar solo una issue: problema, resultado esperado, límites y criterio de aceptación. Usar el [PRD breve](../templates/prd.md) para cambios con alternativas, dependencias entre repositorios o diseño que necesite acuerdo. Guardarlo como docs/designs/<topic>.md y enlazarlo desde la issue; no copiarlo entero al tablero.

El PRD evoluciona en Git. Registrar decisiones y cambios de alcance; evitar versiones finales paralelas. La idea puede madurar en una conversación, pero al iniciar ejecución su alcance debe quedar en archivos o en una issue.

## Vistas y fechas

- Kanban: flujo completo por Status.
- Backlog: selección y prioridad de Backlog y To do.
- Timeline: Start date y Target date; muestra previsiones solo cuando se han acordado.
- Review: resultados pendientes de revisión.
- Completed: trabajo terminado y fecha real de cierre.

Priority usa P0 para bloqueo urgente, P1 para el siguiente resultado importante y P2 para trabajo posterior. Area distingue Knowledge, Website, Research y Operations. Los campos del sistema conservan repositorio, responsables y PRs vinculados.

Start date y Completed date son hechos. Target date es una previsión revisable, no la fecha de creación ni una promesa automática. Las tareas sin previsión permanecen sin Target date. Issues, PRs y sus eventos conservan el historial; el timeline muestra la planificación actual, no reconstruye por sí solo cada cambio de estado. Para medir tiempos de ciclo más adelante se evaluará un registro de transiciones, sin inventar métricas históricas.

## Revisión e integración

Rama corta → PR → checks → Review → revisión e integración por Jairzinho → Done manual. En wiki y notebook la base es main. En la web se conserva development para integración hasta acordar la promoción a main; un PR a una rama no predeterminada referencia la issue y su cierre se verifica explícitamente.

Un merge técnico no acepta automáticamente el tono, una conclusión de investigación ni la publicación del sitio. Las tareas amplias con validación posterior permanecen abiertas. Los PRs usan Refs para enlazar la issue sin provocar su cierre automático. No usar Closes, Fixes o Resolves para automatizar el cierre.

Revisar prioridades al retomar una sesión y registrar el siguiente paso al terminar. Las automatizaciones Auto-close issue, Item closed y Pull request merged están desactivadas. Ningún evento de PR, cierre de issue o check debe mover tarjetas a Done ni sustituir la revisión manual. Se mantienen la entrada en Backlog y los vínculos de trabajo; no autorizan estudios o despliegues. No se ha programado investigación recurrente.

Referencia: [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects).
