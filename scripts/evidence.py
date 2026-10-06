"""Fuentes y observaciones en un único archivo; bibliografía derivada."""
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

START = '<!-- references:start -->'
END = '<!-- references:end -->'


def public_url(value):
    return isinstance(value, str) and urlsplit(value).scheme in {'http', 'https'} and bool(urlsplit(value).netloc)


def validate_evidence(data):
    from knowledge import iso_date
    if not isinstance(data, dict) or data.get('schema_version') != 2:
        raise ValueError('evidence requiere schema_version 2')
    sources, observations = data.get('sources'), data.get('observations')
    if not isinstance(sources, list) or not sources or not isinstance(observations, list) or not observations:
        raise ValueError('evidence requiere sources y observations no vacíos')
    ids = set()
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError('fuente inválida')
        for key in ('id', 'title', 'kind'):
            if not isinstance(source.get(key), str) or not source[key].strip():
                raise ValueError(f'fuente requiere {key}')
        if source['id'] in ids:
            raise ValueError('id de fuente duplicado')
        ids.add(source['id'])
        if not public_url(source.get('url')) or not iso_date(source.get('accessed')):
            raise ValueError('fuente requiere URL pública y accessed ISO')
        if 'authors' in source and (not isinstance(source['authors'], list) or not source['authors'] or any(not isinstance(a, str) or not a.strip() for a in source['authors'])):
            raise ValueError('authors inválido')
    observation_ids, used = set(), set()
    for obs in observations:
        if not isinstance(obs, dict):
            raise ValueError('observación inválida')
        for key in ('id', 'subject', 'claim', 'scope'):
            if not isinstance(obs.get(key), str) or not obs[key].strip():
                raise ValueError(f'observación requiere {key}')
        if obs['id'] in observation_ids:
            raise ValueError('id de observación duplicado')
        observation_ids.add(obs['id'])
        if obs.get('basis') not in ('docs', 'code', 'run') or not iso_date(obs.get('observed')):
            raise ValueError('basis u observed inválido')
        citations = obs.get('citations')
        if not isinstance(citations, list) or not citations:
            raise ValueError('observación requiere citations')
        for citation in citations:
            if not isinstance(citation, dict) or citation.get('source') not in ids:
                raise ValueError('cita a fuente inexistente')
            used.add(citation['source'])
    if used != ids:
        raise ValueError('fuente sin observaciones')
    return data


def load_evidence(path):
    return validate_evidence(json.loads(Path(path).read_text(encoding='utf-8')))


def bibliography(data):
    lines = [START]
    for source in data['sources']:
        author = ', '.join(source.get('authors', [])) or source.get('organization', '')
        label = author.rstrip('.') + '. ' if author else ''
        label += f"[{source['title']}]({source['url']})"
        details = [source[k] for k in ('published', 'edition') if source.get(k)]
        if source.get('version'):
            version = source['version']
            details.append('revisión ' + (version[:12] if re.fullmatch(r'[0-9a-f]{40}', version) else version))
        details.append(f"consulta {source['accessed']}")
        lines.append(f"- {label}. {'; '.join(details)}.")
    return '\n'.join(lines + [END])


def check_bibliography(body, data):
    if body.count(START) != 1 or body.count(END) != 1:
        raise ValueError('falta bloque único de referencias generado')
    actual = body[body.index(START):body.index(END) + len(END)]
    if actual != bibliography(data):
        raise ValueError('referencias desactualizadas; ejecutar scripts/references.py')
