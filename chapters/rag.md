---
id: 2
title: RAG
subtitle: Retrieval-Augmented Generation — dando memoria a los modelos
icon: fas fa-database
accent: c
pillar: academia
status: available
tags: [RAG, embeddings, vectorDB, arquitectura]
updated: 2026-07-05
---

## ¿Qué es RAG?

**Retrieval-Augmented Generation (RAG)** es un patrón de arquitectura que combina la capacidad generativa de un LLM con un sistema de recuperación de información. En lugar de depender exclusivamente del conocimiento «memorizado» en los pesos del modelo, RAG le da al LLM acceso a una base de conocimiento externa, actualizada y verificable.

El problema que resuelve es fundamental: los LLMs tienen un *corte de conocimiento* (training cutoff) y tienden a **alucinar** cuando no tienen información suficiente. RAG corrige ambos problemas.

## Cómo funciona RAG

El flujo básico de RAG tiene tres etapas:

### 1. Indexación (offline)

Los documentos de tu base de conocimiento se dividen en fragmentos (*chunks*), se transforman en vectores numéricos mediante un modelo de **embedding**, y se almacenan en una **base de datos vectorial** (Chroma, Pinecone, Weaviate, pgvector, etc.).

### 2. Recuperación (retrieval)

Cuando el usuario hace una pregunta, esta también se convierte en un vector. El sistema busca los fragmentos más similares semánticamente (usando *cosine similarity* o variantes) y recupera el contexto más relevante.

### 3. Generación (generation)

El LLM recibe el contexto recuperado junto con la pregunta original y genera una respuesta fundamentada en esa información. El prompt incluye instrucciones para que el modelo cite sus fuentes y no «invente».

## Variantes de RAG

- **Naive RAG:** implementación básica. Buena para prototipos pero limitada en producción.
- **Advanced RAG:** incorpora re-ranking, query expansion y mejoras en chunking.
- **Modular RAG:** arquitectura flexible donde cada componente (retriever, reranker, generator) es intercambiable.
- **Graph RAG:** utiliza grafos de conocimiento para relaciones complejas entre entidades. Desarrollado por Microsoft Research.
- **Agentic RAG:** el agente decide dinámicamente cuándo y cómo recuperar información.

## Métricas de evaluación

Evaluar RAG requiere medir dimensiones independientes:

- **Fidelidad (faithfulness):** ¿la respuesta está basada en el contexto recuperado?
- **Relevancia de respuesta:** ¿la respuesta responde realmente la pregunta?
- **Relevancia del contexto:** ¿el retriever trajo los fragmentos correctos?

Frameworks como **RAGAS** o **TruLens** permiten evaluar estas métricas automáticamente.

> RAG convierte a tu LLM en un experto con acceso a tu biblioteca. Sin RAG, el modelo es brillante pero amnésico respecto a tu contexto específico.
