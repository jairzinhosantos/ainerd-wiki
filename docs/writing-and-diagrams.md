# Escritura y diagramas

Guía provisional. La voz y el lenguaje visual se encontrarán trabajando las mismas piezas con Jairzinho; no se consideran fijados por este bootstrap.

Aplica la [política de referencias](references.md) a la prosa, tablas y gráficos.

Una página empieza por una definición o explicación directa. El título nombra el tema: «Harness», «Ensamblaje de contexto», «Pi». Los encabezados identifican el contenido de la sección, sin subtítulos promocionales, metáforas ni preguntas retóricas. Desarrolla mecanismo, fronteras y fuentes en prosa conectada. Su portada explica el conjunto; las páginas hijas profundizan cuando hay contenido suficiente. Evitar una entrada de glosario por cada término.

La concisión corresponde a títulos y orientación; las explicaciones necesitan profundidad. Describir qué ocurre, con qué información, qué componente decide, qué estado cambia y qué sucede ante un fallo. Usar ejemplos continuos para explicar dependencias y consecuencias. Una enumeración de capacidades no sustituye ese desarrollo. Reducir frases que anuncian el recorrido o repiten cómo leer el artículo. Conservar las atribuciones y los límites concretos de evidencia, sin repetir una advertencia general después de cada párrafo.

La lectura debe abrir el sistema por componentes: mapa general, distinciones, mecanismo, ejemplo que evoluciona y, cuando ayude, pseudocódigo. El diagrama introduce o resuelve una relación que la prosa desarrolla. Alternar párrafos, tablas de responsabilidades y secuencias; evitar tanto bloques de prosa homogéneos como frases aisladas sin desarrollo. Las preguntas concretas son útiles cuando expresan una duda técnica real; la restricción anterior se refiere a preguntas retóricas y títulos adornados. Explicar primero cómo funciona el mecanismo y después sus límites. Separar la muestra editorial de las implementaciones y afirmaciones de producto que requieren verificación.

Dirección visual de la muestra vigente: definición de una o dos frases, mapa ordenado y profundidad mediante enlaces. Un mapa de componentes usa cajas alineadas y conectores de relación; un flujo usa dirección y pasos. No mezclar ambas vistas. Para composiciones centrales o comparativas, preferir SVG con geometría explícita cuando Mermaid no conserve la jerarquía. No añadir flechas entre todas las cajas ni atribuir causalidad a una conexión visual. Cada caja lleva un nombre y una función breve. La prosa amplía únicamente la relación que necesita explicación; el resto se desarrolla al abrir el concepto. El sistema visual sigue pendiente de aceptación.

Usar Mermaid para diagramas sencillos. Draw.io y SVG cuando se necesite control visual; conservar fuente y exportación juntas. Comparativas estáticas e interactivas usarán datos identificados. Los resultados ficticios se rotulan como ejemplos y nunca como mediciones.

No fijar colores de marca, densidad ni plantilla definitiva antes del piloto. Evaluar lectura parcial, tamaño de texto, móvil, accesibilidad, leyendas y la relación entre figura y argumento. El texto debe poder leerse también en GitHub.

Se permite publicar una pregunta abierta o hipótesis explicitada. Se bloquean afirmaciones presentadas como hechos cuando siguen sin verificar; un checker no sustituye esa revisión humana.

## Recorrido visual progresivo

Cada lectura desarrolla una secuencia de explicaciones y diagramas; no se limita a una figura ni aplica una cuota fija. Empezar con relaciones o ideas, abrir un flujo, mostrar interacciones en el tiempo y llegar a una arquitectura cuando la pregunta lo requiera. Mantener un ejemplo que conecte las vistas.

Cada figura tiene una pregunta, un pie que explica cómo leerla y un nivel de evidencia: síntesis conceptual, arquitectura propuesta o flujo derivado de código con revisión. Explicar las flechas y distinguir datos, control, dependencia y cronología. Una caja no implica un servicio ni una capa universal. La prosa prepara la figura y desarrolla lo que permite concluir.

Mermaid admite también secuencias, estados y arquitecturas moderadas. Si el layout dificulta la lectura, dividir la vista por responsabilidad; para composición de mayor precisión usar Draw.io con fuente y exportación. No añadir nodos para aparentar profundidad. Validar sintaxis y renderizado, revisar etiquetas y legibilidad. En móvil, las vistas densas deben poder ampliarse o desplazarse sin reducir el texto hasta volverlo ilegible.

El primer recorrido conecta harness, ensamblaje de contexto y Pi. Los borradores y esta guía continúan sujetos a la revisión de Jairzinho; el número de figuras no constituye aceptación editorial.
