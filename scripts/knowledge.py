"""Validación documental y catálogo; no certifica la verdad de la prosa."""
import csv
from datetime import date
import hashlib
import io
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import yaml
from evidence import load_evidence, check_bibliography

ROOTS = ('concepts', 'tech', 'architectures', 'benchmarks', 'labs')
TYPES = {'concept', 'technology', 'architecture', 'comparison', 'benchmark', 'lab'}
RELATIONS = ('parent', 'related', 'requires')
NODE_FIELDS = ('schema_version', 'id', 'title', 'type', 'status', 'path', 'updated', 'reviewed')
EDGE_FIELDS = ('schema_version', 'source', 'target', 'relation')

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for kn, vn in node.value:
        key = loader.construct_object(kn, deep=deep)
        if not isinstance(key, str):
            raise ValueError('las claves YAML deben ser texto')
        if key in result:
            raise ValueError(f'clave YAML duplicada: {key}')
        result[key] = loader.construct_object(vn, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def iso_date(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False

def within(path, root):
    return path.resolve().is_relative_to(root.resolve())

def prose(raw):
    return re.sub(r'^```.*?^```[^\n]*$', '', raw, flags=re.M | re.S)

def read_pages(root):
    pages, errors = [], []
    for directory in ROOTS:
        for path in sorted((root / directory).rglob('*.md')):
            relative = path.relative_to(root).as_posix()
            raw = path.read_text(encoding='utf-8')
            match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', raw, re.S)
            if not match:
                if path.name not in {'README.md', 'method.md'} and 'runs' not in path.parts:
                    errors.append(f'{relative}: faltan metadatos de página')
                continue
            try:
                meta = yaml.load(match.group(1), Loader=UniqueLoader)
                if not isinstance(meta, dict):
                    raise ValueError('los metadatos deben ser un mapa')
            except (yaml.YAMLError, ValueError) as exc:
                errors.append(f'{relative}: YAML inválido: {exc}')
                continue
            body, issues = raw[match.end():], []
            for key in ('id', 'title', 'summary', 'type', 'status', 'language', 'updated', 'reviewed'):
                if key not in meta:
                    issues.append(f'falta {key}')
            for key in ('id', 'title', 'summary', 'type', 'status'):
                if not isinstance(meta.get(key), str) or not meta[key].strip():
                    issues.append(f'{key} debe ser texto no vacío')
            if not re.fullmatch(r'[a-z][a-z0-9-]*', str(meta.get('id', ''))):
                issues.append('id inválido')
            if not isinstance(meta.get('type'), str) or meta['type'] not in TYPES:
                issues.append('type inválido')
            if meta.get('status') not in ('draft', 'published'):
                issues.append('status inválido')
            if meta.get('language') != 'es':
                issues.append('language debe ser es')
            if not iso_date(meta.get('updated')):
                issues.append('updated debe ser fecha ISO entre comillas')
            if meta.get('reviewed') is not None and not iso_date(meta['reviewed']):
                issues.append('reviewed debe ser fecha ISO entre comillas o null')
            sources = meta.get('sources', [])
            if 'evidence' in meta:
                try:
                    if meta['evidence'] != 'observations.json' or meta.get('type') not in {'comparison', 'benchmark'}:
                        raise ValueError('evidence solo admite observations.json en comparativas')
                    if 'sources' in meta:
                        raise ValueError('usar evidence o sources, no ambos')
                    evidence = load_evidence(path.parent / 'observations.json')
                    check_bibliography(body, evidence)
                    sources = [source['url'] for source in evidence['sources']]
                except (OSError, ValueError, TypeError) as exc:
                    issues.append(f'evidencia inválida: {exc}')
            if not isinstance(sources, list) or any(not isinstance(x, str) or urlsplit(x).scheme not in {'http', 'https'} or not urlsplit(x).netloc for x in sources):
                issues.append('sources debe ser una lista de URLs http(s)')
            if re.findall(r'^# (.+)$', prose(body), flags=re.M) != [meta.get('title')]:
                issues.append('debe existir un único H1 igual a title')
            for relation in RELATIONS:
                values = meta.get(relation)
                if relation == 'parent':
                    values = [] if values is None else [values]
                elif values is None:
                    values = []
                if not isinstance(values, list) or any(not isinstance(x, str) for x in values):
                    issues.append(f'{relation}: IDs inválidos')
            if meta.get('status') == 'published':
                if not iso_date(meta.get('reviewed')):
                    issues.append('published requiere reviewed')
                if not isinstance(sources, list) or not sources:
                    issues.append('published requiere fuentes públicas')
                if '[sin verificar]' in body.lower():
                    issues.append('published conserva afirmaciones sin verificar')
                if meta.get('type') == 'technology' and (not isinstance(meta.get('examined_ref'), str) or not meta['examined_ref'].strip()):
                    issues.append('technology publicada requiere examined_ref')
            if issues:
                errors.extend(f'{relative}: {issue}' for issue in issues)
            else:
                pages.append({'path': relative, 'meta': meta, 'body': body})
    return pages, errors

def validate_relations(pages):
    errors, nodes, edges = [], {}, []
    for page in pages:
        key = page['meta']['id']
        if key in nodes:
            errors.append(f'id duplicado {key}')
        nodes[key] = page
    for page in pages:
        meta = page['meta']
        for relation in RELATIONS:
            values = meta.get(relation) or []
            if relation == 'parent':
                values = [values] if values else []
            if len(values) != len(set(values)):
                errors.append(f'{meta["id"]}: relación {relation} duplicada')
            for target in values:
                edges.append((meta['id'], target, relation))
                if target not in nodes:
                    errors.append(f'{meta["id"]}: destino inexistente {target}')
                elif target == meta['id']:
                    errors.append(f'{target}: autorrelación {relation}')
                elif meta['status'] == 'published' and nodes[target]['meta']['status'] != 'published':
                    errors.append(f'{meta["id"]}: relación pública hacia borrador {target}')
    for relation in ('parent', 'requires'):
        graph = {key: [] for key in nodes}
        for a, b, kind in edges:
            if kind == relation and b in nodes:
                graph[a].append(b)
        active, done = set(), set()
        def visit(node):
            if node in active:
                errors.append(f'ciclo en {relation}: {node}')
                return
            if node in done:
                return
            active.add(node)
            for target in graph[node]:
                visit(target)
            active.remove(node)
            done.add(node)
        for key in graph:
            visit(key)
    return errors, sorted(set(edges))

def validate_snapshots(root, pages):
    errors = []
    for page in pages:
        meta = page['meta']
        if meta['type'] not in {'comparison', 'benchmark'} or (meta['status'] != 'published' and 'evidence' not in meta):
            continue
        directory = (root / page['path']).parent
        try:
            manifest = json.loads((directory / 'manifest.json').read_text())
            observations = json.loads((directory / 'observations.json').read_text())
            if not isinstance(manifest, dict) or not iso_date(manifest.get('cutoff')):
                raise ValueError('manifest requiere cutoff ISO')
            if 'evidence' in meta:
                observations = load_evidence(directory / 'observations.json')['observations']
            if not isinstance(observations, list) or not observations:
                raise ValueError('observations debe contener observaciones')
            for obs in ([] if 'evidence' in meta else observations):
                if not isinstance(obs, dict):
                    raise ValueError('observación inválida')
                for key in ('id', 'technology', 'component', 'examined_ref', 'claim', 'source', 'scope'):
                    if not isinstance(obs.get(key), str) or not obs[key].strip():
                        raise ValueError(f'observación requiere {key}')
                if obs.get('basis') not in ('docs', 'code', 'run') or not iso_date(obs.get('observed')):
                    raise ValueError('basis u observed inválido')
            inputs = manifest.get('inputs')
            if not isinstance(inputs, list) or not inputs:
                raise ValueError('manifest requiere inputs')
            observed = False
            for item in inputs:
                if not isinstance(item, dict) or not isinstance(item.get('path'), str):
                    raise ValueError('input inválido')
                path = directory / item['path']
                if Path(item['path']).is_absolute() or not within(path, directory):
                    raise ValueError('input fuera del estudio')
                if hashlib.sha256(path.read_bytes()).hexdigest() != item.get('sha256'):
                    raise ValueError(f'checksum distinto: {item["path"]}')
                observed |= path.resolve() == (directory / 'observations.json').resolve()
            if not observed:
                raise ValueError('manifest no identifica observations.json')
        except (OSError, ValueError, TypeError, KeyError) as exc:
            errors.append(f'{page["path"]}: evidencia histórica inválida: {exc}')
    return errors

def validate_links(root):
    errors = []
    for path in sorted(root.rglob('*.md')):
        relative = path.relative_to(root)
        if any(p.startswith('.') or p == '__pycache__' for p in relative.parts) or relative.parts[0] == 'chapters':
            continue
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', prose(path.read_text())):
            target = target.strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            target = unquote(target.split('#', 1)[0])
            if not target:
                continue
            dest = path.parent / target
            if not within(dest, root):
                errors.append(f'{relative}: enlace fuera del repo: {target}')
            elif not dest.exists():
                errors.append(f'{relative}: enlace ausente: {target}')
    return errors

def csv_text(fields, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()

def build(root):
    pages, errors = read_pages(root)
    relation_errors, edges = validate_relations(pages)
    errors.extend(relation_errors)
    errors.extend(validate_snapshots(root, pages))
    nodes = []
    for page in sorted(pages, key=lambda p: p['meta']['id']):
        meta = page['meta']
        nodes.append({'schema_version': '1', **{key: meta.get(key) or '' for key in NODE_FIELDS if key not in {'path', 'schema_version'}}, 'path': page['path']})
    return {'nodes.csv': csv_text(NODE_FIELDS, nodes), 'edges.csv': csv_text(EDGE_FIELDS, [{'schema_version': '1', 'source': a, 'target': b, 'relation': k} for a, b, k in edges])}, errors

def validate_repository(root, generated=True):
    outputs, errors = build(root)
    errors.extend(validate_links(root))
    for name in ROOTS:
        for path in (root / name).rglob('*'):
            if path.name.casefold() == 'agents.md':
                errors.append(f'{path.relative_to(root)}: nombre reservado para instrucciones')
    if generated:
        for name, content in outputs.items():
            path = root / 'catalog' / name
            if not path.exists() or path.read_text() != content:
                errors.append(f'catalog/{name}: regenerar con scripts/catalog.py')
    return outputs, errors
