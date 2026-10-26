"""Offline package verification. Run with Python 3.9+; no external dependencies."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def contained(relative):
    path = (ROOT / relative).resolve()
    if ROOT.resolve() not in path.parents:
        raise ValueError('Path outside plugin: ' + relative)
    return path


def check_hash(path, expected, text=False):
    data = path.read_text(encoding='utf-8').encode('utf-8') if text else path.read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('Hash mismatch: ' + str(path.relative_to(ROOT)))


def main():
    manifest = json.loads((ROOT / 'knowledge-manifest.json').read_text(encoding='utf-8'))
    entries = manifest['skills']
    for resource in manifest.get('runtime_files', []):
        check_hash(contained(resource['path']), resource['text_sha256'], text=True)
    assert len(entries) == 31
    assert len({e['skill'] for e in entries}) == 31
    count, links = 0, 0
    docs = [ROOT / 'references/catalogo.md', ROOT / 'references/execucao.md']
    for entry in entries:
        folder = contained('skills/' + entry['skill'])
        skill = folder / 'SKILL.md'
        text = skill.read_text(encoding='utf-8')
        assert text.startswith('---\n') and '\nname: ' + entry['skill'] + '\n' in text
        description = json.loads(next(line[13:] for line in text.splitlines() if line.startswith('description: ')))
        assert 0 < len(description) <= 1024 and not re.search('[<>]', description)
        check_hash(folder / 'references/instrucoes-originais.md', entry['original_instruction_sha256'])
        check_hash(folder / 'references/instrucoes.md', entry['active_instruction_sha256'], text=True)
        docs += [skill, folder / 'references/instrucoes.md', folder / 'references/bases.md']
        for attachment in entry['attachments']:
            original = contained('skills/' + entry['skill'] + '/' + attachment['original_copy'])
            consultation = contained('skills/' + entry['skill'] + '/' + attachment['path'])
            check_hash(original, attachment['sha256'])
            check_hash(consultation, attachment['consultation_sha256'], text=True)
            assert consultation.read_text(encoding='utf-8').strip()
            count += 1
    assert count == 63
    docs += list((ROOT / 'skills/funcionarios/references').glob('*atual*.md'))
    for path in docs:
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if target.startswith(('http://', 'https://', '#')):
                continue
            resolved = (path.parent / target).resolve()
            assert ROOT.resolve() in resolved.parents and resolved.is_file(), (path, target)
            links += 1
    for relative in ['plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json']:
        data = json.loads((ROOT / relative).read_text(encoding='utf-8'))
        assert data['version'] == manifest['version']
        assert data['name'] == 'funcionarios-do-futuro'
    for path in ROOT.rglob('*'):
        if not path.is_file() or '__pycache__' in path.parts:
            continue
        relative = path.relative_to(ROOT).as_posix()
        assert re.fullmatch('[A-Za-z0-9._/-]+', relative), relative
        prefix = 'C:/Users/Ciro/.claude/plugins/marketplaces/ciro-rosa-funcionarios-do-futuro-plugin..clone/funcionarios-do-futuro/'
        assert len(prefix + relative) <= 240, relative
    print(json.dumps({'version': manifest['version'], 'skills': len(entries),
                      'original_attachments': count, 'readable_references': count,
                      'links': links, 'status': 'ok'}))


if __name__ == '__main__':
    main()
