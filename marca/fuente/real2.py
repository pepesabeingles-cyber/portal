"""Búho americano (Bubo virginianus), frontal, estilo grabado. Lienzo 200 × 300."""
import math
import logo_kit as lk
from eyes import C

def mirror(p, cx=100): return lk.transform(p, -1, 0, 0, 1, 2 * cx, 0)
def both(p): return lk.union(p, mirror(p))
def sym(d): L = lk.from_svg(d); return both(L)
def line(d, w, cap="round"): return lk.stroke(lk.from_svg(d), w, cap=cap)
def tline(d, w0, w1, n=24):
    """Trazo que se afina de w0 a w1 (como un corte de gubia)."""
    p = lk.from_svg(d)
    # muestreo de la curva cúbica única M x y C ...
    nums = [float(v) for v in d.replace("M", " ").replace("C", " ").replace(",", " ").split()]
    P = [(nums[i], nums[i + 1]) for i in range(0, 8, 2)]
    pts = []
    for k in range(n + 1):
        t = k / n
        x = (1-t)**3*P[0][0] + 3*(1-t)**2*t*P[1][0] + 3*(1-t)*t**2*P[2][0] + t**3*P[3][0]
        y = (1-t)**3*P[0][1] + 3*(1-t)**2*t*P[1][1] + 3*(1-t)*t**2*P[2][1] + t**3*P[3][1]
        pts.append((x, y, w0 + (w1 - w0) * t))
    out = None
    for x, y, w in pts:
        c = C(x, y, w / 2)
        out = c if out is None else lk.union(out, c)
    for (x0, y0, a), (x1, y1, b) in zip(pts, pts[1:]):
        ang = math.atan2(y1 - y0, x1 - x0) + math.pi / 2
        q = lk.polygon([(x0 + math.cos(ang) * a / 2, y0 + math.sin(ang) * a / 2), (x1 + math.cos(ang) * b / 2, y1 + math.sin(ang) * b / 2),
                        (x1 - math.cos(ang) * b / 2, y1 - math.sin(ang) * b / 2), (x0 - math.cos(ang) * a / 2, y0 - math.sin(ang) * a / 2)])
        out = lk.union(out, q)
    return out

SIL = ("M100 46 C90 46 79 44 71 38 C64 28 55 12 44 0 C43 10 41 19 37 26 C34 24 30 22 26 21 "
       "C29 30 29 39 26 47 C20 61 18 79 19 97 C20 109 17 120 15 132 C12 148 11 166 13 184 "
       "C16 210 30 234 52 250 C62 256 70 258 80 259 L82 276 L100 278 L100 46 Z")

EYE_Y, EYE_DX, EYE_R = 93, 24.5, 16.8

def eye_parts(cx, cy=EYE_Y, r=EYE_R, lid=0.09, pup=9.2, rim=2.6):
    lid_y = cy - r + 2 * r * lid                               # borde del párpado
    lidcut = lk.from_svg(f"M{cx-r-3} {cy-r-3} L{cx+r+3} {cy-r-3} L{cx+r+3} {lid_y-1.5} C{cx+r*0.4} {lid_y+1.2} {cx-r*0.4} {lid_y+1.2} {cx-r-3} {lid_y-1.5} Z")
    white = lk.diff(C(cx, cy, r), lidcut)                      # anillo claro exterior
    iris = lk.diff(C(cx, cy, r - rim), lidcut)
    pupil = lk.diff(C(cx, cy + 1, pup), lidcut)
    glint = C(cx + pup * 0.35, cy - pup * 0.1, 1.9)
    return white, iris, pupil, glint

