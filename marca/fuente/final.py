"""Gabinete Contable · el nombre en Bodoni Moda con un búho que acompaña."""
import logo_kit as lk
from buho import buho2, silueta2, patas, percha
from eyes import C
from sereno import G, Cn, F_DISPLAY, F_TEXT, word, match, _w, PET, PETD, HUE, TIN, ORO, NIE, WHITE

SYM = buho2()
# reducido (16-24 px): silueta, ojos grandes y pico; sin líneas finas
SMALL = lk.union(lk.diff(lk.union(silueta2(), patas()),
                         lk.diff(C(23, 40, 9), C(23, 40, 4.2)), lk.diff(C(47, 40, 9), C(47, 40, 4.2)),
                         lk.polygon([(35, 47), (39, 53), (35, 59), (31, 53)])), percha(t=2.6))
OW, OH = lk.bounds(SYM)[2] - lk.bounds(SYM)[0], lk.bounds(SYM)[3] - lk.bounds(SYM)[1]

LEAD = 134
BLOCK = lk.union(G, lk.move(Cn, 0, LEAD))
BB = lk.bounds(BLOCK); TH = BB[3] - BB[1]
X = OW / 6  # módulo: 1/6 del ancho del búho

def _fit(o, h):
    ob = lk.bounds(o); s = h / (ob[3] - ob[1]); o2 = lk.scale(o, s); return o2, s

def vertical(k=0.66, gap=0.30):
    """Principal: búho pequeño sobre el nombre."""
    o, s = _fit(SYM, TH * k); ob = lk.bounds(o)
    return lk.move(o, (BB[0] + BB[2]) / 2 - (ob[0] + ob[2]) / 2, BB[1] - TH * gap - ob[3])

_gs = word("GABINETE", 170, F_TEXT)[0]
BLOCK_S = lk.union(_gs, lk.move(match(_w(_gs), "CONTABLE", F_TEXT), 0, LEAD))   # corte texto para tamaños chicos
BBS = lk.bounds(BLOCK_S); THS = BBS[3] - BBS[1]

def horizontal(k=1.0, gap=0.36):
    """Búho a la izquierda, a la altura del bloque de texto (corte texto)."""
    o, s = _fit(SYM, THS * k); ob = lk.bounds(o)
    return lk.move(o, BBS[0] - THS * gap - ob[2], (BBS[1] + BBS[3]) / 2 - (ob[1] + ob[3]) / 2)

OV, OHZ = vertical(), horizontal()
V_TEXT = H_TEXT = BLOCK
WV, WH = "V", "H"

def layers(word, scheme):
    txt, sym = {"color": (PET, PET), "negativo": (HUE, ORO), "oro": (ORO, ORO), "tinta": (TIN, TIN),
                "hueso": (HUE, HUE), "blanco": (WHITE, WHITE), "sobre-oro": (TIN, TIN)}[scheme]
    if word == "V": return [(OV, sym), (BLOCK, txt)]
    if word == "H": return [(OHZ, sym), (BLOCK_S, txt)]
    return [(SYM, sym)]
