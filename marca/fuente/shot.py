"""Render de HTML con fuentes locales (file://) a PNG."""
import os
from playwright.sync_api import sync_playwright
HERE = os.path.abspath(os.path.dirname(__file__))
FONTCSS = f"""
@font-face{{font-family:'Bricolage Grotesque';font-weight:600;src:url('file://{HERE}/node_modules/@fontsource/bricolage-grotesque/files/bricolage-grotesque-latin-600-normal.woff2')}}
@font-face{{font-family:'Bricolage Grotesque';font-weight:700;src:url('file://{HERE}/node_modules/@fontsource/bricolage-grotesque/files/bricolage-grotesque-latin-700-normal.woff2')}}
@font-face{{font-family:'Hanken Grotesk';font-weight:400;src:url('file://{HERE}/node_modules/@fontsource/hanken-grotesk/files/hanken-grotesk-latin-400-normal.woff2')}}
@font-face{{font-family:'Hanken Grotesk';font-weight:600;src:url('file://{HERE}/node_modules/@fontsource/hanken-grotesk/files/hanken-grotesk-latin-600-normal.woff2')}}
@font-face{{font-family:'Hanken Grotesk';font-weight:700;src:url('file://{HERE}/node_modules/@fontsource/hanken-grotesk/files/hanken-grotesk-latin-700-normal.woff2')}}
@font-face{{font-family:'Bodoni Moda';font-weight:400 900;src:url('file://{HERE}/node_modules/@fontsource-variable/bodoni-moda/files/bodoni-moda-latin-standard-normal.woff2')}}
@font-face{{font-family:'Jost';font-weight:400;src:url('file://{HERE}/node_modules/@fontsource/jost/files/jost-latin-400-normal.woff2')}}
@font-face{{font-family:'Jost';font-weight:500;src:url('file://{HERE}/node_modules/@fontsource/jost/files/jost-latin-500-normal.woff2')}}
*{{box-sizing:border-box}} body{{margin:0}}
"""
def shot(html, png, width, height, scale=2, transparent=False):
    fn = os.path.join(HERE, "_tmp_render.html")
    if "<style>" in html: html = html.replace("<style>", "<style>" + FONTCSS, 1)
    else: html = html.replace("<head>", "<head><style>" + FONTCSS + "</style>", 1)
    open(fn, "w").write("<!DOCTYPE html>" + html)
    with sync_playwright() as pw:
        try: b = pw.chromium.launch()
        except Exception: b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = b.new_page(viewport={"width": width, "height": height}, device_scale_factor=scale)
        pg.goto("file://" + fn); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(250)
        pg.screenshot(path=png, omit_background=transparent, clip={"x": 0, "y": 0, "width": width, "height": height})
        b.close()
