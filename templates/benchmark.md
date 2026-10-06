# Plantilla provisional de benchmark

Usar como apoyo durante el piloto; ajustar a la pregunta, sin rellenar secciones mecánicamente. Sustituir los ejemplos y usar un ID real único.

```yaml
id: example-benchmark
title: "Pregunta de comparación"
summary: "Pregunta y alcance en una frase."
type: benchmark
status: draft
language: es
updated: "YYYY-MM-DD"
reviewed: null
sources: []
```

## Desarrollo sugerido

Pregunta y contexto; explicación o método; límites y perspectivas; evidencia y fuentes; siguiente paso. Un perfil tecnológico identifica examined_ref al publicarse. Una comparación o benchmark conserva observations.json y manifest.json con los hashes de sus entradas.

No declarar published o reviewed por generar el texto. La aceptación editorial se registra en la revisión.

Para un barrido documental usar type: comparison y el contrato de [comparativas](../benchmarks/README.md). Al incorporar observations.json schema_version 2, sustituir sources por evidence: observations.json y añadir al final un bloque references:start / references:end para la bibliografía generada. No trasladar una definición propuesta al estudio: se trabaja en concepts/.
