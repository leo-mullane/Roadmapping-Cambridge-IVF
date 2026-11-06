#!/usr/bin/env python3
"""Builds the findings report pages into src/report/ from report-src/.

- report-src/report.md      -> src/report/index.html (the findings report)
- report-src/ideas.html     -> src/report/ideas.html (all 43 ideas, filterable, payback calculator)
- report-src/design-system.html -> src/report/design-system.html
The Word version lives at src/assets/cambridge-ivf-website-findings-and-ideas.docx.

    python3 tools/build_report.py && python3 tools/quick_wins.py && node build-includes.js && node validate.js
"""
import json, os, re
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'report-src')
OUT = os.path.join(ROOT, 'src', 'report')
DOCX = '../assets/cambridge-ivf-website-findings-and-ideas.docx'

# Links that pointed at Claude-hosted copies now point inside this repository.
RELINK = {
    'https://claude.ai/artifact/Kmv3jsjWSrXxN2xDhboYfL': '../index.html',
    'https://claude.ai/artifact/4wSxQavT4ERFQSL34fVicE': 'ideas.html',
    'https://claude.ai/artifact/7EtJavHXqrG74wQfCKuxx4': 'design-system.html',
}

STRIP_CSS = '''<style>
.rp-strip{background:#7C2855;font-family:"Frutiger W01","Hind",Arial,sans-serif;position:relative;z-index:50}
.rp-strip .in{max-width:1280px;margin:0 auto;padding:0 20px;display:flex;gap:4px;flex-wrap:wrap}
.rp-strip a{color:#fff;text-decoration:none;font-weight:700;font-size:15px;padding:9px 12px;border-bottom:3px solid transparent}
.rp-strip a[aria-current=page]{border-bottom-color:#fff}
.rp-strip a:hover{background:#551C3B}
.rp-strip a:focus{background:#75EDFF;color:#212B32;outline:4px solid transparent}
</style>'''


def strip(current):
    items = [('index.html', 'Findings report'), ('ideas.html', 'All 43 ideas'), ('design-system.html', 'Design system'), ('../index.html', 'Prototypes'), ('../quick-wins/index.html', 'Quick wins')]
    links = ''.join(f'<a href="{h}"{" aria-current=page" if h == current else ""}>{t}</a>' for h, t in items)
    return f'<nav class="rp-strip" aria-label="Report and prototypes"><div class="in">{links}</div></nav>'


INLINE = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\))')


def inline(text):
    out = ''
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith('**') and part.endswith('**'):
            out += f'<strong>{escape(part[2:-2])}</strong>'
        elif part.startswith('*') and part.endswith('*') and len(part) > 1:
            out += f'<em>{escape(part[1:-1])}</em>'
        else:
            m = re.match(r'^\[([^\]]+)\]\(([^)]+)\)$', part)
            if m:
                url = RELINK.get(m.group(2), m.group(2))
                out += f'<a href="{escape(url)}">{escape(m.group(1))}</a>'
            else:
                out += escape(part)
    return out


def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')


def qw_table():
    qws = json.load(open(os.path.join(ROOT, 'data', 'quick-wins.json')))
    ideas = {i['n']: i for i in json.load(open(os.path.join(ROOT, 'data', 'ideas.json')))}
    rows = ['| QW | Quick win | Who does it | Payback |', '|---|---|---|---|']
    for q in qws:
        i = ideas[q['idea']]
        rows.append(f"| [QW{q['qw']}](../quick-wins/{q['slug']}.html) | **{q['title']}** {q['summary']} | {i['route']} | {'£' * i['roi']} |")
    return '\n'.join(rows)


def md_to_html(md):
    md = md.replace('{{QW_TABLE}}', qw_table())
    lines = md.splitlines()
    html, toc, i = [], [], 0
    title = ''
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1; continue
        if ln.startswith('# '):
            title = ln[2:]; i += 1; continue
        if ln.startswith('### '):
            html.append(f'<h3 id="{slug(ln[4:])}">{inline(ln[4:])}</h3>'); i += 1; continue
        if ln.startswith('## '):
            t = ln[3:]; toc.append((slug(t), t))
            html.append(f'</section><section class="rp-sec" id="{slug(t)}"><h2>{inline(t)}</h2>'); i += 1; continue
        if ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            head = ''.join(f'<th scope="col">{inline(c)}</th>' for c in rows[0])
            body = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows[1:])
            cls = ' wide' if len(rows[0]) >= 7 else ''
            html.append(f'<div class="rp-table{cls}"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
            continue
        if ln.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(f'<li>{inline(lines[i][2:])}</li>'); i += 1
            html.append('<ul>' + ''.join(items) + '</ul>'); continue
        if re.match(r'^\d+\. ', ln):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                items.append(f'<li>{inline(re.sub(r"^\d+\. ", "", lines[i]))}</li>'); i += 1
            html.append('<ol>' + ''.join(items) + '</ol>'); continue
        html.append(f'<p>{inline(ln)}</p>'); i += 1
    body = '\n'.join(html)
    body = body.replace('</section>', '', 1) + '</section>'
    return title, toc, body


def write_report():
    title, toc, body = md_to_html(open(os.path.join(SRC, 'report.md'), encoding='utf-8').read())
    toc_html = ''.join(f'<li><a href="#{s}">{escape(t)}</a></li>' for s, t in toc)
    page = f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cambridge IVF: website findings, ideas and how to do them</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hind:wght@400;600;700&display=swap">
<link rel="stylesheet" href="../css/report.css">
{STRIP_CSS}
</head>
<body>
<a class="rp-skip" href="#main">Skip to content</a>
{strip('index.html')}
<header class="rp-hero"><div class="rp-wrap">
  <p class="rp-eyebrow">Cambridge IVF</p>
  <h1>{escape(title)}</h1>
  <p class="rp-lead">What we found on cambridge-ivf.nhs.uk, how five competitors handle the same things, the five bigger improvements and 22 quick wins, and how the clinic could make them itself.</p>
  <div class="rp-actions"><a class="rp-btn" href="../index.html">Open the prototypes</a><a class="rp-btn rp-btn-2" href="ideas.html">See all 43 ideas</a><a class="rp-btn rp-btn-2" href="{DOCX}">Download as Word</a></div>
</div></header>
<div class="rp-wrap rp-layout">
  <nav class="rp-toc" aria-label="Contents"><p class="rp-eyebrow">Contents</p><ol>{toc_html}</ol></nav>
  <main id="main" class="rp-main">
{body}
  </main>
</div>
<footer class="rp-foot"><div class="rp-wrap">Findings from the live sites and the HFEA's public data. Prices as published on cambridge-ivf.nhs.uk.</div></footer>
</body>
</html>
'''
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)


def write_copy(name, current):
    s = open(os.path.join(SRC, name), encoding='utf-8').read()
    for a, b in RELINK.items():
        s = s.replace(a, b)
    s = s.replace('</head>', STRIP_CSS + '\n</head>', 1)
    s = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + strip(current), s, count=1)
    # The sticky section header on these pages sits below the strip, not on top of it.
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write(s)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    write_report()
    write_copy('ideas.html', 'ideas.html')
    write_copy('design-system.html', 'design-system.html')
    print('Wrote src/report/index.html, ideas.html and design-system.html')
