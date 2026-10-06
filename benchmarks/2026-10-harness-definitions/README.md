---
id: harness-definitions-comparison
title: "Definiciones y alcance de harness"
summary: "Comparación documental de perspectivas sobre harness y 27 proyectos: vocabulario, fronteras y propuesta de síntesis."
type: comparison
status: draft
language: es
updated: "2026-10-05"
reviewed: null
related: [harness, context-assembly, pi]
sources:
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/research/trustworthy-agents
  - https://developers.openai.com/api/docs/guides/agents/sandboxes
  - https://developers.openai.com/blog/codex-as-a-platform
  - https://www.langchain.com/blog/the-anatomy-of-an-agent-harness
  - https://docs.langchain.com/oss/python/concepts/products
  - https://code.claude.com/docs/en/agent-sdk/overview
  - https://pydantic.dev/docs/ai/harness/
  - https://strandsagents.com/docs/user-guide/harness/
  - https://github.com/openai/codex/blob/5ad689169645a953ec7380762c4ae596712057ee/README.md
  - https://github.com/anthropics/claude-agent-sdk-python/blob/7bb2753754c9725bccc972a5530ae8d572921658/README.md
  - https://github.com/earendil-works/pi/blob/28dcce2ba45ce4a9efeb0f5b686f0be830fd89b9/README.md
  - https://github.com/langchain-ai/deepagents/blob/3086f7b918b53b12a6ad675231ebd4752d4a420a/README.md
  - https://github.com/strands-agents/harness-sdk/blob/d6faa6ece53c38ac0f05b19713cdd14112c21150/README.md
  - https://github.com/pydantic/pydantic-ai/blob/62013d9fa54e441e03a792ba8c26c20b56d55291/README.md
  - https://github.com/bytedance/deer-flow/blob/d8bdd7552c6ecb49f82519d35c07f161be7d6c0f/README.md
  - https://github.com/letta-ai/letta-code/blob/4b028fab07c69edaac2ddb4f7b9a43573ff20d81/README.md
  - https://github.com/anomalyco/opencode/blob/772392050500e0ddcd2ad2193411a22a3824372f/README.md
  - https://github.com/google-gemini/gemini-cli/blob/fb972b2f87fe7d5b06d37eac711490162d98de2c/README.md
  - https://github.com/aaif-goose/goose/blob/104ddde585112af6f074f912f3ceb405fb5b800e/README.md
  - https://github.com/cline/cline/blob/c00bf86595d2fee6665fa3b27091d95e57578013/README.md
  - https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md
  - https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md
  - https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/README.md
  - https://github.com/NousResearch/hermes-agent/blob/7b2ff7a7d4e84a1018eecb27e606a485f65435f1/README.md
  - https://github.com/openai/openai-agents-python/blob/d7e52c375021248973f60ccbea8e7b69bc5b16e3/README.md
  - https://github.com/langchain-ai/langchain/blob/7ca02f333aa6d5e4cf566a2dcc444d06758e2958/README.md
  - https://github.com/langchain-ai/langgraph/blob/2d942085e214ef6b99b6f54ed4d544a7c7c5ac56/README.md
  - https://github.com/OpenHands/software-agent-sdk/blob/cb7eabaf7b784a2f58f9df35d610f106287e823b/README.md
  - https://github.com/huggingface/smolagents/blob/c30b115286e000e98711fae5e85993547b73d826/README.md
  - https://github.com/google/adk-python/blob/71d5ed77382865c419a57692d68c296866efe2e5/README.md
  - https://github.com/microsoft/agent-framework/blob/b9d24c8fb484c8330abe8bb9e7500ca3c3bbf46c/README.md
  - https://github.com/mastra-ai/mastra/blob/a793ec23949ee59b4aa850d83f9e1eba365ac5c8/README.md
  - https://github.com/agno-agi/agno/blob/c44b082010d925d083b945798deb82ae8fb9429e/README.md
  - https://github.com/crewAIInc/crewAI/blob/1133f16cab274b9863b36fdacca7766b30e549fd/README.md
  - https://github.com/EleutherAI/lm-evaluation-harness/blob/d6de81643928d653435c431bae19945d41d32520/README.md
---

# Definiciones y alcance de harness

La documentación examinada comparte un objeto —el software que organiza el trabajo alrededor de un modelo—, pero utiliza *harness* con alcances distintos. Algunas fuentes describen el bucle de control; otras incluyen configuración, herramientas e infraestructura; otras presentan un producto ya ensamblado. La comparación conserva esas diferencias antes de proponer una definición para la wiki.

