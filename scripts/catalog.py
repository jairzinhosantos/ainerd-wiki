#!/usr/bin/env python3
"""Genera el catálogo desde las páginas; --check no modifica archivos."""
import argparse
from pathlib import Path
import sys
from knowledge import build

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    outputs, errors = build(root)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    for name, content in outputs.items():
        path = root / 'catalog' / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                print(f'catalog/{name}: desactualizado', file=sys.stderr)
                return 1
        else:
            path.parent.mkdir(exist_ok=True)
            path.write_text(content, encoding='utf-8')
    print('Catálogo comprobado.' if args.check else 'Catálogo generado.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
