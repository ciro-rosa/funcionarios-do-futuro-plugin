"""Deterministic output checks; stdin or --file. No network or writes."""
import argparse
import csv
import io
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('kind', choices=['texto', 'json-video', 'csv-reels'])
    parser.add_argument('--file', type=Path)
    parser.add_argument('--limit', type=int, default=150)
    parser.add_argument('--rows', type=int, default=7)
    options = parser.parse_args()
    if options.file:
        text = options.file.read_text(encoding='utf-8-sig')
    else:
        raw = sys.stdin.buffer.read()
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            text = raw.decode('cp1252')
        text = text.replace('\r\n', '\n')
    if options.kind == 'texto':
        # Remove only a terminal newline introduced by a shell pipe.
        if text.endswith('\n'):
            text = text[:-1]
        result = {'characters': len(text), 'limit': options.limit, 'within_limit': len(text) <= options.limit}
    elif options.kind == 'json-video':
        data = json.loads(text)
        duration = data['timing']['duration_seconds']
        assert isinstance(duration, (int, float)) and not isinstance(duration, bool) and 0 < duration <= 8
        assert data['aspect_ratio'] in ['9:16', '16:9']
        assert data['mode'] in ['text_to_video', 'frame_to_video']
        assert all(data['constraints'][k] is True for k in ['single_take', 'no_cuts', 'no_zoom'])
        assert {'no subtitles', 'no text overlays'} <= set(data['negative_prompts'])
        timeline = data['timeline']
        end = 0
        for beat in timeline:
            assert beat['start'] == end and beat['end'] > beat['start']
            end = beat['end']
        assert end == duration
        assert len(text) <= 8000
        result = {'valid': True, 'aspect_ratio': data['aspect_ratio'], 'duration_seconds': duration}
    else:
        rows = [row for row in csv.reader(io.StringIO(text)) if row]
        assert len(rows) == options.rows + 1 and all(len(row) == 4 for row in rows)
        result = {'valid': True, 'data_rows': len(rows) - 1, 'columns': 4}
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