**Corte documental: 2026-10-05.** Se revisaron 27 proyectos y 11 textos de documentación y definición. Los proyectos incluyen harnesses explícitos, aplicaciones agénticas, componentes de construcción y un harness de evaluación como contraste terminológico. Es una selección amplia e intencional; no un censo de todos los proyectos abiertos. Se examinaron pasajes de presentación, categorías y responsabilidades; no se ejecutó el software ni se auditó su implementación.

## Cómo lo define cada fuente

Las siguientes formulaciones son paráfrasis en español. Se distingue entre **definición conceptual**, **frontera arquitectónica** y **autodescripción de producto**. Una autodescripción muestra qué quiere ofrecer el proyecto; no establece por sí sola una definición universal.

| Fuente y tipo de pasaje | Formulación de la fuente | Diferencia que conviene conservar |
|---|---|---|
| [Anthropic: evaluaciones](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) · definición | Sistema que permite actuar al modelo: procesa entradas, orquesta llamadas a herramientas y devuelve resultados. | Separa expresamente agent harness y evaluation harness. |
| [Anthropic: Managed Agents](https://www.anthropic.com/engineering/managed-agents) · arquitectura | Bucle que llama a Claude y dirige sus solicitudes de herramientas a la infraestructura correspondiente. | La sesión y el sandbox son componentes separados. |
| [Anthropic: tareas prolongadas](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · diseño | El SDK es un harness general; para continuar entre sesiones se agregan preparación del entorno y artefactos que conservan el progreso. | La continuidad requiere diseño del trabajo; compactar contexto no resuelve por sí solo todo el problema. |
| [Anthropic: gobernanza](https://www.anthropic.com/research/trustworthy-agents) · descripción de componentes | Instrucciones y guardrails bajo los que opera el modelo. | En este texto, herramientas y entorno quedan fuera de esa etiqueta. |
| [OpenAI: sandbox agents](https://developers.openai.com/api/docs/guides/agents/sandboxes) · arquitectura | Plano de control: bucle, llamadas al modelo, enrutamiento de herramientas, aprobaciones y estado. | El cómputo que ejecuta acciones se distingue del control. |
| [OpenAI: Codex](https://developers.openai.com/blog/codex-as-a-platform) · descripción de sistema | Sistema de ejecución que mantiene contexto, utiliza herramientas y conduce el trabajo alrededor del modelo. | El mismo harness puede servir a distintas interfaces y aplicaciones. |
| [LangChain: anatomía](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) · definición | Código, configuración y lógica de ejecución externos al modelo. | Alcance amplio: incluye prompts, herramientas, infraestructura y orquestación. |
| [LangChain: categorías](https://docs.langchain.com/oss/python/concepts/products) · clasificación de productos | Harness como framework con decisiones y capacidades ya incorporadas. | Lo diferencia de las abstracciones del framework y de la infraestructura del runtime. |
| [Pydantic AI Harness](https://pydantic.dev/docs/ai/harness/) · composición | El agente básico ya tiene un harness ligero; capacidades adicionales componen harnesses para tareas más complejas. | No hay una frontera absoluta entre framework y harness. |
| [Strands harness](https://strandsagents.com/docs/user-guide/harness/) · producto | Agente ensamblado con configuración predeterminada de herramientas, contexto, sesiones, memoria y hooks. | La configuración ensamblada se distingue del SDK para construirla. |
| [Pi](https://github.com/earendil-works/pi/blob/28dcce2ba45ce4a9efeb0f5b686f0be830fd89b9/README.md) · producto | Harness mínimo y extensible. Extensiones, skills y plantillas; evita imponer subagentes y modo de planificación en el núcleo. | Un harness no necesita incluir todas las capacidades avanzadas. |
| [Deep Agents](https://github.com/langchain-ai/deepagents/blob/3086f7b918b53b12a6ad675231ebd4752d4a420a/README.md) · producto | Harness con capacidades y decisiones predeterminadas. Sistema de archivos, subagentes, contexto y skills sobre LangChain y LangGraph. | Distinguir paquete ensamblado de los componentes sobre los que se construye. |
| [DeerFlow](https://github.com/bytedance/deer-flow/blob/d8bdd7552c6ecb49f82519d35c07f161be7d6c0f/README.md) · producto | Super agent harness, denominación del proyecto. Orquestación de subagentes, memoria, sandboxes y skills. | Ejemplo de alcance amplio y configuración integrada. |
| [Letta Code](https://github.com/letta-ai/letta-code/blob/4b028fab07c69edaac2ddb4f7b9a43573ff20d81/README.md) · producto | Harness agéntico con estado. Memoria, identidad y continuidad a lo largo de interacciones. | Estudiar la continuidad como eje de diseño; la mejora declarada requiere evaluación. |

La variación dentro de Anthropic es especialmente útil: el artículo de gobernanza reserva *harness* para instrucciones y controles, mientras que el de arquitectura lo usa para un bucle de ejecución. Son pasajes con objetivos y fronteras distintos. La wiki debe atribuir la perspectiva al documento concreto, evitando hablar de «la definición de Anthropic» como si fuese una sola.

## Proyectos examinados

Las columnas de énfasis resumen lo que declaran los documentos. La última columna contiene nuestra interpretación para el estudio. La ausencia de una capacidad en estas filas significa que no se examinó aquí, no que el proyecto carezca de ella. Cada nombre enlaza el README en un commit fijo; las referencias complementarias de las filas anteriores precisan los casos donde el README no define harness.

### Harnesses y composiciones explícitas

| Proyecto | Cómo se presenta | Énfasis declarado | Aporte a la comparación |
|---|---|---|---|
| [Codex](https://github.com/openai/codex/blob/5ad689169645a953ec7380762c4ae596712057ee/README.md) | Agente de código; el artículo de OpenAI denomina harness al sistema subyacente. | Bucle, contexto, herramientas y políticas de ejecución. | Distinguir interfaz de usuario y harness reutilizable. |
| [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python/blob/7bb2753754c9725bccc972a5530ae8d572921658/README.md) | SDK que expone el agente de Claude Code; Anthropic lo describe como harness de propósito general. | Bucle, herramientas y gestión de contexto integrados. | Distinguir biblioteca de integración, binario ejecutado y servicio alojado. |
| [Pi](https://github.com/earendil-works/pi/blob/28dcce2ba45ce4a9efeb0f5b686f0be830fd89b9/README.md) | Harness mínimo y extensible. | Extensiones, skills y plantillas; evita imponer subagentes y modo de planificación en el núcleo. | Un harness no necesita incluir todas las capacidades avanzadas. |
| [Deep Agents](https://github.com/langchain-ai/deepagents/blob/3086f7b918b53b12a6ad675231ebd4752d4a420a/README.md) | Harness con capacidades y decisiones predeterminadas. | Sistema de archivos, subagentes, contexto y skills sobre LangChain y LangGraph. | Distinguir paquete ensamblado de los componentes sobre los que se construye. |
| [Strands](https://github.com/strands-agents/harness-sdk/blob/d6faa6ece53c38ac0f05b19713cdd14112c21150/README.md) | Harness ensamblado y SDK para construir harnesses. | Valores predeterminados para herramientas, contexto, sesiones, memoria y hooks. | Separar la configuración lista para usar de las primitivas de construcción. |
| [Pydantic AI / Harness](https://github.com/pydantic/pydantic-ai/blob/62013d9fa54e441e03a792ba8c26c20b56d55291/README.md) | Framework y biblioteca de capacidades y harnesses componibles. | Bucle tipado en el núcleo; capacidades que componen agentes como Coder y Researcher. | La frontera del paquete no constituye una frontera conceptual universal. |
| [DeerFlow](https://github.com/bytedance/deer-flow/blob/d8bdd7552c6ecb49f82519d35c07f161be7d6c0f/README.md) | Super agent harness, denominación del proyecto. | Orquestación de subagentes, memoria, sandboxes y skills. | Ejemplo de alcance amplio y configuración integrada. |
| [Letta Code](https://github.com/letta-ai/letta-code/blob/4b028fab07c69edaac2ddb4f7b9a43573ff20d81/README.md) | Harness agéntico con estado. | Memoria, identidad y continuidad a lo largo de interacciones. | Estudiar la continuidad como eje de diseño; la mejora declarada requiere evaluación. |

### Aplicaciones y agentes

| Proyecto | Cómo se presenta | Énfasis declarado | Aporte a la comparación |
|---|---|---|---|
| [OpenCode](https://github.com/anomalyco/opencode/blob/772392050500e0ddcd2ad2193411a22a3824372f/README.md) | Agente de código abierto. | Agentes build y plan con reglas de acceso diferentes; subagente general. | Comparar configuraciones de control dentro de un mismo producto. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/fb972b2f87fe7d5b06d37eac711490162d98de2c/README.md) | Agente de IA para la terminal. | Operaciones de archivos, shell, búsqueda y extensiones MCP. | La interfaz terminal y las herramientas describen un producto, no una definición universal de harness. |
| [goose](https://github.com/aaif-goose/goose/blob/104ddde585112af6f074f912f3ceb405fb5b800e/README.md) | Agente de propósito general que se ejecuta en la máquina del usuario. | Interfaces de escritorio, CLI y API; extensiones MCP. | Separar el dominio de uso de la interfaz y del conjunto de integraciones. |
| [Cline](https://github.com/cline/cline/blob/c00bf86595d2fee6665fa3b27091d95e57578013/README.md) | Agente de código en IDE, terminal y escritorio. | Reglas del proyecto y skills para orientar el trabajo. | Examinar políticas y superficie de interacción como dimensiones separadas. |
| [Aider](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/README.md) | Programación en pareja con IA en la terminal. | Trabajo sobre código existente y mapa del repositorio. | El contexto del repositorio es una decisión concreta de ensamblaje. |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/README.md) | Agente que permite a un modelo usar herramientas para resolver tareas de software. | Interacción con repositorios y configuración para investigación. | Aporta un antecedente de diseño; su README recomienda mini-swe-agent para trabajo nuevo. |
| [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent/blob/04d809ceab9df28f9adaed044884180159172930/README.md) | Agente mínimo de ingeniería de software. | Bash, historial lineal y acciones ejecutadas de forma independiente. | Contraejemplo a exigir APIs nativas de tool calling o un shell persistente para definir un harness. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/7b2ff7a7d4e84a1018eecb27e606a485f65435f1/README.md) | Agente con aprendizaje continuo, según la presentación de sus autores. | Memoria, creación de skills y recuperación de conversaciones. | Separar mecanismos declarados de afirmaciones de mejora; no se verificó rendimiento. |

### Frameworks, runtimes y SDKs

| Proyecto | Cómo se presenta | Énfasis declarado | Aporte a la comparación |
|---|---|---|---|
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python/blob/d7e52c375021248973f60ccbea8e7b69bc5b16e3/README.md) | Framework para flujos multiagente. | Agentes, herramientas, handoffs, guardrails, sesiones y trazas. | Primitivas para construir un sistema; no confundirlas con una aplicación configurada. |
| [LangChain](https://github.com/langchain-ai/langchain/blob/7ca02f333aa6d5e4cf566a2dcc444d06758e2958/README.md) | Framework para agentes y aplicaciones basadas en LLM. | Componentes e integraciones interoperables. | El framework contiene construcciones de harness: Deep Agents llama harness mínimo a create_agent. |
| [LangGraph](https://github.com/langchain-ai/langgraph/blob/2d942085e214ef6b99b6f54ed4d544a7c7c5ac56/README.md) | Framework de orquestación de bajo nivel para agentes con estado. | Ejecución duradera, intervención humana y persistencia. | Responsabilidades de runtime que un harness puede utilizar. |
| [OpenHands Software Agent SDK](https://github.com/OpenHands/software-agent-sdk/blob/cb7eabaf7b784a2f58f9df35d610f106287e823b/README.md) | SDK para construir agentes que trabajan con código. | Agentes y conversaciones con workspaces locales o remotos mediante Agent Server. | Separar definición del agente, conversación, herramientas y lugar de ejecución. |
| [smolagents](https://github.com/huggingface/smolagents/blob/c30b115286e000e98711fae5e85993547b73d826/README.md) | Biblioteca de agentes con abstracciones pequeñas. | CodeAgent expresa acciones como código; admite entornos de ejecución aislados. | Agente que usa código para actuar no equivale a agente dedicado a programar. |
| [Google ADK](https://github.com/google/adk-python/blob/71d5ed77382865c419a57692d68c296866efe2e5/README.md) | Framework flexible y modular de desarrollo de agentes. | Workflows, runtime, delegación y herramientas. | Un framework puede incluir mecanismos de runtime; las categorías se solapan. |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework/blob/b9d24c8fb484c8330abe8bb9e7500ca3c3bbf46c/README.md) | Framework para agentes y flujos multiagente. | Middleware, grafos, checkpoints, streaming y observabilidad. | Evaluar componentes de una configuración; MAF es una tecnología, harness es un concepto. |
| [Mastra](https://github.com/mastra-ai/mastra/blob/a793ec23949ee59b4aa850d83f9e1eba365ac5c8/README.md) | Framework TypeScript para aplicaciones y agentes. | Agentes, workflows y gestión de contexto y memoria. | Distinguir marco de desarrollo, mecanismos integrados y aplicación resultante. |
| [Agno](https://github.com/agno-agi/agno/blob/c44b082010d925d083b945798deb82ae8fb9429e/README.md) | Framework y runtime para plataformas de agentes. | Construcción de agentes y ejecución como servicio mediante AgentOS. | La propia descripción combina framework y runtime; no forzar una etiqueta excluyente. |
| [CrewAI](https://github.com/crewAIInc/crewAI/blob/1133f16cab274b9863b36fdacca7766b30e549fd/README.md) | Framework para flujos multiagente. | Crews de agentes y Flows dirigidos por eventos. | Estudiar colaboración y control del flujo, sin asumir que multiagente sea requisito de harness. |

### Harness de evaluación

| Proyecto | Cómo se presenta | Énfasis declarado | Aporte a la comparación |
|---|---|---|---|
| [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness/blob/d6de81643928d653435c431bae19945d41d32520/README.md) | Framework para evaluar modelos de lenguaje. | Tareas y ejecución de evaluaciones. | Comparador terminológico: evaluation harness no es sinónimo de agent harness. |

## Normalización del vocabulario

Se propone comparar responsabilidades y después relacionarlas con componentes de cada implementación. La columna de equivalencias permite conectar vocabulario; no afirma que las implementaciones sean intercambiables.

| Dimensión | Términos próximos en las fuentes | Aspecto que debe precisarse |
|---|---|---|
| Control | agent loop, runner, orchestration | Quién invoca el modelo y quién decide continuar, delegar o terminar. |
| Entrada al modelo | context management, assembly, prompt construction | Qué información se selecciona, transforma y entrega en cada llamada. |
| Acciones | tools, code execution, shell, integrations | Cómo una salida se convierte en una operación y cómo vuelve el resultado. |
| Continuidad | state, session, history, checkpoint, memory | Qué se conserva, durante cuánto tiempo y para qué uso; son objetos relacionados, no sinónimos. |
| Restricciones | permissions, guardrails, hooks, policies | Qué regla se aplica, dónde se aplica y si previene, interrumpe o registra una acción. |
| Entorno | workspace, sandbox, compute | Dónde ocurren los efectos; un workspace no implica aislamiento. |
| Construcción | framework, SDK, capabilities, extensions | Qué se reutiliza y qué debe configurar la aplicación. |
| Evaluación | tracing, evals, benchmarks | Las trazas describen ejecuciones; los criterios de evaluación determinan cómo juzgarlas. |

Esta matriz permite describir MAF como una tecnología que aporta mecanismos de varias dimensiones, y harness como un concepto sobre la coordinación del sistema. No los coloca al mismo nivel ni convierte todos los productos en capas excluyentes.

## Coincidencias y diferencias

**Punto común operativo.** Las perspectivas de ingeniería de Anthropic y OpenAI coinciden en vincular llamadas al modelo, acciones y resultados mediante software. Pi muestra que ese sistema puede mantenerse pequeño; Deep Agents, Strands y DeerFlow muestran configuraciones más integradas. La formulación común se refiere a una responsabilidad, no a una cantidad mínima de componentes. Fuentes: definiciones y filas de estos proyectos arriba.

**Capacidades variables.** La documentación de Pi excluye del núcleo ciertas decisiones que otros proyectos incorporan de inicio. Por ello, planificación explícita, subagentes, skills y memoria entre sesiones se tratarán como capacidades que deben describirse por configuración. No se proponen como requisitos universales del término.

**Frontera de infraestructura.** La definición amplia de LangChain incluye infraestructura en el harness; las arquitecturas examinadas de Anthropic y OpenAI distinguen control y sandbox. Para la wiki, «coordinar una herramienta» y «contener su implementación o su infraestructura» serán relaciones distintas. Un componente puede participar en el sistema sin estar empaquetado dentro del harness.

**Runtime y framework.** Deep Agents denomina a create_agent un harness mínimo sobre LangGraph. Pydantic considera que su agente básico ya tiene un harness ligero. ADK y Agno incluyen runtime en su presentación de framework. Esto impide adoptar framework → runtime → harness como una jerarquía universal: conviene registrar qué responsabilidades asume cada componente y sobre cuál se construye.

**Agente de código.** mini-swe-agent utiliza Bash sin requerir la interfaz nativa de tool calling. smolagents distingue generar código como forma de actuar de trabajar específicamente en tareas de programación. Ambas observaciones amplían el análisis más allá de un contrato de API o un dominio de aplicación particular.

**Evaluación.** Anthropic y LM Evaluation Harness permiten separar el sistema que conduce al agente del sistema que ejecuta y califica pruebas. Las evaluaciones pueden orientar la ingeniería de un harness; eso no las convierte necesariamente en parte del bucle que atiende una tarea.

## Propuesta de definición

La siguiente formulación es una **síntesis editorial propuesta**, no un consenso formal de los proyectos examinados:

> Un harness agéntico es el andamiaje de software que coordina la interacción de un modelo con su entorno para ejecutar una tarea.

El desarrollo explicativo puede precisar el mecanismo sin cargar la primera frase:

> Prepara las entradas del modelo, interpreta sus salidas, gestiona las acciones y sus resultados, y mantiene la continuidad del ciclo hasta su terminación. Su implementación puede incorporar memoria, planificación, delegación, restricciones y mecanismos de recuperación según los requisitos de la tarea.

Se recomienda usar **harness agéntico** cuando el objeto es ese ciclo. **AI harness** puede mantenerse como término más amplio, siempre indicando el sistema al que se aplica. **Harness engineering** designará la práctica de diseñar y evaluar ese andamiaje. **Agent runtime** nombrará responsabilidades de ejecución y ciclo de vida; su frontera se describirá por implementación. **Evaluation harness** tendrá una entrada y relaciones propias.

Esta definición evita prometer fiabilidad, autonomía o escalabilidad por el solo hecho de incorporar un harness. Esas propiedades deben evaluarse sobre una configuración, tarea y entorno identificados.

## Decisiones para revisión

1. **Alcance:** se recomienda definir el concepto por su función de coordinación y describir aparte los componentes incluidos en cada implementación. La alternativa amplia —todo lo externo al modelo— facilita una vista general, pero pierde precisión al delimitar servicios, herramientas y entorno.
2. **Entrada editorial:** se recomienda mantener la frase corta anterior y abrir inmediatamente el mecanismo. Una formulación más operacional sería: «Un harness agéntico coordina el ciclo de llamadas al modelo, ejecución de acciones e incorporación de resultados».
3. **Mapa de conceptos:** preservar las relaciones entre contexto, estado, memoria, control, acciones y entorno. La comparación de productos será una vista sobre ese mapa; no su taxonomía principal.

La definición vigente del piloto sigue provisional. Jairzinho decidirá la redacción y las fronteras que adopte la wiki después de revisar esta comparación.

## Método y trazabilidad

Selección intencional de proyectos que permiten contrastar minimalismo, composición, continuidad, orquestación, aplicaciones de código y evaluación. Incluye los ecosistemas solicitados y familias relacionadas; no ordena por popularidad ni afirma cobertura exhaustiva. Se consultaron READMEs públicos en commits de sus ramas predeterminadas y documentación primaria de los autores. Un commit de esa rama no implica una release estable.

Los [datos de observación](observations.json) conservan afirmación, alcance, fuente, commit o fecha de consulta, base documental e interpretación. El [manifiesto](manifest.json) identifica el corte y la integridad de las entradas. Los hashes de README identifican el texto recibido mediante la API de GitHub; no se redistribuyen documentos completos. Las páginas web vivas conservan localizador y fecha de acceso; no se capturó una copia histórica completa de ellas.

Los nombres actuales resueltos por GitHub incluyen earendil-works/pi, aaif-goose/goose y strands-agents/harness-sdk. El README de [letta-ai/letta](https://github.com/letta-ai/letta/blob/5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a/README.md) dirige al repositorio Letta Code, usado en la tabla. Estas observaciones de ubicación no fechan cuándo ocurrió cada cambio.

La selección no debe leerse como «27 stacks íntegramente open source». El README y la documentación del Claude Agent SDK distinguen el SDK, el binario de Claude Code y sus términos; tener código público del SDK no demuestra apertura de todo el sistema. Mastra documenta un núcleo Apache-2.0 y componentes ee/ con licencia empresarial. Las licencias declaradas por GitHub se conservan como metadatos del repositorio, no como auditoría de dependencias o de servicios.

No se validaron afirmaciones comerciales de superioridad, rendimiento, aprendizaje o preparación para producción. La ausencia de ensayos impide extraer un ranking técnico. El [perfil anterior de Pi](../../tech/pi/README.md) conserva su propio commit de inspección: esta revisión documental no lo actualiza silenciosamente.
