"""Gabinete Contable · identidad: la mirada del búho + Bodoni Moda."""
import logo_kit as lk
import fuentes
from eyes import ring, C

fuentes.asegurar()
PET, PETD, HUE, TIN, ORO, NIE, WHITE = "#134150", "#0E2F3A", "#F4F0E8", "#14252B", "#C2A36B", "#5C6E75", "#FFFFFF"
F_DISPLAY = "fonts/bodoni-op18-w500.ttf"
F_TEXT = "fonts/bodoni-op11-w600.ttf"

R, GAP = 36, 8            # radio del ojo y separación
RIM, FINE, PUP = 4.2, 1.5, 12.5
X = R / 4.5               # módulo x = 8: el aro exterior mide ~0,5x, la separación 1x

def eye(cx, cy):
    """Aro grueso, tres anillos finos equidistantes, pupila con brillo."""
    p = ring(cx, cy, R, RIM)
    inner, n = R - RIM, 3
    g = (inner - PUP - n * FINE) / (n + 1)          # aire igual entre todos los anillos
    for i in range(n):
        outer_r = inner - g * (i + 1) - FINE * i
        p = lk.union(p, ring(cx, cy, outer_r, FINE))
    pu = lk.diff(C(cx, cy, PUP), C(cx + PUP * 0.36, cy - PUP * 0.36, PUP * 0.27))
    return lk.union(p, pu)

def eye_small(cx, cy):
    """Reducido (16-24 px): aro grueso y pupila, sin anillos ni brillo."""
    return lk.union(ring(cx, cy, R, 8.5), C(cx, cy, 14.5))

CX1, CX2 = R, 3 * R + GAP
SYM = lk.union(eye(CX1, R), eye(CX2, R))
SMALL = lk.union(eye_small(CX1, R), eye_small(CX2, R + 0))
SW = CX2 + R  # ancho del símbolo (152)

def _line(s, tracking, f, size=100):
    return lk.text(f, s, size=size, tracking=tracking)

def _w(p): b = lk.bounds(p); return b[2] - b[0]

def block(f=F_DISPLAY, t1=150, lead=1.34, size=100):
    g, m = _line("GABINETE", t1, f, size)
    target, lo, hi = _w(g), -100, 400
    for _ in range(40):
        mid = (lo + hi) / 2
        if _w(_line("CONTABLE", mid, f, size)[0]) < target: lo = mid
        else: hi = mid
    c, _ = _line("CONTABLE", (lo + hi) / 2, f, size)
    g = lk.move(g, -lk.bounds(g)[0], 0)
    c = lk.move(c, -lk.bounds(c)[0], lead * size)
    return lk.union(g, c)

WB, WBS = block(), block(F_TEXT, 170)

def vertical(ratio=1.85, gap=3.2 * X):
    s = SW * ratio / _w(WB); w = lk.scale(WB, s); b = lk.bounds(w)
    return lk.move(w, SW / 2 - (b[0] + b[2]) / 2, 2 * R + gap - b[1])

def horizontal(h_ratio=0.86, gap=2.6 * X):
    th = 2 * R * h_ratio
    s = th / (lk.bounds(WBS)[3] - lk.bounds(WBS)[1]); w = lk.scale(WBS, s); b = lk.bounds(w)
    return lk.move(w, SW + gap - b[0], R - th / 2 - b[1])

WV, WH = vertical(), horizontal()

def layers(word, scheme):
    ink, sym = {"color": (PET, PET), "negativo": (HUE, ORO), "oro": (ORO, ORO), "tinta": (TIN, TIN),
                "hueso": (HUE, HUE), "blanco": (WHITE, WHITE)}[scheme]
    L = [(SYM, sym)]
    if word is not None: L.append((word, ink))
    return L
