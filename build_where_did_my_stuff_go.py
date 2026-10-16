"""Builds where-did-my-stuff-go/index.html from the project README (images copied from the repo). Run after editing the README."""
import re, shutil
from pathlib import Path
import markdown

REPO = Path("/home/archie/my_isaac_projects/what-changed-in-the-room")
GH = "https://github.com/ar3o/where-did-my-stuff-go"
OUT = Path(__file__).parent / "where-did-my-stuff-go"
src = (REPO / "README.md").read_text()
src = re.sub(r"<p align=\"center\"><b>Live write-up:</b>.*?</p>\n", "", src, flags=re.S)
src = src.replace("<details>", '<details markdown="1">')   # let md_in_html parse the collapsed sections
body = markdown.markdown(src, extensions=["tables", "md_in_html", "fenced_code"])
body = re.sub(r'href="((?:docs|examples)/[^"]*)"', lambda m: f'href="{GH}/blob/main/{m.group(1)}"', body)
body = body.replace('href="LICENSE"', f'href="{GH}/blob/main/LICENSE"')
OUT.mkdir(exist_ok=True)
if (OUT / "assets").exists():
    shutil.rmtree(OUT / "assets")
shutil.copytree(REPO / "assets", OUT / "assets")
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Where did my stuff go</title><link rel="stylesheet" href="../style.css"></head><body><main>
<nav><a href="../">Archie McMurray</a> / Where did my stuff go · <a href="{GH}">code on GitHub</a></nav>
<p class="note">This page is the living version of the project write-up. I'm continuing the work after the challenge deadline, and new results land here first.</p>
<article>{body}</article></main></body></html>"""
(OUT / "index.html").write_text(html)
print("built", OUT / "index.html")
