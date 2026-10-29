#!/usr/bin/env python3
"""Build the SpeechDesk manual as portable, dependency-free HTML pages."""
from pathlib import Path
import html
import json
import re
import shutil
import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
APP = 'https://github.com/Davoda1/Speech-Desk'
REPO = 'https://github.com/Davoda1/Speech-Desk-Manual'
PAGES = [
    ('Getting started', 'overview', 'Introduction', 'SpeechDesk manual'),
    ('Getting started', 'installation', 'Installation', 'Install SpeechDesk'),
    ('Getting started', 'first-reading', 'Your first reading', 'Your first reading'),
    ('Using SpeechDesk', 'playback', 'Text & playback', 'Text and playback'),
    ('Using SpeechDesk', 'dictation', 'Local dictation', 'Dictate on your computer'),
    ('Using SpeechDesk', 'providers', 'Speech providers', 'Connect a speech provider'),
    ('Using SpeechDesk', 'model-packs', 'Optional models', 'Install optional models'),
    ('Using SpeechDesk', 'settings', 'Settings', 'Settings and preferences'),
    ('Reference', 'shortcuts', 'Keyboard shortcuts', 'Keyboard shortcuts'),
    ('Reference', 'server-profiles', 'Advanced server profiles', 'Advanced server profiles'),
    ('Reference', 'troubleshooting', 'Troubleshooting', 'Troubleshooting'),
    ('Reference', 'privacy', 'Privacy & data', 'Privacy and data'),
    ('Reference', 'release-notes', 'Release notes', 'Release notes'),
]

def filename(slug):
    return 'index.html' if slug == 'overview' else slug + '.html'

def nav(current):
    parts=[];group=None
    for category,slug,label,title in PAGES:
        if category != group:
            if group is not None: parts.append('</ul>')
            parts.append(f'<p class="nav-heading">{category}</p><ul>');group=category
        active=' aria-current="page"' if slug==current else ''
        parts.append(f'<li><a href="{filename(slug)}"{active}>{html.escape(label)}</a></li>')
    parts.append('</ul>');return ''.join(parts)

SEARCH_ICON='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.8" cy="10.8" r="6.8"/><path d="m16 16 4.5 4.5"/></svg>'
THEME_ICON='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.4 1.4m11.2 11.2L19 19M5 19l1.4-1.4M17.6 6.4 19 5"/></svg>'

def build():
    OUT.mkdir(exist_ok=True)
    shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
    index=[]
    for position,(category,slug,label,title) in enumerate(PAGES):
        source=(ROOT/'content'/f'{slug}.md').read_text(encoding='utf-8')
        md=markdown.Markdown(extensions=['tables','fenced_code','toc'],extension_configs={'toc':{'permalink':False}})
        article=md.convert(source)
        # Tables retain semantic headers and scroll only within their own region.
        article=re.sub(r'(<table>.*?</table>)',r'<div class="table-scroll" tabindex="0">\1</div>',article,flags=re.S)
        article=re.sub(r'<p>', '<p class="lead">', article, count=1)
        headings=md.toc_tokens
        toc=''.join(f'<li><a href="#{h["id"]}">{html.escape(h["name"])}</a></li>' for h in headings)
        if not toc:toc='<li><a href="#main">Overview</a></li>'
        intro=re.sub('<[^>]+>',' ',article)
        intro=html.unescape(re.sub(r'\s+',' ',intro)).strip()
        desc=intro[:158].rsplit(' ',1)[0]+'.'
        index.append({'title':title,'label':label,'url':filename(slug),'text':intro,'headings':[{'title':html.unescape(h['name']),'url':filename(slug)+'#'+h['id']} for h in headings]})
        pager=[]
        for offset,caption in [(-1,'Previous'),(1,'Next')]:
            neighbor=position+offset
            if 0<=neighbor<len(PAGES):
                _,s,l,_=PAGES[neighbor]
                pager.append(f'<a class="{caption.lower()}" href="{filename(s)}"><span>{caption}</span><strong>{html.escape(l)} {"→" if offset==1 else ""}</strong></a>')
            else:pager.append('<span></span>')
        page=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · SpeechDesk</title>
