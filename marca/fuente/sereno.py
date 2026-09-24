"""Ojos serenos: aro fino + pupila, acompañando al nombre."""
import logo_kit as lk
import fuentes
from eyes import ring, C
fuentes.asegurar()
PET, PETD, HUE, TIN, ORO, NIE, WHITE = "#134150", "#0E2F3A", "#F4F0E8", "#14252B", "#C2A36B", "#5C6E75", "#FFFFFF"
F_DISPLAY = "fonts/bodoni-op18-w500.ttf"
F_TEXT = "fonts/bodoni-op11-w600.ttf"

def eyes(d=26, gap=None, hair=2.2, pupil=0.42):
    """Par de ojos de diámetro d: aro fino (el trazo fino de Bodoni) y pupila sólida."""
    r = d / 2; gap = d * 0.28 if gap is None else gap
    c1, c2 = r, 3 * r + gap
    e = lambda cx: lk.union(ring(cx, r, r, hair), C(cx, r, r * pupil))
    return lk.union(e(c1), e(c2))

def word(s, tracking, f=F_DISPLAY, size=100):
    p, m = lk.text(f, s, size=size, tracking=tracking)
    return lk.move(p, -lk.bounds(p)[0], 0), m

def _w(p): b = lk.bounds(p); return b[2] - b[0]

def match(target, s, f=F_DISPLAY):
    lo, hi = -100, 400
    for _ in range(40):
        mid = (lo + hi) / 2
        if _w(word(s, mid, f)[0]) < target: lo = mid
        else: hi = mid
    return word(s, (lo + hi) / 2, f)[0]

def hline(x0, x1, y, t):
    return lk.rect(x0, y - t / 2, x1 - x0, t)

G, MG = word("GABINETE", 150)
CAPH = MG["cap_height"]
W = _w(G)
Cn = match(W, "CONTABLE")

def stacked(d=24, hair=2.2, rule=1.6, row_gap=None, rule_gap=14):
    """GABINETE / filete con ojos / CONTABLE."""
    row_gap = row_gap or CAPH * 0.36
    e = eyes(d, hair=hair)
    ew = _w(e)
    y_row = row_gap + d / 2                      # centro de la fila, bajo la línea base de GABINETE
    e = lk.move(e, W / 2 - ew / 2, y_row - d / 2)
    l1 = hline(0, W / 2 - ew / 2 - rule_gap, y_row, rule)
    l2 = hline(W / 2 + ew / 2 + rule_gap, W, y_row, rule)
    c = lk.move(Cn, 0, y_row + d / 2 + row_gap + CAPH)
    return G, lk.union(l1, l2), e, c

def one_line(d=None, f=F_DISPLAY, tracking=150):
    """GABINETE ◦◦ CONTABLE en una línea."""
    g, m = word("GABINETE", tracking, f); c, _ = word("CONTABLE", tracking, f)
    d = d or m["cap_height"] * 0.5
    e = eyes(d, hair=2.4)
    sp = m["cap_height"] * 0.55
    e = lk.move(e, _w(g) + sp, -m["cap_height"] / 2 - d / 2)
    c = lk.move(c, lk.bounds(e)[2] + sp, 0)
    return g, e, c

# ---------- sistema final ----------
_g, _rl, _e, _c = stacked(d=26)
V_TEXT, V_ACC = lk.union(_g, _c), lk.union(_rl, _e)
_g1, _e1, _c1 = one_line(f=F_TEXT, tracking=170)
H_TEXT, H_ACC = lk.union(_g1, _c1), _e1
SYM = eyes(26, hair=2.2)                 # los ojos solos: avatar, sello, marca de agua
SMALL = eyes(26, hair=4.6, pupil=0.46)   # reducido: 16-32 px
WV, WH = "V", "H"
X = 26  # módulo: diámetro de un ojo; zona de protección = 2x

def layers(word, scheme):
    txt, acc = {"color": (PET, PET), "negativo": (HUE, ORO), "oro": (ORO, ORO), "tinta": (TIN, TIN),
                "hueso": (HUE, HUE), "blanco": (WHITE, WHITE), "sobre-oro": (TIN, TIN)}[scheme]
    if word == "V": return [(V_TEXT, txt), (V_ACC, acc)]
    if word == "H": return [(H_TEXT, txt), (H_ACC, acc)]
    return [(SYM, acc)]
