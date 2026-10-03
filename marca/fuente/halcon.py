"""Halcón peregrino (Falco peregrinus), de perfil mirando a la derecha, estilo grabado. Lienzo 200 × 300."""
import math
import logo_kit as lk
from eyes import C

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


# silueta: cabeza con capucha, pico corto y ganchudo, pecho, ala plegada y cola bajo la rama
HEAD = "M100 56 C96 38 104 22 120 20.4 C129.4 19.6 136 22.4 140 27.2 C142.6 30.4 144 34 144.6 38 L145 44 C145 50 144 54 142 58 L104 68 Z"
BEAK = ("M139.2 27.6 C143.8 27 148 29.2 150.2 33.2 C152.2 37 152.2 41.6 150.4 45.4 L148.2 49.4 "
        "C148 45.8 147.4 43 145.8 41.8 L144.8 43.4 L143.6 41.8 C142 42.4 140.4 42.6 139 42.2 Z")
BODY = ("M104 42 C126 44 144 54 152 74 C161 96 163 130 157 162 C151 188 140 206 128 216 "
        "C124 219 118 221 112 222 L100 221 C86 206 76 180 72 150 C68 116 74 80 88 58 C93 50 98 44 104 42 Z")
WING = ("M96 54 C82 70 72 100 72 136 C72 178 82 222 96 262 C98 268 100 272 103 275 "
        "C108 246 116 210 122 172 C128 128 120 82 96 54 Z")
TAIL = "M101 206 L121 208 L114 283 C110 285 105 285 101.4 283 Z"
# capucha oscura con la bigotera que baja desde el ojo
HOOD = ("M80 0 L170 0 L170 45 C158 46 146 45 136 45.4 C135 52.4 133.4 59.4 129.8 65.6 "
        "C129.2 66.8 128 66.8 127.4 65.6 C124.8 59.4 123.8 52.4 124 46.4 C118 46 112 49 108 56 L80 72 Z")

LEAN, PIVOT = 5.0, (114, 228)
EYE = (126.2, 33.6)      # centro del ojo
EYE_R = 8.2

def eye_parts(cx=EYE[0], cy=EYE[1], r=EYE_R, ring=2.8, gap=1.3, glint=1.55):
    white = C(cx, cy, r)                              # filete claro alrededor del anillo
    iris = C(cx, cy, r - gap)                         # anillo orbital en oro
    pupil = C(cx, cy, r - gap - ring)                 # ojo oscuro del halcón
    g = C(cx + 1.6, cy - 1.6, glint)
    return white, iris, pupil, g

def bars(free, y0, y1, dy, dx, half, w, stagger=True):
    """Barrado: solo las marcas que caben enteras dentro de `free`."""
    out = []
    for j, y in enumerate(range(y0, y1, dy)):
        off = dx / 2 if (stagger and j % 2) else 0
        x = 60 + off
        while x < 170:
            if all(free.contains((px, py)) for px, py in ((x - half - 1.5, y), (x + half + 1.5, y), (x, y - 2), (x, y + 3))):
                out.append(line(f"M{x-half} {y} C{x-half/3} {y+1.6} {x+half/3} {y+1.6} {x+half} {y}", w))
            x += dx
    return out

def falcon():
    head, beak, body, wing, tail = (lk.from_svg(d) for d in (HEAD, BEAK, BODY, WING, TAIL))
    sil = lk.union(head, beak, body, wing, tail)
    front = lk.union(head, body)
    edge = lk.stroke(front, 4.6)                                           # filete oscuro del contorno
    under = lk.diff(front, lk.from_svg(HOOD), lk.union(wing, lk.stroke(lk.from_svg(WING), 5.2)), edge)
    cuts = [under]
    # cera, fosa nasal y comisura
    cuts.append(C(143.6, 32.4, 1.25))
    # borde del ala sobre la cola
    cuts.append(lk.inter(lk.stroke(lk.from_svg(WING), 1.5), lk.diff(lk.from_svg(TAIL), lk.rect(0, 0, 200, 214))))
    # cobertoras: escamas en el hombro
    for (x, y) in ((93, 80), (86, 94), (98, 96), (81, 110), (93, 112), (105, 110), (82, 128), (95, 130), (108, 126), (88, 146), (101, 146), (113, 142)):
        cuts.append(line(f"M{x-4.6} {y} C{x-2} {y+3.8} {x+2} {y+3.8} {x+4.6} {y}", 1.05))
    # primarias: trazos largos que se afinan hacia la punta
    for x0 in (84, 93, 102):
        cuts.append(tline(f"M{x0} 164 C{x0-1} 196 {x0+1} 232 {x0+4} 262", 1.5, 0.7))
    b = lk.diff(sil, *cuts)
    # barrado oscuro del pecho, sobre la parte clara (garganta limpia)
    b = lk.union(b, *bars(under, 92, 212, 8, 9, 3.0, 1.15))
    W, I, P, G = eye_parts()
    b = lk.diff(b, W)
    # el ave se inclina un poco hacia adelante, apoyada en la rama
    tilt = lambda p: lk.rotate(p, LEAN, *PIVOT)
    b, W, I, P, G = (tilt(p) for p in (b, W, I, P, G))
    # tarsos y dedos que abrazan la rama, con uñas
    feet = []
    for fx in (111, 124):
        feet.append(lk.from_svg(f"M{fx-4} 212 C{fx-4} 218 {fx-3.4} 224 {fx-2.4} 229.6 L{fx+3} 229.6 C{fx+3.4} 224 {fx+3.8} 218 {fx+4} 212 Z"))
        feet.append(tline(f"M{fx} 228.6 C{fx+6} 228.4 {fx+10.4} 231 {fx+10.6} 240.6", 3.4, 0.9))
        feet.append(tline(f"M{fx+1} 229 C{fx+4.6} 230 {fx+6.4} 233 {fx+6} 241.4", 3.0, 0.8))
        feet.append(tline(f"M{fx-1} 228.8 C{fx-4.6} 229.4 {fx-7.6} 232 {fx-7.6} 240", 3.0, 0.8))
    branch = lk.from_svg("M2 231.5 C60 229 140 229 198 231 L198 236.5 C140 235 60 235 3 238 Z")
    return lk.union(b, *feet, branch), W, I, P, G

def falcon_small():
    """Reducido (16–32 px): la cabeza sola, con capucha, bigotera, garganta clara y ojo; sin barrado."""
    head, beak, body = (lk.from_svg(d) for d in (HEAD, BEAK, BODY))
    bust = lk.inter(lk.union(head, body), lk.from_svg("M60 0 L180 0 L180 88 C150 96 110 96 60 88 Z"))
    sil = lk.union(bust, beak)
    wing = lk.from_svg(WING)
    under = lk.diff(bust, lk.from_svg(HOOD), lk.union(wing, lk.stroke(wing, 8)), lk.stroke(bust, 9))
    b = lk.diff(sil, under, C(*EYE, EYE_R + 1.4))
    return lk.union(b, C(EYE[0], EYE[1], EYE_R - 3.0))

if __name__ == "__main__":
    import prev
    from sereno import PET, HUE, ORO
    body, W, I, P, G = falcon()
    color = [(body, PET), (W, HUE), (I, ORO), (P, PET), (G, HUE)]
    neg = [(body, HUE), (W, PET), (I, ORO), (P, PET), (G, HUE)]
    prev.show(color, neg, falcon_small())
