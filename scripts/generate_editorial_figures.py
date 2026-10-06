"""Genera las figuras SVG del piloto. Ejecutar desde cualquier directorio."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'harness'
INK, MUTED, LINE = '#203b43', '#546e75', '#a9bdc2'
TEAL, PURPLE, ORANGE = '#13776e', '#62598d', '#b65a28'


def text(x, y, value, size=18, color=INK, weight=400, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'


def card(x, y, w, h, title, lines, color=TEAL, fill='#ffffff'):
    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{color}" stroke-width="1.5"/>', text(x+w/2, y+32, title, 21, color, 650)]
    for i, line in enumerate(lines):
        parts.append(text(x+w/2, y+59+i*24, line, 17, MUTED))
    return ''.join(parts)


def path(d, arrow=False):
    return f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="1.6"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>'


def save(name, h, title, desc, content):
    OUT.mkdir(parents=True, exist_ok=True)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="{h}" viewBox="0 0 1120 {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="none" stroke="{LINE}"/></marker></defs>
<rect width="1120" height="{h}" rx="18" fill="#f8faf9"/>
<g font-family="Inter, system-ui, sans-serif">{content}</g></svg>'''
    (OUT / name).write_text(svg)


def overview():
    left = [('Contexto', ['Información de esta llamada']), ('Memoria', ['Información que se conserva']), ('Estado', ['Situación actual de la tarea']), ('Recuperación', ['Fuentes y evidencia pertinente']), ('Herramientas y skills', ['Acciones y procedimientos'])]
    right = [('Orquestación', ['Pasos, decisiones y delegación']), ('Políticas e intervención', ['Permisos y revisión humana']), ('Observabilidad', ['Eventos, trazas y métricas']), ('Evaluación', ['Calidad frente a criterios']), ('Runtime y fiabilidad', ['Ejecución, límites y recuperación'])]
    s = '<rect x="18" y="18" width="1084" height="636" rx="16" fill="none" stroke="#b8c9cc" stroke-dasharray="6 5"/>'
    s += text(46, 53, 'HARNESS', 15, MUTED, 650, 'start')
    # Una columna por responsabilidad; conexiones sin dirección: no son un flujo.
    for i in range(5):
        y = 83+i*108
        s += path(f'M 356 {y+43} L 442 339') + path(f'M 678 339 L 764 {y+43}')
    for items, x, color in [(left, 40, TEAL), (right, 764, PURPLE)]:
        for i, (title, lines) in enumerate(items):
            s += card(x, 83+i*108, 316, 86, title, lines, color)
    s += card(442, 273, 236, 132, 'Modelo', ['LLM', 'Generación de tokens'], ORANGE, '#fff5ec')
    s += text(560, 445, 'Capacidades conectadas', 16, MUTED)
    s += text(560, 470, 'alrededor del modelo', 16, MUTED)
    save('overview.svg', 675, 'Componentes de un harness de IA', 'Modelo central rodeado por contexto, memoria, estado, recuperación, herramientas, orquestación, políticas, observabilidad, evaluación y runtime. Las líneas indican relaciones, no orden de ejecución.', s)


def scenarios():
    s = text(560, 43, 'Dos escenarios · responsabilidades compartidas', 23, INK, 650)
    cols = [(30, 'Agentes de código', ['Repositorio, editor y terminal', 'Diffs, pruebas y dependencias', 'Permisos sobre el workspace', 'Entrega de cambios revisables'], TEAL), (398, 'En común', ['Modelo y contexto', 'Memoria y estado', 'Herramientas y políticas', 'Runtime, trazas y evaluación'], ORANGE), (766, 'Agentes empresariales', ['Canales, APIs y datos', 'Identidad y reglas del proceso', 'Efectos en sistemas externos', 'Seguimiento de operaciones'], PURPLE)]
    for x, title, lines, color in cols:
        s += f'<rect x="{x}" y="78" width="324" height="295" rx="14" fill="white" stroke="{color}" stroke-width="1.5"/>'
        s += text(x+162, 120, title, 22, color, 650)
        for i, line in enumerate(lines):
            s += text(x+162, 173+i*48, line, 17)
    s += text(560, 415, 'La autonomía, el riesgo y la revisión humana se definen por tarea.', 18, MUTED)
    save('scenarios.svg', 448, 'Agentes de código y agentes empresariales', 'Comparación de escenarios, sin capacidades exclusivas: ambos necesitan políticas, estado, ejecución y evaluación. El grado de autonomía depende de la tarea.', s)


def assembly():
    s = text(40, 45, 'CONTEXTO', 15, MUTED, 650, 'start')
    inputs=[('Instrucciones', ['Objetivo y restricciones']), ('Estado e historial', ['Trabajo en curso']), ('Memoria', ['Información recuperada']), ('Fuentes y herramientas', ['Evidencia y resultados'])]
    for i, (title, lines) in enumerate(inputs):
        x=30+i*270
        s += card(x, 73, 250, 90, title, lines)
        s += path(f'M {x+125} 163 V 202')
    s += path('M 155 202 H 965 M 252 202 V 246', True)
    stages=[('Seleccionar', ['Relevancia y vigencia']), ('Transformar', ['Filtrar, resumir, recortar']), ('Ensamblar', ['Roles, orden y presupuesto'])]
    for i,(title, lines) in enumerate(stages):
        x=112+i*306
        s+=card(x, 250, 280, 90, title, lines, PURPLE)
        if i<2:s+=path(f'M {x+280} 295 H {x+303}',True)
    s+=path('M 1004 295 H 1075 V 417 H 700',True)
    s+=card(420, 373, 280, 90, 'Contexto de la llamada', ['Entrada seleccionada'], TEAL)
    s+=path('M 560 463 V 497',True)
    s+=card(420, 508, 280, 90, 'Modelo', ['Siguiente inferencia'], ORANGE, '#fff5ec')
    s+=text(560, 636, 'El ensamblaje se repite cuando cambian la tarea o sus observaciones.',18,MUTED)
    save('context-assembly.svg', 665, 'Ensamblaje de contexto', 'Cuatro fuentes alimentan selección, transformación y ensamblaje. El resultado es el contexto de una llamada al modelo. La memoria aporta información seleccionada; no se envía completa.',s)


if __name__ == '__main__':
    overview()
    scenarios()
    assembly()
    print('Generadas 3 figuras SVG.')
