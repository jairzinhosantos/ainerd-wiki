---
id: language-model
title: "Modelo de lenguaje grande"
summary: "Generación autorregresiva, tokens y relación del modelo con el harness."
type: concept
status: draft
language: es
updated: "2026-10-05"
reviewed: null
related: [harness, context-assembly]
sources:
  - https://huggingface.co/docs/transformers/v4.38.2/en/tasks/language_modeling
  - https://developers.openai.com/api/docs/concepts
  - https://developers.openai.com/blog/codex-as-a-platform
---

# Modelo de lenguaje grande

Un **modelo de lenguaje grande (LLM)** aprende patrones del lenguaje a partir de datos. En un modelo autorregresivo, la generación avanza prediciendo el siguiente token a partir de la secuencia disponible. El token generado se incorpora a esa secuencia y el proceso continúa. [Hugging Face: causal language modeling](https://huggingface.co/docs/transformers/v4.38.2/en/tasks/language_modeling).

`Contexto → predicción del siguiente token → secuencia ampliada → siguiente predicción`

Un **token** es una unidad de representación del texto: puede corresponder a una palabra o a parte de ella, entre otras secuencias de caracteres. Su división depende del tokenizador. Por eso «predecir la siguiente palabra» es una aproximación; «predecir el siguiente token» describe mejor este mecanismo. [OpenAI: tokens](https://developers.openai.com/api/docs/concepts#tokens).

## Relación con el harness

El modelo puede generar texto que representa una respuesta, código o una solicitud de herramienta. Para que esa solicitud produzca una acción, el sistema debe interpretarla, controlar su ejecución y devolver el resultado. El [harness](../harness/README.md) conecta esas operaciones con el modelo. [OpenAI: agent loop y harness](https://developers.openai.com/blog/codex-as-a-platform).

La predicción de tokens describe el mecanismo de generación autorregresiva; no resume por sí sola el entrenamiento, las capacidades ni todos los tipos de modelos. Esta entrada conecta con [el ensamblaje de contexto](../harness/context/context-assembly.md), donde se estudia cómo preparar la información de cada llamada.
