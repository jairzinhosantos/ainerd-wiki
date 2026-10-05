# Transición desde los capítulos actuales

La web consume main/chapters/*.md con status available o coming-soon. Esta primera entrega conserva esos seis archivos sin cambios para evitar introducir un fallo del build. Son compatibilidad temporal, no una segunda colección editorial. Todos están actualmente en coming-soon en esta copia del repositorio.

## Inventario de rutas anteriores

| Slug anterior | Tratamiento al migrar |
|---|---|
| generative-ai | Revisar su relación con concepts/models; no publicar automáticamente el texto anterior |
| rag | Reescribir al desarrollar retrieval-and-rag y decidir redirección |
| mcp | Reescribir desde herramientas e integraciones; destino por acordar |
| agents | Reescribir como agent-concepts; evitar el nombre reservado |
| agentic-ai | Revisar desde systems y decidir destino |
| multi-agents | Revisar desde coordinación y arquitecturas |

Estuvieron marcados available algunos capítulos en el historial; no inferir que las URLs nunca circularon. Antes de retirar chapters se documentarán destinos o retiradas explícitas.

## Trabajo pendiente en el sitio

Cargar recursivamente los nuevos tipos; respetar IDs y estados; resolver Markdown y assets; evitar H1 duplicados; actualizar modelos y navegación; generar el grafo desde relaciones tipadas. El render público excluye borradores, también en índices y relaciones.

El build debe fallar si no puede obtener la fuente requerida, sin aparentar una publicación nueva con contenido anterior. Su resultado identificará la revisión de contenido y del sitio. Probar preview y despliegue antes de retirar la compatibilidad. Los scripts actuales de esta wiki no despliegan el sitio.
