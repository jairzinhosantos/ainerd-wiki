---
id: 3
title: MCP
subtitle: Model Context Protocol — el protocolo que conecta modelos con el mundo
icon: fas fa-plug
accent: i
status: available
tags: [MCP, protocolo, herramientas, integración]
updated: 2026-07-05
---

## ¿Qué es el Model Context Protocol?

El **Model Context Protocol (MCP)** es un estándar abierto creado por Anthropic (2024) que define cómo los modelos de lenguaje se conectan con fuentes de datos externas y herramientas de forma estandarizada. Es, en esencia, el «USB de la IA»: un protocolo universal que permite que cualquier LLM se conecte a cualquier recurso externo sin necesidad de integraciones personalizadas.

## El problema que resuelve

Antes de MCP, cada integración de LLM con herramientas externas (bases de datos, APIs, archivos) requería código personalizado específico para cada modelo y cada fuente. Esto generaba una explosión combinatoria de integraciones imposible de mantener.

MCP define una arquitectura cliente-servidor donde:

- **MCP Servers:** exponen recursos, herramientas y prompts de forma estandarizada.
- **MCP Clients:** son los modelos o aplicaciones que consumen esos recursos.
- **MCP Host:** el entorno que orquesta la comunicación (Claude Desktop, IDEs, etc.).

## Conceptos fundamentales

### Resources (recursos)

Datos que el servidor expone al modelo para leer. Pueden ser archivos, registros de base de datos, respuestas de APIs, etc. Son análogos a los endpoints GET de una API REST.

### Tools (herramientas)

Funciones que el modelo puede ejecutar. Son análogos a los endpoints POST. Cuando un modelo llama a una tool, está ejecutando código real en tu sistema.

### Prompts (plantillas)

Templates de prompts reutilizables que el servidor puede exponer para estandarizar interacciones comunes.

## ¿Por qué importa MCP?

MCP está transformando el ecosistema de IA de dos formas:

- **Estandarización:** cualquier IDE, cliente de chat o aplicación que implemente MCP puede usar cualquier servidor MCP sin cambios de código.
- **Seguridad:** el protocolo define claramente qué puede hacer el modelo y qué no, con permisos explícitos.

> MCP es la diferencia entre tener un asistente brillante encerrado en una caja y tener un asistente que puede actuar en el mundo real. Es el puente entre el razonamiento del modelo y la acción.
