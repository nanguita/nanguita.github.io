# Academic Pages-like Jekyll Site

This repository contains a Jekyll-based academic website inspired by Academic Pages. It provides sections for publications, talks, teaching, portfolio, and a blog.

## Prerequisites
- Ruby (>= 2.7) and Bundler: `gem install bundler`

## Local development
```bash
bundle install
bundle exec jekyll serve
```
Then open `http://localhost:4000`.

## GitHub Pages deployment
- For a user/organization site: name repo `username.github.io` and push `main`.
- For a project site: use any repo name, set `baseurl` in `_config.yml`.
- Enable GitHub Pages in repository settings (Source: GitHub Actions or `main` branch). For Actions, use the Jekyll workflow template.

## Content structure
- `_publications`: markdown with YAML frontmatter (title, authors, venue, year, abstract, pdf, code, doi)
- `_talks`: talks (title, event, location, date)
- `_teaching`: courses (title, course, term, role)
- `_portfolio`: projects (title, tags)
- `_posts`: classic Jekyll posts
- `_pages`: additional pages like `about`

## Configuration
- `_config.yml`: site title, author info, collections, plugins, theme options
- `_data/navigation.yml`: main nav
- `site_theme`: `default` or `air`
- `dark_mode`: theme toggle
- `mathjax`, `mermaid`, `plotly`: embed support

## Customization
- Replace `assets/img/profile.jpg` with your photo
- Edit `author` block in `_config.yml`
- Adjust styles in `assets/css/main.scss` and `_sass/_variables.scss`

## Optional: generate publications from CSV
Place a CSV at `scripts/publications.csv` with columns: `title,authors,venue,year,abstract,pdf,code,doi`. Then run:
```bash
python3 scripts/generate_publications.py
```
It will create markdown files in `_publications/`.

## Optional: generate publications from BibTeX
Place a BibTeX file at `scripts/publications.bib`, then run:
```bash
python3 scripts/generate_publications_bibtex.py
```
This will create markdown files in `_publications/`.

## License
MIT
