#!/usr/bin/env python3
"""Comprueba documentos, relaciones, enlaces locales y catálogo."""
from pathlib import Path
import sys
from knowledge import validate_repository

if __name__ == '__main__':
    _, errors = validate_repository(Path(__file__).resolve().parents[1])
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print('Identidades, metadatos, relaciones, enlaces locales y catálogo correctos.')
