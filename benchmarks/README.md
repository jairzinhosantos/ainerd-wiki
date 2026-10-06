# Comparativas y mediciones

[Definiciones y alcance de harness](2026-10-harness-definitions/README.md): barrido documental de 39 proyectos, servicios gestionados, libros y artículos. No hay benchmarks ejecutados.

`benchmarks/` reúne estudios comparativos y mediciones. Una comparación documental usa `type: comparison`; un benchmark ejecutado usa `type: benchmark`. El tipo distingue el método sin abrir otra área del repositorio.

Cada comparación vive en `YYYY-MM-description/` con:

- `README.md`: alcance y método, análisis, diagramas, coincidencias y diferencias, referencias.
- `observations.json`: fuentes bibliográficas y observaciones en un único archivo.
- `manifest.json`: corte y hashes generados; no se edita a mano.
- `figures/`: solo cuando hacen falta figuras externas, con editable Draw.io, SVG y PNG para consumidores que lo requieran.

Los esquemas simples viven en Mermaid dentro del README. La definición que adopte la wiki pertenece a `concepts/` y referencia la comparación y el commit que la sustentan. El estudio puede concluir con desacuerdos o preguntas pendientes; no necesita proponer una definición única.

## Evidencia

Usar `evidence: observations.json` en la cabecera. El JSON `schema_version: 2` tiene dos listas: `sources` y `observations`. Cada fuente tiene `id`, `title`, `kind`, `url` y `accessed`; según corresponda, `authors`, `organization`, `published`, `edition`, `version` o `isbn`. Cada observación tiene `id`, `subject`, `claim`, `scope`, `basis`, `observed` y `citations`, una lista de objetos con `source` y un `locator` cuando sea útil. `basis` distingue docs, code y run. `interpretation` separa nuestra lectura de la afirmación atribuida.

No exigir `technology` o un commit a un libro. Desconocido no significa ausencia; la fecha de consulta no es fecha de aparición. Un preprint no constituye consenso y un README no prueba rendimiento.

```sh
python scripts/references.py benchmarks/2026-10-harness-definitions
python scripts/catalog.py
python scripts/check.py
```

El generador actualiza únicamente el bloque final de referencias y el manifiesto. CI comprueba también los borradores con evidencia: citas resolubles, fuentes utilizadas, bibliografía sincronizada y hashes. Se conserva compatibilidad de lectura para comparativas anteriores con observaciones planas y `sources` en la cabecera.

## Continuidad

Pregunta → evidencia → comparación visual → Review → revisión de Jairzinho. Una definición conceptual se elabora después de revisar el estudio. Las nuevas observaciones conservan su fecha; una corrección señala qué reemplaza. Git conserva las iteraciones: no crear copias v2/final ni regenerar silenciosamente entradas desde perfiles tecnológicos más recientes.

El notebook privado recibe chats y material de trabajo que no puede publicarse. Una vez que una observación forma parte del estudio público, no se mantiene otra ficha bibliográfica activa en el notebook. Solo se enlaza el estudio y su revisión.
