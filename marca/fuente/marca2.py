"""Gabinete Contable · marca v3: búho-plumilla + Bodoni Moda."""
import logo_kit as lk
import fuentes
from nib import owl, silhouette

fuentes.asegurar()

PET, PETD, HUE, TIN, ORO, NIE, WHITE = "#134150", "#0E2F3A", "#F4F0E8", "#14252B", "#C2A36B", "#5C6E75", "#FFFFFF"
FS = "node_modules/@fontsource"
def font(fam, w): return f"{FS}/{fam}/files/{fam}-latin-{w}-normal.woff2"
F_DISPLAY = "fonts/bodoni-op18-w500.ttf"   # corte display: logo principal
F_TEXT = "fonts/bodoni-op11-w600.ttf"      # corte texto: tamaños pequeños
SANS = font("jost", 400)

GEOM = dict(eye="ring", rim=4.2, er=15.5, dip=18, shoulder=(104, 80), taper=(70, 124))
SYM = owl(**GEOM)
_by, _bw, _bh = 64, 5, 7
JEWEL = lk.polygon([(50, _by - _bh), (50 + _bw, _by), (50, _by + _bh), (50 - _bw, _by)])  # pico / respiradero en oro
# reducido (16-24 px): sin ranura, aros más gruesos, pico más grande
SMALL = owl(eye="ring", rim=6, er=17, ex=29, dip=18, shoulder=(104, 80), taper=(70, 124), slit=False, beak=(66, 7, 9))
X = 100 / 12  # módulo: 1/12 del ancho

def line(s, tracking, size=100, f=None):
    p, m = lk.text(f or F_DISPLAY, s, size=size, tracking=tracking)
    return p, m

def width(p): b = lk.bounds(p); return b[2] - b[0]

def block(size=100, lead=1.34, t1=150, f=None):
    """GABINETE / CONTABLE a igual ancho: CONTABLE ajusta su tracking."""
    g, m = line("GABINETE", t1, size, f)
    target = width(g)
    lo, hi = -100, 400
    for _ in range(40):
        mid = (lo + hi) / 2
        c, _ = line("CONTABLE", mid, size, f)
        if width(c) < target: lo = mid
        else: hi = mid
    c, _ = line("CONTABLE", (lo + hi) / 2, size, f)
    g = lk.move(g, -lk.bounds(g)[0], 0)
    c = lk.move(c, -lk.bounds(c)[0], lead * size)
    return lk.union(g, c), m, (lo + hi) / 2

WB, WM, T2 = block()
WBS, _, _ = block(t1=170, f=F_TEXT)
CAP = WM["cap_height"]

def place_vertical(sym_h=150, text_w=None, gap=None):
    sb = lk.bounds(SYM)
    tw = text_w or (sb[2] - sb[0]) / 0.34
    s = tw / width(WB)
    w = lk.scale(WB, s)
    b = lk.bounds(w)
    gap = gap or 3 * X
    return lk.move(w, (sb[0] + sb[2]) / 2 - (b[0] + b[2]) / 2, sb[3] + gap - b[1])

def place_horizontal():
    """Corte texto; bloque centrado en el centro óptico del búho (y = 60)."""
    sb = lk.bounds(SYM)
    # el bloque de texto ocupa la altura de la cabeza (penachos a pico)
    th = 0.44 * (sb[3] - sb[1])
    s = th / (lk.bounds(WBS)[3] - lk.bounds(WBS)[1])
    w = lk.scale(WBS, s)
    b = lk.bounds(w)
    return lk.move(w, sb[2] + 3 * X - b[0], 60 - th / 2 - b[1])

WV = place_vertical()
WH = place_horizontal()

def layers(word, scheme):
    ink, sym = {"color": (PET, PET), "negativo": (HUE, ORO), "oro": (ORO, ORO), "tinta": (TIN, TIN),
                "hueso": (HUE, HUE), "blanco": (WHITE, WHITE)}[scheme]
    L = [(SYM, sym)]
    if scheme == "color": L.append((JEWEL, ORO))
    if word is not None: L.append((word, ink))
    return L
