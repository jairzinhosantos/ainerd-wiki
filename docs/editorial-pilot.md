# Piloto editorial

Estado: primera iteración sustantiva preparada para revisión; aceptación editorial pendiente.

## Muestra

Trabajaremos sobre harness, ensamblaje de contexto y un perfil de Pi. Una secuencia de diagramas conecta sistema, mecanismo e implementación: relaciones, flujos, secuencias, estados y arquitectura. Cada figura responde una pregunta y explicita su evidencia. Una prueba pequeña se añade si sirve para observar el mecanismo. Las tres páginas desarrollan el recorrido con fuentes primarias y una lectura estática de Pi en un commit fijo. No se han ejecutado Pi ni experimentos con modelos.

## Qué decidiremos juntos

| Dimensión | Pregunta de revisión | Estado |
|---|---|---|
| Prosa | ¿Suena a la voz que quiere Jairzinho y articula las ideas? | open |
| Profundidad | ¿Explica lo necesario sin convertirse en un curso introductorio? | open |
| Organización | ¿Se puede pasar del sistema al detalle y regresar? | open |
| Diagramas | ¿Explican mecanismos y relaciones con claridad? | open |
| Visuales | ¿Funcionan lectura parcial, móvil y exportaciones? | open |
| Evidencia | ¿Se distingue definición, implementación y comprobación? | open |

## Iteración

Proponer variantes acotadas sobre un mismo fragmento. Registrar en el PR la variante, feedback y decisión. Git conserva las anteriores. No llenar el resto del mapa ni congelar templates hasta que esta muestra permita acordar una guía.

El piloto termina cuando Jairzinho acepta la muestra y podemos actualizar una observación sin duplicar cambios en artículos y gráficos. No implica haber estudiado todo el harness.

## Comprobaciones de esta iteración

2026-10-05: los 18 bloques se renderizaron con Mermaid 11.17.0 (9 en harness, 5 en contexto y 4 en Pi), sin errores. La preview local permite zoom y desplazamiento para figuras amplias; se comprobó que a 390 px no desborde la página. El Markdown sigue siendo la fuente; la preview no es el diseño final de la web ni implica publicación. La apariencia del renderer de GitHub puede diferir.

Los validadores de la wiki comprueban metadatos, relaciones, enlaces y catálogo. Las citas de Pi apuntan al commit examinado; otras fuentes documentales registran su consulta en el estudio. La sintaxis y el renderizado no sustituyen revisar semántica, claridad ni afirmaciones.