<meta name="description" content="{html.escape(desc,quote=True)}">
<meta name="color-scheme" content="light dark">
<meta name="referrer" content="strict-origin-when-cross-origin">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/manual.css">
<script src="assets/theme.js"></script>
<script src="assets/search-index.js" defer></script><script src="assets/manual.js" defer></script>
</head>
<body data-page="{slug}">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
 <div class="header-inner">
  <a class="brand" href="index.html" aria-label="SpeechDesk manual home"><img src="assets/favicon.svg" width="30" height="30" alt=""><span>SpeechDesk</span></a>
  <span class="header-divider" aria-hidden="true"></span><span class="site-label">Manual</span>
  <nav class="header-links" aria-label="Project"><a href="{APP}/releases/tag/v1.0.0" aria-label="Download SpeechDesk 1.0.0">Downloads <span aria-hidden="true">↗</span></a><a href="{APP}">GitHub <span aria-hidden="true">↗</span></a></nav>
  <button class="icon-button mobile-search search-trigger" aria-label="Search manual">{SEARCH_ICON}</button>
  <button class="icon-button theme-toggle" aria-label="Change color theme" title="Change color theme">{THEME_ICON}</button>
 </div>
</header>
<div class="manual-layout">
 <aside class="sidebar" aria-label="Manual navigation">
  <button class="search-trigger search-button">{SEARCH_ICON}<span>Search manual</span><kbd>/</kbd></button>
  <nav aria-label="Chapters">{nav(slug)}</nav>
  <div class="sidebar-meta"><span class="version-label">Version 1.0.0</span><span>Windows &amp; Linux</span></div>
 </aside>
 <div class="mobile-navigation"><details><summary>Browse manual <span>{html.escape(label)}</span></summary><nav aria-label="Mobile chapters">{nav(slug)}</nav></details></div>
 <main id="main" tabindex="-1">
  <div class="breadcrumb"><a href="index.html">Manual</a><span aria-hidden="true">/</span><span>{category}</span></div>
  <article><header class="article-header"><p class="edition">SpeechDesk 1.0.0</p><h1>{title}</h1></header>{article}</article>
  <nav class="page-navigation" aria-label="Adjacent chapters">{''.join(pager)}</nav>
  <footer class="article-footer"><span>SpeechDesk documentation · © 2026 davoda1</span><a href="{REPO}/blob/master/content/{slug}.md">View page source <span aria-hidden="true">↗</span></a></footer>
 </main>
 <aside class="page-outline" aria-label="On this page"><div><p>On this page</p><ul>{toc}</ul><a class="help-link" href="troubleshooting.html">Need help?</a><a class="outline-source" href="{APP}/issues">Report an issue ↗</a></div></aside>
</div>
<dialog id="search-dialog" aria-labelledby="search-title">
 <div class="search-heading"><h2 id="search-title">Search the manual</h2><button class="dialog-close" aria-label="Close search">Esc</button></div>
 <div class="search-input-wrap">{SEARCH_ICON}<input id="search-input" type="search" placeholder="Search topics, settings, shortcuts…" autocomplete="off" aria-label="Search manual pages" aria-controls="search-results"></div>
 <p id="search-status" aria-live="polite">Type a topic to find a page.</p><ul id="search-results"></ul>
 <div class="search-footer">Search runs in your browser. No queries are sent.</div>
</dialog>
<div id="toast" role="status" aria-live="polite"></div>
</body></html>'''
        (OUT/filename(slug)).write_text(page,encoding='utf-8')
    (OUT/'assets/search-index.js').write_text('window.MANUAL_SEARCH = '+json.dumps(index,ensure_ascii=False)+';\n',encoding='utf-8')
    (OUT/'.nojekyll').write_text('')
    # A useful error page also works on hosts that serve custom 404 documents.
    (OUT/'404.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found · SpeechDesk</title><style>body{font:18px/1.6 system-ui;max-width:38rem;margin:12vh auto;padding:24px;color:#252a31}a{color:#175dae}</style><h1>Page not found</h1><p>This address does not match a manual page.</p><p><a href="index.html">Open the SpeechDesk manual</a></p></html>''',encoding='utf-8')
    print(f'Built {len(PAGES)} manual pages in {OUT}')

if __name__=='__main__':build()
