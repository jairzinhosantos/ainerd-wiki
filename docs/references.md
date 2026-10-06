# Referencias

Toda explicación conceptual, perfil tecnológico, comparación y diagrama técnico debe permitir rastrear sus afirmaciones. Esta política se aplica también a los borradores públicos; la falta de revisión se indica en sus metadatos.

- **Citar junto a la afirmación.** Una lista de enlaces al final no sustituye identificar qué fuente respalda una definición, capacidad o resultado. Añadir una lista final breve para profundizar.
- **Preferir fuentes primarias.** Documentación oficial, artículos de sus autores, papers originales y código. Leer el contenido antes de citarlo; un resultado de búsqueda o una conversación no constituyen evidencia suficiente.
- **Distinguir fuente y síntesis.** Atribuir las definiciones de un proveedor. Marcar como propuesta o síntesis propia una organización que construimos nosotros; no presentarla como estándar universal ni como cita de otra organización.
- **Identificar el tiempo y alcance.** Registrar fecha de consulta en el estudio o artículo. Fijar versión o commit al describir una implementación. No convertir una inspección estática en una afirmación de rendimiento o fiabilidad.
- **Referenciar los gráficos.** El pie identifica si el diagrama es una síntesis, una adaptación o una lectura de código y enlaza las fuentes que sustentan sus relaciones. Los datos cuantitativos requieren método y origen. Conservar fuente editable y exportación.
- **Enlazar conceptos mantenidos.** Usar la página existente para profundizar, evitando repetir definiciones completas. Los enlaces internos conectan la lectura; las fuentes externas sostienen las afirmaciones.

Si una afirmación aún no está verificada, se formula como pregunta o hipótesis explícita, o se retira de la explicación factual. La revisión comprueba correspondencia entre afirmación y fuente; la mera presencia de URLs no valida el contenido.

En artículos ordinarios, `sources` puede conservar las URLs de referencia. En comparativas con evidencia estructurada, usar `evidence: observations.json` y omitir `sources` de la cabecera. El mismo JSON contiene `sources` (fichas bibliográficas únicas) y `observations` (afirmaciones con citas por ID y localizador). No añadir un `sources.yml` paralelo. La lista final de referencias se genera con `python scripts/references.py benchmarks/<study>`; las citas próximas a las afirmaciones siguen siendo responsabilidad editorial. Los enlaces visibles y los pies de figura permiten entenderlas sin consultar el notebook privado. Los chats y capturas entregados para orientar el tono no se publican automáticamente como fuentes técnicas.
