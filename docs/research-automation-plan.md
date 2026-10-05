# Evaluación futura de la automatización de investigación

Estado: deferred. No se ha implementado ni programado una automatización.

## Problema

Los estudios conversacionales son extensos, difíciles de retomar y pueden producir más material del que se llega a leer. La exportación completa de una cuenta no es una entrada práctica para cada sesión. Queremos conservar comprensión, trazabilidad y control de la profundidad.

## Opciones a evaluar

| Opción | Entrada y experiencia | Coste principal |
|---|---|---|
| Flujo directo sobre archivos | Pregunta en un agente; lee la wiki, investiga y deja análisis, síntesis y pendientes en el notebook | Diseñar instrucciones y continuidad; validar calidad de evidencia |
| Captura asistida de una conversación | Texto pegado o captura seleccionada mediante una capacidad disponible y autorizada | Evaluar acceso real, integridad de citas e imágenes y mantenimiento de la integración |
| Interfaz web de estudio | Cola de preguntas, síntesis progresiva, lecturas pendientes y controles de profundidad | Aplicación, autenticación, almacenamiento, coste y operación |

La primera referencia será el flujo directo sin web. La captura de conversaciones y cualquier API se investigarán con documentación oficial actual; no se asume un endpoint de descarga por chat ni se automatiza la extracción ahora.

## Criterios de la evaluación

- Una pregunta acotada y un presupuesto de lectura, tiempo y coste.
- Resumen breve primero; profundidad por secciones bajo demanda.
- Separar resultados nuevos, fuentes, contradicciones y pendientes.
- Detectar repetición y reusar el conocimiento ya escrito.
- Conservar citas y versiones; declarar fallos de acceso.
- Permitir retomar en otra sesión sin releer el chat completo.
- Probar la calidad con un estudio real antes de elegir una web o scheduler.

El entregable futuro será una comparación de las opciones, un prototipo pequeño y una recomendación. La publicación o actualización automática de la wiki requerirá su propio alcance; esta evaluación no la activa.
