"""logo_kit.py — construir logos vectoriales con acabado profesional."""
import io, math
import pathops
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path

K = 0.5522847498

def _load(font_path):
    f = TTFont(font_path)
    f.flavor = None
    buf = io.BytesIO(); f.save(buf)
    return TTFont(io.BytesIO(buf.getvalue())), buf.getvalue()

def text(font_path, s, size=100, tracking=0, kern=None, features=None):
    font, data = _load(font_path)
    upem = font["head"].unitsPerEm
    face = hb.Face(data); hbf = hb.Font(face)
    buf = hb.Buffer(); buf.add_str(s); buf.guess_segment_properties()
    hb.shape(hbf, buf, features or {"kern": True, "liga": True})
    glyphs, order = font.getGlyphSet(), font.getGlyphOrder()
    sc, x, kern = size / upem, 0.0, kern or {}
    out, boxes = pathops.Path(), []
    n = len(buf.glyph_infos)
    for i, (inf, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        g = pathops.Path()
        glyphs[order[inf.codepoint]].draw(TransformPen(g.getPen(glyphSet=glyphs), (sc, 0, 0, -sc, (x + pos.x_offset) * sc, -pos.y_offset * sc)))
        boxes.append(g.bounds)
        out.addPath(g)
        x += pos.x_advance
        if i < n - 1:
            x += (tracking + kern.get(i, 0)) * upem / 1000
    os2 = font["OS/2"]
    m = {"width": x * sc, "boxes": boxes,
         "x_height": getattr(os2, "sxHeight", 0) * sc, "cap_height": getattr(os2, "sCapHeight", 0) * sc,
         "ascender": font["hhea"].ascent * sc, "descender": font["hhea"].descent * sc}
    return clean(out), m

def circle(cx, cy, r):
    p = pathops.Path(); k = K * r
    p.moveTo(cx + r, cy)
    p.cubicTo(cx + r, cy + k, cx + k, cy + r, cx, cy + r)
    p.cubicTo(cx - k, cy + r, cx - r, cy + k, cx - r, cy)
    p.cubicTo(cx - r, cy - k, cx - k, cy - r, cx, cy - r)
    p.cubicTo(cx + k, cy - r, cx + r, cy - k, cx + r, cy)
    p.close(); return p

def rect(x, y, w, h, r=0):
    p = pathops.Path(); r = min(r, w / 2, h / 2); k = K * r
    if r == 0:
        p.moveTo(x, y); p.lineTo(x + w, y); p.lineTo(x + w, y + h); p.lineTo(x, y + h); p.close(); return p
    p.moveTo(x + r, y); p.lineTo(x + w - r, y)
    p.cubicTo(x + w - r + k, y, x + w, y + r - k, x + w, y + r); p.lineTo(x + w, y + h - r)
    p.cubicTo(x + w, y + h - r + k, x + w - r + k, y + h, x + w - r, y + h); p.lineTo(x + r, y + h)
    p.cubicTo(x + r - k, y + h, x, y + h - r + k, x, y + h - r); p.lineTo(x, y + r)
    p.cubicTo(x, y + r - k, x + r - k, y, x + r, y); p.close(); return p

def polygon(pts):
    p = pathops.Path(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    p.close(); return p

def from_svg(d):
    p = pathops.Path(); parse_path(d, p.getPen()); return p

def union(*ps):
    out = ps[0]
    for q in ps[1:]: out = pathops.op(out, q, pathops.PathOp.UNION, fix_winding=True)
    return out

def diff(a, *bs):
    for b in bs: a = pathops.op(a, b, pathops.PathOp.DIFFERENCE, fix_winding=True)
    return a

def inter(a, b):
    return pathops.op(a, b, pathops.PathOp.INTERSECTION, fix_winding=True)

def clean(p):
    return pathops.simplify(p, fix_winding=True)

def transform(p, a=1, b=0, c=0, d=1, e=0, f=0):
    out = pathops.Path(); p.draw(TransformPen(out.getPen(), (a, b, c, d, e, f))); return out

def move(p, dx, dy): return transform(p, e=dx, f=dy)
def scale(p, s, cx=0, cy=0): return transform(p, s, 0, 0, s, cx - s * cx, cy - s * cy)
def rotate(p, deg, cx=0, cy=0):
    t = math.radians(deg); co, si = math.cos(t), math.sin(t)
    return transform(p, co, si, -si, co, cx - co * cx + si * cy, cy - si * cx - co * cy)

def stroke(p, w, cap="round", join="round"):
    caps = {"round": pathops.LineCap.ROUND_CAP, "butt": pathops.LineCap.BUTT_CAP, "square": pathops.LineCap.SQUARE_CAP}
    joins = {"round": pathops.LineJoin.ROUND_JOIN, "miter": pathops.LineJoin.MITER_JOIN, "bevel": pathops.LineJoin.BEVEL_JOIN}
    q = transform(p); q.stroke(w, caps[cap], joins[join], 4); q.convertConicsToQuads()
    return clean(q)

def soften(p, r):
    er = diff(p, stroke(p, 2 * r))
    return union(er, stroke(er, 2 * r))

def bounds(p): return p.bounds

def lockup(symbol, word, m, gap, baseline=None, vertical=False, band="x"):
    sb, wb = bounds(symbol), bounds(word)
    if vertical:
        return move(word, (sb[0] + sb[2]) / 2 - (wb[0] + wb[2]) / 2, sb[3] + gap - wb[1])
    h = m["cap_height"] if band == "cap" else m["x_height"]
    return move(word, sb[2] + gap - wb[0], baseline if baseline is not None else (sb[1] + sb[3]) / 2 + h / 2)

def d(p, nd=2):
    pen = SVGPathPen(None, ntos=lambda v: ("%.*f" % (nd, v)).rstrip("0").rstrip("."))
    p.draw(pen); return pen.getCommands()

def svg(layers, pad=0, title="logo", box=None):
    xs = [bounds(p) for p, _ in layers]
    x0, y0 = min(b[0] for b in xs) - pad, min(b[1] for b in xs) - pad
    x1, y1 = max(b[2] for b in xs) + pad, max(b[3] for b in xs) + pad
    if box: x0, y0, x1, y1 = box
    body = "".join(f'<path fill="{c}" d="{d(p)}"/>' for p, c in layers)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.2f} {y0:.2f} {x1 - x0:.2f} {y1 - y0:.2f}">'
            f"<title>{title}</title>{body}</svg>")

def contrast(c1, c2):
    def lum(h):
        h = h.lstrip("#"); h = "".join(ch * 2 for ch in h) if len(h) == 3 else h
        v = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        v = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in v]
        return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]
    a, b = sorted((lum(c1), lum(c2)), reverse=True)
    return round((a + 0.05) / (b + 0.05), 2)

def render(html, png, width=1600, scale=2, transparent=False, selector=None, height=100):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        try: b = pw.chromium.launch()
        except Exception: b = pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = b.new_page(viewport={"width": width, "height": height}, device_scale_factor=scale)
        if not html.lstrip().lower().startswith("<!doctype"): html = "<!DOCTYPE html>" + html
        pg.set_content(html); pg.wait_for_timeout(200)
        if selector: pg.locator(selector).first.screenshot(path=png, omit_background=transparent)
        else: pg.screenshot(path=png, full_page=True, omit_background=transparent)
        b.close()

def export_png(svg_str, png, width=1024):
    tag = '<svg width="%d" ' % width
    render("<html><body style='margin:0'>" + svg_str.replace("<svg ", tag, 1) + "</body></html>",
           png, width=width, scale=1, transparent=True, selector="svg")
