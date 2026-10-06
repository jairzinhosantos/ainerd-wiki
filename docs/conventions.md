# Convenciones

## Idioma y nombres

Rutas en inglés, ASCII y kebab-case; scripts Python en snake_case. Conservar README.md, AGENTS.md, CLAUDE.md y nombres convencionales de herramientas. No usar agents.md como artículo: puede resolver como AGENTS.md en sistemas de archivos que no distinguen mayúsculas.

Títulos, resúmenes, prosa y encabezados de lectura en español. Claves de metadatos e identificadores de control en inglés. Fechas ISO YYYY-MM-DD, escritas entre comillas en YAML. Las fechas de revisión técnica se asignan al revisar evidencia; consultar novedades no equivale a revisar una página.

## Páginas

Una página publicable usa frontmatter con id, title, summary, type, status, language, updated, reviewed. Tipos: concept, technology, architecture, comparison, benchmark, lab. Estados: draft, published. language es es. reviewed puede ser null en un borrador; una página published necesita fecha de revisión y al menos una fuente pública.

El cuerpo tiene un único H1 que coincide con title. El renderer futuro debe evitar duplicarlo. El contrato antiguo de chapters no se modifica todavía.

id es globalmente único, legible y estable, independiente de la ruta. parent es una relación de lectura opcional y acíclica. related y requires son listas de IDs existentes. Una página publicada solo enlaza por esas relaciones a páginas publicadas. Los índices de navegación README sin frontmatter no se incluyen como artículos en el catálogo.

sources es una lista de URLs públicas para artículos ordinarios. Una comparación puede usar evidence: observations.json en su lugar; ambos campos son excluyentes. El JSON schema_version 2 contiene sources y observations; cada observación enlaza citas por ID. Las referencias completas se presentan al final del README mediante un bloque generado, nunca como una lista extensa en la cabecera. Citas y localizadores se explican junto a las afirmaciones. Esta lista no demuestra veracidad. Una página de tecnología publicada identifica examined_ref, con versión o commit. Una comparación conserva entradas y método conforme a benchmarks/README.md.

## Relaciones y datos

El catálogo inicial genera parent, related y requires. No deduce pertenencia arquitectónica desde los enlaces Markdown. Las afirmaciones implements solo se añadirán cuando existan observaciones con componente, versión, fuente, base de evidencia y alcance; hasta entonces no se inventa una matriz de capacidades.

Fuentes Markdown y metadatos se mantienen una vez. nodes.csv y edges.csv son derivados deterministas. Su schema_version es 1. Su estado permite excluir borradores en consumidores; la adaptación web deberá filtrar páginas y relaciones.

## Versiones

Git conserva cambios de texto y código: no crear artículos v1, v2 o final. Producto examinado, método y ejecución son identidades distintas. Una ejecución citada tiene manifiesto y resultados conservados; un benchmark no cambia silenciosamente al actualizar el perfil de una tecnología. Corregir evidencia registra qué reemplaza.

La marca no forma parte del ID. Los slugs históricos se revisan en docs/migration.md antes de cambiar sus destinos.
