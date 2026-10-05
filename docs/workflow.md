# Flujo de estudio y publicación

## Dos entradas al mismo trabajo

Una conversación previa se entrega como texto o archivo y se clasifica en un expediente de estudio privado. Una investigación directa comienza leyendo esta wiki y abriendo o retomando ese expediente. Ambos caminos continúan con fuentes primarias, análisis, comprobaciones y borradores.

El notebook privado conserva pregunta, alcance, revisión base de la wiki, fuentes, análisis, revisión y siguiente paso. Un chat sirve de entrada; no sustituye el estudio ni se copia automáticamente a este repositorio público.

El [modelo de gestión](project-management.md) conecta ideas, issues, PRDs breves, Kanban y PRs. El estado se mantiene en GitHub Projects.

## Elaboración

1. Identificar qué existe y la pregunta que falta resolver.
2. Contrastar fuentes y versiones; separar afirmación atribuida, síntesis propia, hipótesis y resultado ejecutado.
3. Preparar la explicación y el diagrama. Añadir pruebas solo cuando la conclusión las necesite.
4. Iterar con Jairzinho la prosa, profundidad y visuales, conforme al piloto editorial.
5. Preparar un cambio sobre la revisión actual de la wiki; comparar contra la revisión base para no sobrescribir trabajo posterior.

Para tareas amplias, una issue reúne alcance y aceptación. Un planner actualiza esa misma tarea; no crea un segundo backlog. WIP orientativo: un estudio principal y su prueba asociada. Una revisión puede cerrar sin publicar si no hay cambio útil.

## Integración y publicación

El contenido destinado al repositorio público debe ser apto para ese destino incluso si tiene status: draft. Los drafts en GitHub no son privados. Fuentes, explicación y resultados publicados deben poder entenderse sin acceso al cuaderno privado.

Usar rama corta → PR → validación → revisión dentro de la autorización de la tarea → integración. El bootstrap de estructura no convierte los artículos en published. Cambiar a published requiere revisión técnica y aceptación editorial identificables en el PR.

Tras integrar, la wiki es la fuente mantenida. El estudio privado conserva el commit y PR resultantes; sus borradores pasan a antecedente, no a copia activa. La web se publica por un paso separado y verificable.

## Continuidad

Al cerrar una sesión registrar qué cambió, dudas, fuentes pendientes y próximo paso en el expediente. Otra herramienta continúa leyendo esos archivos. Una corrección pública pequeña puede hacerse directamente en una rama sin abrir un estudio completo.

La automatización se evaluará según docs/research-automation-plan.md. No hay scheduler ni servicio de investigación activado.
