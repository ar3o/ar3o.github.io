"""Builds clean-tables/index.html from the project README (images copied from the repo). Run after editing the README."""
import re, shutil
from pathlib import Path
import markdown

REPO = Path("/home/archie/my_isaac_projects/androids-dream-of-clean-tables")
OUT = Path(__file__).parent / "clean-tables"
src = (REPO / "README.md").read_text()
src = re.sub(r"<p align=\"center\"><b>Live write-up:</b>.*?</p>\n", "", src, flags=re.S)
body = markdown.markdown(src, extensions=["tables", "md_in_html", "fenced_code"])
body = body.replace('href="docs/', 'href="https://github.com/ar3o/can-androids-dream-of-clean-tables/blob/main/docs/')
body = body.replace('href="LICENSE"', 'href="https://github.com/ar3o/can-androids-dream-of-clean-tables/blob/main/LICENSE"')
if (OUT / "assets").exists():
    shutil.rmtree(OUT / "assets")
shutil.copytree(REPO / "assets", OUT / "assets")
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Can Androids Dream of Clean Tables?</title><link rel="stylesheet" href="../style.css"></head><body><main>
<nav><a href="../">Archie McMurray</a> / Can Androids Dream of Clean Tables? · <a href="https://github.com/ar3o/can-androids-dream-of-clean-tables">code on GitHub</a></nav>
<p class="note">This page is the living version of the project write-up. I'm continuing the work after the challenge deadline, and new results land here first.</p>
<article>{body}</article></main></body></html>"""
(OUT / "index.html").write_text(html)
print("built", OUT / "index.html")