def owl():
    body = sym(SIL)
    # tallas en hueso (cortes del grabado)
    cuts = []
    # disco facial: borde exterior, de la mejilla al mentón
    cuts.append(both(line("M42 66 C30 86 32 114 52 126 C64 132 80 131 94 123", 2.5)))
    # cejas en V suave, desde los penachos
    cuts.append(both(tline("M58 64 C70 59 86 64 98 84", 1.2, 3.4)))
    # babero claro bajo la cara
    # pecho: marcas de plumaje en filas (barrado)
    ticks = []
    # barrado fino que sigue el óvalo del vientre: marcas más cortas hacia los bordes
    cx0, cy0, rx, ry = 100, 196, 40, 50
    for j, y in enumerate(range(152, 244, 8)):
        off = 5.5 if j % 2 else 0
        for x in [100 - off - 11 * k for k in range(0, 5)]:
            d = ((x - cx0) / rx) ** 2 + ((y - cy0) / ry) ** 2
            if d > 0.92 or x > 100: continue
            half = 4.4 * (1 - 0.55 * d)
            if x + half > 97.5:
                continue
            ticks.append(line(f"M{x-half} {y} C{x-half/3} {y-1.3} {x+half/3} {y+1.3} {x+half} {y}", 1.0))
    cuts.append(both(lk.union(*ticks)))
    center = []
    for j, y in enumerate(range(152, 244, 8)):
        d = ((y - cy0) / ry) ** 2
        if j % 2 == 0 and d <= 0.92:
            half = 4.4 * (1 - 0.55 * d)
            center.append(line(f"M{100-half} {y} C{100-half/3} {y-1.3} {100+half/3} {y+1.3} {100+half} {y}", 1.0))
    cuts.append(lk.union(*center))
    # ala plegada: borde, cobertoras y primarias
    cuts.append(both(tline("M30 128 C30 170 38 212 58 246", 1.3, 2.6)))
    cuts.append(both(lk.union(tline("M40 222 C44 232 50 240 58 247", 1.0, 1.7), tline("M34 204 C37 218 43 230 51 240", 1.0, 1.5), tline("M29 186 C31 202 36 216 44 228", 0.9, 1.3))))
    # pico
    cuts.append(lk.from_svg("M100 100 C104 101 106 106 104 112 C103 116 101 119 100 121 C99 119 97 116 96 112 C94 106 96 101 100 100 Z"))
    b = lk.diff(body, *cuts)
    beak_dark = lk.from_svg("M100 103 C102.5 104 103.5 107 102.5 111 C101.8 114 100.8 116 100 117.5 C99.2 116 98.2 114 97.5 111 C96.5 107 97.5 104 100 103 Z")
    b = lk.union(b, beak_dark)
    # ojos
    whites, irises, pupils, glints = [], [], [], []
    for cx in (100 - EYE_DX, 100 + EYE_DX):
        w, i, p, g = eye_parts(cx)
        whites.append(w); irises.append(i); pupils.append(p); glints.append(g)
    W = lk.union(*whites); I = lk.union(*irises); Pp = lk.union(*pupils); G = lk.union(*glints)
    b = lk.diff(b, W)
    # patas emplumadas y garras sobre la rama
    feet = []
    for fx in (84, 116):
        feet.append(lk.from_svg(f"M{fx-10} 244 C{fx-12} 254 {fx-11} 262 {fx-9} 268 L{fx+9} 268 C{fx+11} 262 {fx+12} 254 {fx+10} 244 Z"))
        for dx in (-7, 0, 7):
            feet.append(lk.from_svg(f"M{fx+dx-2.6} 266 L{fx+dx+2.6} 266 C{fx+dx+3} 272 {fx+dx+2} 277 {fx+dx-1.5} 279.5 C{fx+dx-0.6} 276 {fx+dx-1.8} 271 {fx+dx-2.6} 266 Z"))
    feet = lk.union(*feet)
    tail = lk.from_svg("M90 268 L110 268 L108 287 C104 289 96 289 92 287 Z")
    branch = lk.from_svg("M2 270.5 C60 268 140 268 198 270 L198 275.5 C140 274 60 274 3 277 Z")
    feet = lk.union(feet, tail)
    return lk.union(b, feet, branch), W, I, Pp, G


def owl_small():
    body = sym(SIL)
    cuts = [both(line("M42 66 C30 86 32 114 52 126 C64 132 80 131 94 123", 5.0)),
            both(tline("M58 64 C70 59 86 64 98 84", 3.0, 5.5))]
    b = lk.diff(body, *cuts)
    eyes, pups = [], []
    for cx in (100 - EYE_DX, 100 + EYE_DX):
        eyes.append(C(cx, EYE_Y, EYE_R + 1)); pups.append(C(cx, EYE_Y + 1, 9.5))
    b = lk.union(lk.diff(b, *eyes), *pups)
    feet = lk.union(*[lk.from_svg(f"M{fx-10} 244 C{fx-12} 254 {fx-11} 262 {fx-9} 270 L{fx+9} 270 C{fx+11} 262 {fx+12} 254 {fx+10} 244 Z") for fx in (84, 116)])
    branch = lk.from_svg("M2 269 C60 266 140 266 198 268 L198 278 C140 276 60 276 3 280 Z")
    return lk.union(b, feet, branch)
