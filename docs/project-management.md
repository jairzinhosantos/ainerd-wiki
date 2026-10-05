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
| Done | Criterios cumplidos, evidencia enlazada e integración completada cuando corresponde. Registrar Completed date y cerrar la issue. |

Una revisión puede devolver trabajo a In progress. Una tarea bloqueada conserva su estado y registra causa, dependencia y siguiente acción en la issue. No abrir otra tarjeta para representar el mismo trabajo. WIP inicial: una tarea técnica y un estudio editorial.

El Project es la fuente del estado; la issue es la fuente de alcance y aceptación; el PR contiene cambios y validación. No duplicar el backlog en Markdown. Vincular los PRs a su issue y mover la tarjeta al iniciar y al presentar resultados. Cerrar como no planificada una idea descartada no equivale a validar su hipótesis.

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

Rama corta → PR → checks → revisión → integración. En wiki y notebook la base es main. En la web se conserva development para integración hasta acordar la promoción a main; un PR a una rama no predeterminada referencia la issue y su cierre se verifica explícitamente.

Un merge técnico no acepta automáticamente el tono, una conclusión de investigación ni la publicación del sitio. Las tareas amplias con validación posterior permanecen abiertas. Los PRs parciales usan Refs; Closes solo cuando el cambio satisface toda la aceptación y su integración debe cerrar la issue.

Revisar prioridades al retomar una sesión y registrar el siguiente paso al terminar. Las automatizaciones nativas del tablero pueden acompañar eventos de issues y PRs; no sustituyen comprobar aceptación ni autorizan estudios o despliegues. No se ha programado investigación recurrente.

Referencia: [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects).
