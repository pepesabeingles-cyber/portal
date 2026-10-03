"""Gabinete Contable · halcón peregrino en grabado + nombre en Bodoni Moda."""
import logo_kit as lk
from halcon import falcon, falcon_small
from sereno import G, Cn, F_DISPLAY, F_TEXT, word, match, _w, PET, PETD, HUE, TIN, ORO, NIE, WHITE

BODY, EW, EI, EP, EG = falcon()       # cuerpo tallado, filete del ojo, anillo en oro, ojo, brillo
SMALL = falcon_small()
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

def ave_layers(parts, scheme):
    body, w, i, p, g = parts
    ink, eye_w, iris = {"color": (PET, HUE, ORO), "negativo": (HUE, PET, ORO), "oro": (ORO, PET, ORO), "tinta": (TIN, None, None),
                        "hueso": (HUE, None, None), "blanco": (WHITE, None, None)}[scheme]
    if eye_w is None:   # una tinta: el filete queda calado, anillo y ojo en la tinta
        return [(lk.union(body, lk.diff(i, lk.diff(i, p)), lk.diff(p, g)), ink)]
    return [(body, ink), (w, eye_w), (i, iris), (p, PET if scheme in ("oro", "negativo") else ink), (g, HUE)]

# principal: halcón sobre el nombre; horizontal: halcón a la izquierda
V_AVE = _place(TH * 1.22, lambda b: (BB[0] + BB[2]) / 2 - (b[0] + b[2]) / 2, lambda b: BB[1] - TH * 0.26 - b[3])
H_AVE = _place(THS * 1.55, lambda b: BBS[0] - THS * 0.42 - b[2], lambda b: BBS[3] + THS * 0.08 - b[3])
S_AVE = _place(OB[3] - OB[1], lambda b: -b[0], lambda b: -b[1])
WV, WH = "V", "H"

def layers(word, scheme):
    txt = {"color": PET, "negativo": HUE, "oro": ORO, "tinta": TIN, "hueso": HUE, "blanco": WHITE}[scheme]
    if word == "V": return ave_layers(V_AVE, scheme) + [(BLOCK, txt)]
    if word == "H": return ave_layers(H_AVE, scheme) + [(BLOCK_S, txt)]
    return ave_layers(S_AVE, scheme)
SYM = lk.union(BODY, EW)
