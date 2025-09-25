#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / 'scripts' / 'publications.csv'
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

def main():
  OUT_DIR.mkdir(parents=True, exist_ok=True)
  with CSV_PATH.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
      year = row.get('year', '').strip() or '0000'
      title = row.get('title', 'untitled').strip()
      slug = f"{year}-{slugify(title)[:50]}"
      md = TEMPLATE.format(
        title=title,
        authors=row.get('authors', ''),
        venue=row.get('venue', ''),
        year=year,
        abstract=row.get('abstract', '').replace('\n', '\n  '),
        pdf=row.get('pdf', ''),
        code=row.get('code', ''),
        doi=row.get('doi', ''),
      )
      (OUT_DIR / f"{slug}.md").write_text(md)
  print(f"Generated markdown files in {OUT_DIR}")

if __name__ == '__main__':
  main()


