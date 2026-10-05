# Catálogo generado

`nodes.csv` registra páginas con metadatos. `edges.csv` registra relaciones de lectura declaradas por esas páginas. Ambos tienen schema_version 1, orden estable y codificación UTF-8.

Regenerar con `python scripts/catalog.py`. Verificar con `python scripts/check.py` o `python scripts/catalog.py --check`. El catálogo incluye borradores con su estado; el consumidor público debe seleccionar status published y solo relaciones cuyos extremos estén publicados.

La primera versión no infiere capacidades de productos ni las extrae de la prosa. Las matrices se incorporarán junto con observaciones verificadas y un contrato explícito. La web actual todavía utiliza el grafo anterior.
