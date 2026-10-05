from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from knowledge import build, validate_repository


class KnowledgeContracts(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def page(self, filename='concepts/example.md', key='example', extra='', status='draft', kind='concept', body=''):
        path = self.root / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        reviewed = '"2026-10-04"' if status == 'published' else 'null'
        sources = '["https://example.org/source"]' if status == 'published' else '[]'
        path.write_text(f'---\nid: {key}\ntitle: "Ejemplo"\nsummary: "Una pregunta."\ntype: {kind}\nstatus: {status}\nlanguage: es\nupdated: "2026-10-04"\nreviewed: {reviewed}\nsources: {sources}\n{extra}---\n\n# Ejemplo\n\n{body}\n')
        return path

    def errors(self):
        return '\n'.join(validate_repository(self.root, generated=False)[1])

    def test_moving_a_page_preserves_identity_and_edges(self):
        p = self.page()
        self.page('concepts/child.md', 'child', 'parent: example\n')
        before, errors = build(self.root)
        self.assertEqual(errors, [])
        dest = self.root / 'concepts' / 'new-name.md'
        p.rename(dest)
        after, errors = build(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(before['edges.csv'], after['edges.csv'])
        self.assertIn('concepts/new-name.md', after['nodes.csv'])

    def test_duplicate_ids_are_rejected(self):
        self.page()
        self.page('tech/duplicate.md')
        self.assertIn('id duplicado', self.errors())

    def test_dangling_relation_is_rejected(self):
        self.page(extra='related: [missing]\n')
        self.assertIn('destino inexistente', self.errors())

    def test_parent_cycle_is_rejected(self):
        self.page(extra='parent: other\n')
        self.page('concepts/other.md', 'other', 'parent: example\n')
        self.assertIn('ciclo en parent', self.errors())

    def test_published_page_cannot_depend_on_hidden_draft(self):
        self.page(status='published', extra='related: [draft]\n')
        self.page('concepts/draft.md', 'draft')
        self.assertIn('relación pública hacia borrador', self.errors())

    def test_published_technology_needs_an_examined_revision(self):
        self.page(status='published', kind='technology')
        self.assertIn('requiere examined_ref', self.errors())

    def test_published_page_requires_review(self):
        p = self.page(status='published')
        p.write_text(p.read_text().replace('reviewed: "2026-10-04"', 'reviewed: null'))
        self.assertIn('published requiere reviewed', self.errors())

    def test_repeated_yaml_keys_are_not_silently_overwritten(self):
        self.page(extra='status: published\n')
        self.assertIn('clave YAML duplicada', self.errors())

    def test_broken_markdown_link_is_rejected_but_code_example_ignored(self):
        p = self.page(body='```markdown\n[Ejemplo](missing.md)\n```')
        self.assertEqual(self.errors(), '')
        p.write_text(p.read_text() + '\n[Enlace](missing.md)\n')
        self.assertIn('enlace ausente', self.errors())

    def test_stale_catalog_is_detected(self):
        self.page()
        outputs, _ = build(self.root)
        (self.root / 'catalog').mkdir()
        for name, content in outputs.items():
            (self.root / 'catalog' / name).write_text(content)
        self.assertEqual(validate_repository(self.root)[1], [])
        self.page('concepts/new.md', 'new')
        self.assertIn('regenerar', '\n'.join(validate_repository(self.root)[1]))

    def snapshot(self):
        p = self.page('benchmarks/case/README.md', status='published', kind='comparison')
        observations = p.parent / 'observations.json'
        observations.write_text(json.dumps([{'id': 'one', 'technology': 'example', 'component': 'part', 'examined_ref': 'v1', 'claim': 'Una observación', 'source': 'https://example.org', 'scope': 'fixture', 'basis': 'docs', 'observed': '2026-10-04'}]))
        manifest = {'cutoff': '2026-10-04', 'inputs': [{'path': 'observations.json', 'sha256': hashlib.sha256(observations.read_bytes()).hexdigest()}]}
        (p.parent / 'manifest.json').write_text(json.dumps(manifest))
        return observations, manifest

    def test_changed_comparison_input_is_detected(self):
        observations, _ = self.snapshot()
        self.assertEqual(self.errors(), '')
        observations.write_text(observations.read_text() + '\n')
        self.assertIn('checksum distinto', self.errors())

    def test_snapshot_cannot_pull_input_outside_its_directory(self):
        observations, manifest = self.snapshot()
        manifest['inputs'][0]['path'] = '../../outside.json'
        (observations.parent / 'manifest.json').write_text(json.dumps(manifest))
        self.assertIn('input fuera del estudio', self.errors())


if __name__ == '__main__':
    unittest.main()
