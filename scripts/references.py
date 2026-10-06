"""Regenera referencias y hashes sin red ni modelos."""
import argparse
import hashlib
import json
from pathlib import Path
from evidence import START, END, bibliography, load_evidence


def update(directory):
    path = directory / 'observations.json'
    data = load_evidence(path)
    readme = directory / 'README.md'
    text = readme.read_text()
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError('README requiere un bloque references:start/end')
    start, end = text.index(START), text.index(END) + len(END)
    readme.write_text(text[:start] + bibliography(data) + text[end:])
    manifest_path = directory / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest['cutoff'] = max(o['observed'] for o in data['observations'])
    manifest['source_count'] = len(data['sources'])
    manifest['observation_count'] = len(data['observations'])
    manifest.pop('project_count', None)
    manifest.pop('primary_document_count', None)
    manifest['inputs'] = [{'path': 'observations.json', 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}]
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    update(parser.parse_args().directory)
