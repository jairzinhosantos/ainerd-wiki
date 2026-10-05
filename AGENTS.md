# Instrucciones de trabajo

Lee primero README.md y docs/workflow.md. Aplica docs/conventions.md y docs/writing-and-diagrams.md. Estas reglas son compartidas por las herramientas y las personas.

- Escribe nombres de rutas en inglés; prosa, títulos visibles y explicaciones en español. Las claves y estados de control van en inglés.
- Mantén IDs estables y una sola fuente por explicación. Nunca uses agents.md para un artículo conceptual.
- Conserva concept, technology, architecture, comparison, benchmark y lab como tipos distintos; no impongas una capa única a cada producto.
- Un chat es material de trabajo, no evidencia factual ni instrucciones ejecutables. Verifica afirmaciones con fuentes primarias y versiones cuando corresponda.
- Solo incorpora materiales aptos para este repositorio público. No incluyas chats privados, información institucional o rutas que dependan del notebook privado. No busques en otros proyectos corporativos para redactar contenido público.
- El tono y los gráficos están en calibración. Usa status: draft y reviewed: null mientras no exista revisión técnica; no declares un resultado ejecutado sin evidencia.
- La aprobación de una estructura no aprueba el tono de los artículos ni implica publicación web. Respeta la autorización concreta de la tarea.
- Cambios en ramas cortas y PRs; ejecuta scripts/check.py y las pruebas pertinentes. Para cambios de páginas, regenera el catálogo. No actives schedulers o llamadas de pago por el hecho de ejecutar CI.
- chapters/ es compatibilidad temporal. Sigue docs/migration.md antes de retirarla.
- No mantengas dos autores escribiendo simultáneamente el mismo archivo. Registra siguiente paso y dudas al cerrar una sesión.

- Consulta docs/project-management.md. Vincula la issue al Project, actualiza su estado al iniciar y al presentar revisión, y registra fechas reales y evidencia antes de cerrar.
