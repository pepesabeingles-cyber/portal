"""Símbolo y logotipos de Gabinete Contable. Unidad de construcción x = 8."""
import logo_kit as lk

PET, HUE, TIN, AMB, PETD, NIE, WHITE = "#134150", "#F6F3EC", "#14252B", "#E2A13C", "#0E343F", "#5C6E75", "#FFFFFF"
FONTS = "node_modules/@fontsource"
F7 = f"{FONTS}/bricolage-grotesque/files/bricolage-grotesque-latin-700-normal.woff2"
X = 8  # módulo
W, H = 12 * X, 15 * X  # 96 × 120


def body():
    """Silueta: borde superior cóncavo con dos penachos, lados rectos, base redonda."""
    p = lk.pathops.Path()
    r = W / 2
    p.moveTo(0, 0)
    p.quadTo(W / 2, 28, W, 0)
    p.lineTo(W, H - r)
    p.cubicTo(W, H - r + lk.K * r, W / 2 + lk.K * r, H, W / 2, H)
    p.cubicTo(W / 2 - lk.K * r, H, 0, H - r + lk.K * r, 0, H - r)
    p.close()
    return lk.soften(lk.clean(p), 1.2)


def parts(pr=9):
    eyes = lk.union(lk.circle(26, 40, 18), lk.circle(70, 40, 18))
    pup = lk.union(lk.circle(26, 40, pr), lk.circle(70, 40, pr))
    beak = lk.soften(lk.polygon([(42.5, 51), (53.5, 51), (48, 62)]), 0.8)
    eq = lk.union(lk.rect(32, 76, 4 * X, X, X / 2), lk.rect(32, 76 + 2 * X, 4 * X, X, X / 2))
    return dict(body=body(), eyes=eyes, pup=pup, beak=beak, eq=eq)


def small_parts():
    """Reducido (16-24 px): sin pico, ojos, pupilas y barras reforzados."""
    eyes = lk.union(lk.circle(26, 40, 19), lk.circle(70, 40, 19))
    pup = lk.union(lk.circle(26, 40, 10), lk.circle(70, 40, 10))
    eq = lk.union(lk.rect(28, 74, 40, 11), lk.rect(28, 95, 40, 11))
    return dict(body=body(), eyes=eyes, pup=pup, beak=None, eq=eq)


def mono(P):
    cut = [P["eyes"], P["eq"]] + ([P["beak"]] if P["beak"] is not None else [])
    return lk.union(lk.diff(P["body"], *cut), P["pup"])


def color(P, ink=PET, eye=HUE, accent=AMB):
    L = [(P["body"], ink), (P["eyes"], eye), (P["pup"], ink)]
    if P["beak"] is not None:
        L.append((P["beak"], accent))
    L.append((P["eq"], accent))
    return L


P = parts()
SYM = mono(P)
SMALL = mono(small_parts())

# ---------- logotipos ----------
_g, _mg = lk.text(F7, "Gabinete", size=100, tracking=-12)
_c, _mc = lk.text(F7, "Contable", size=100, tracking=-12)
_one, _m1 = lk.text(F7, "Gabinete Contable", size=100, tracking=-12)
CAP = _m1["cap_height"] / 100  # por unidad de tamaño


def _left(p, x):
    return lk.move(p, x - lk.bounds(p)[0], 0)


def word_stacked():
    top, base = 10, 118
    asc = -lk.bounds(_g)[1] / 100
    S = (base - top) / (asc + 1.0)
    y1 = top + asc * S
    g = _left(lk.move(lk.scale(_g, S / 100), 0, y1), W + 2 * X)
    c = _left(lk.move(lk.scale(_c, S / 100), 0, y1 + S), W + 2 * X)
    return lk.union(g, c)


def word_horizontal(size=64):
    w = lk.scale(_one, size / 100)
    base = H / 2 + CAP * size / 2
    return _left(lk.move(w, 0, base), W + 2 * X)


def word_vertical(size=40):
    w = lk.scale(_one, size / 100)
    wb = lk.bounds(w)
    return lk.move(w, W / 2 - (wb[0] + wb[2]) / 2, H + 2 * X + CAP * size)


WS, WH, WV = word_stacked(), word_horizontal(), word_vertical()
WORDONLY = lk.move(lk.scale(_one, 1), 0, 0)

# ---------- combinaciones de color por versión ----------
def layers(word, scheme):
    """scheme: color | negativo | tinta | hueso | petroleo | sobre-ambar"""
    if scheme == "color":
        return color(P) + ([(word, PET)] if word is not None else [])
    if scheme == "negativo":  # búho ámbar + nombre hueso, sobre petróleo
        return [(SYM, AMB)] + ([(word, HUE)] if word is not None else [])
    ink = {"tinta": TIN, "hueso": HUE, "petroleo": PET, "sobre-ambar": TIN, "blanco": WHITE}[scheme]
    return [(SYM, ink)] + ([(word, ink)] if word is not None else [])
