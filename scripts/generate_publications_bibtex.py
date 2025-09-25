#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / 'scripts' / 'publications.bib'
OUT_DIR = ROOT / '_publications'

TEMPLATE = """---
title: {title}
authors: {authors}
venue: {venue}
year: {year}
abstract: |
  {abstract}
pdf: {pdf}
code: {code}
doi: {doi}
---

"""

def slugify(text: str) -> str:
  return ''.join(c.lower() if c.isalnum() else '-' for c in text).strip('-')

def parse_bibtex(content: str):
  entries = []
  buf = []
  level = 0
  for line in content.splitlines():
    if line.strip().startswith('@') and level == 0:
      if buf:
        entries.append('\n'.join(buf))
        buf = []
    buf.append(line)
    level += line.count('{') - line.count('}')
  if buf:
    entries.append('\n'.join(buf))
  result = []
  for e in entries:
    fields = {}
    for line in e.splitlines():
      if '=' in line:
        k, v = line.split('=', 1)
        k = k.strip().strip(',').lower()
        v = v.strip().strip(',').strip('{}').strip()
        fields[k] = v
    result.append(fields)
  return result

def main():
  OUT_DIR.mkdir(parents=True, exist_ok=True)
  if not BIB_PATH.exists():
    print(f"Missing {BIB_PATH}")
    return
  content = BIB_PATH.read_text()
  for entry in parse_bibtex(content):
    title = entry.get('title', 'untitled')
    authors = entry.get('author', '')
    venue = entry.get('booktitle', '') or entry.get('journal', '')
    year = entry.get('year', '0000')
    abstract = entry.get('abstract', '')
    pdf = entry.get('url', '')
    doi = entry.get('doi', '')
    code = ''
    slug = f"{year}-{slugify(title)[:50]}"
    md = TEMPLATE.format(
      title=title,
      authors=authors,
      venue=venue,
      year=year,
      abstract=abstract.replace('\n', '\n  '),
      pdf=pdf,
      code=code,
      doi=doi,
    )
    (OUT_DIR / f"{slug}.md").write_text(md)
  print(f"Generated markdown files in {OUT_DIR}")

if __name__ == '__main__':
  main()


