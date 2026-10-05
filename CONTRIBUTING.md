# Contribuir a la wiki

Empieza por una pregunta acotada y revisa lo existente. Un cambio pequeño puede ir directamente a una rama y PR; un estudio amplio necesita registrar alcance, fuentes, límites y resultado esperado.

Sigue el [flujo de trabajo](docs/workflow.md), las [convenciones](docs/conventions.md) y la [guía editorial provisional](docs/writing-and-diagrams.md). Las fuentes citadas deben ser accesibles al lector público; una afirmación de producto identifica el componente y revisión examinados.

Antes del PR, ejecuta `python scripts/catalog.py`, `python scripts/check.py` y las pruebas pertinentes. Explica qué cambia, por qué y qué está verificado. El estado draft es público en GitHub y se excluye de la futura publicación web.

El piloto editorial admite cambios de voz y de diagramas. Propón alternativas sobre la misma pieza y registra la elección; no multipliques archivos final-v2-v3. No se exige un experimento para una explicación documental ni una issue para una errata.
