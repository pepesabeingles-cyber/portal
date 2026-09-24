"""Gabinete Contable · búho americano en grabado + nombre en Bodoni Moda."""
import logo_kit as lk
from real2 import owl, owl_small
from sereno import G, Cn, F_DISPLAY, F_TEXT, word, match, _w, PET, PETD, HUE, TIN, ORO, NIE, WHITE

BODY, EW, EI, EP, EG = owl()          # cuerpo tallado, blanco del ojo, iris, pupila, brillo
SMALL = owl_small()
OB = lk.bounds(lk.union(BODY, EW))

LEAD = 134
BLOCK = lk.union(G, lk.move(Cn, 0, LEAD)); BB = lk.bounds(BLOCK); TH = BB[3] - BB[1]
_gs = word("GABINETE", 170, F_TEXT)[0]
BLOCK_S = lk.union(_gs, lk.move(match(_w(_gs), "CONTABLE", F_TEXT), 0, LEAD)); BBS = lk.bounds(BLOCK_S); THS = BBS[3] - BBS[1]

def _place(h, x_of, y_of):
    s = h / (OB[3] - OB[1])
    parts = [lk.scale(p, s) for p in (BODY, EW, EI, EP, EG)]
    b = lk.bounds(lk.union(parts[0], parts[1]))
    dx, dy = x_of(b), y_of(b)
    return [lk.move(p, dx, dy) for p in parts]

def owl_layers(parts, scheme):
    body, w, i, p, g = parts
    ink, eye_w, iris = {"color": (PET, HUE, ORO), "negativo": (HUE, PET, ORO), "oro": (ORO, PET, ORO), "tinta": (TIN, None, None),
                        "hueso": (HUE, None, None), "blanco": (WHITE, None, None)}[scheme]
    if eye_w is None:   # una tinta: el ojo queda calado, iris y pupila en la tinta
        return [(lk.union(body, lk.diff(i, lk.diff(i, p)), lk.diff(p, g)), ink)]
    return [(body, ink), (w, eye_w), (i, iris), (p, PET if scheme in ("oro", "negativo") else ink), (g, HUE if scheme == "oro" else eye_w)]

# principal: búho sobre el nombre; horizontal: búho a la izquierda
V_OWL = _place(TH * 1.05, lambda b: (BB[0] + BB[2]) / 2 - (b[0] + b[2]) / 2, lambda b: BB[1] - TH * 0.26 - b[3])
H_OWL = _place(THS * 1.55, lambda b: BBS[0] - THS * 0.42 - b[2], lambda b: BBS[3] + THS * 0.08 - b[3])
S_OWL = _place(OB[3] - OB[1], lambda b: -b[0], lambda b: -b[1])
WV, WH = "V", "H"

def layers(word, scheme):
    txt = {"color": PET, "negativo": HUE, "oro": ORO, "tinta": TIN, "hueso": HUE, "blanco": WHITE}[scheme]
    if word == "V": return owl_layers(V_OWL, scheme) + [(BLOCK, txt)]
    if word == "H": return owl_layers(H_OWL, scheme) + [(BLOCK_S, txt)]
    return owl_layers(S_OWL, scheme)
SYM = lk.union(BODY, EW)
