"""Búho de pie, frontal, esbelto. Coordenadas: ancho 70, alto ~146."""
import logo_kit as lk
from eyes import ring, C

def mirror_path(pts_right, cx=35):
    """pts_right: lista de segmentos cúbicos del lado derecho, desde arriba-centro hasta abajo-centro."""
    p = lk.pathops.Path()
    start = pts_right[0][0]
    p.moveTo(*start)
    for seg in pts_right:
        _, c1, c2, e = seg
        p.cubicTo(*c1, *c2, *e)
    for seg in reversed(pts_right):
        s, c1, c2, e = seg
        m = lambda q: (2 * cx - q[0], q[1])
        p.cubicTo(*m(c2), *m(c1), *m(s))
    p.close()
    return lk.clean(p)

def silueta(tuft=(57, 0), head=(67, 40), belly=(69, 92), dip=12, bottom=146):
    segs = [((35, dip), (43, dip - 1), (52, 6), tuft),
            (tuft, (62, 10), (67, 24), head),
            (head, (67.5, 58), (70, 74), belly),
            (belly, (68, 120), (52, bottom), (35, bottom))]
    return mirror_path(segs)

def hair_curve(pts, w):
    p = lk.pathops.Path(); p.moveTo(*pts[0]); p.cubicTo(*pts[1], *pts[2], *pts[3])
    return lk.stroke(p, w, cap="round")

def buho(eye_r=7.5, eye_hair=1.4, pup=3.4, eye_y=40, eye_dx=11.5, wing=True, hair=1.3, face=True, beak=(35, 52, 3.2, 5.5), **kw):
    s = silueta(**kw)
    cuts = []
    for cx in (35 - eye_dx, 35 + eye_dx):
        cuts.append(lk.diff(C(cx, eye_y, eye_r), C(cx, eye_y, pup)))
    bx, by, bw, bh = beak
    cuts.append(lk.polygon([(bx, by - bh), (bx + bw, by), (bx, by + bh), (bx - bw, by)]))
    if face:   # disco facial: arco fino bajo los ojos que baja hasta el pico
        for sgn in (-1, 1):
            cuts.append(hair_curve([(35 + sgn * 26, 30), (35 + sgn * 27, 52), (35 + sgn * 12, 60), (35 + sgn * 1.2, 62)], hair))
    if wing:   # alas plegadas
        for sgn in (-1, 1):
            cuts.append(hair_curve([(35 + sgn * 25, 70), (35 + sgn * 29, 98), (35 + sgn * 24, 124), (35 + sgn * 12, 138)], hair))
    return lk.diff(s, *cuts)

def silueta2(dip=12, bottom=140):
    """Cuerpo que se afina hacia abajo, con cola corta."""
    segs = [((35, dip), (43, dip - 1), (52, 6), (57, 0)),
            ((57, 0), (62, 10), (67, 24), (67, 40)),
            ((67, 40), (67.5, 58), (69.5, 76), (68.5, 94)),
            ((68.5, 94), (67, 118), (50, bottom - 2), (35, bottom))]
    return mirror_path(segs)

def patas(y=140, w=1.3):
    p = lk.pathops.Path()
    feet = []
    for cx in (28, 42):
        for dx in (-3.2, 0, 3.2):
            feet.append(lk.rect(cx + dx - 1.1, y - 4, 2.2, 7.5, 1.1))
    return lk.union(*feet)

def percha(x0=6, x1=64, y=146.5, t=1.6):
    return lk.rect(x0, y - t / 2, x1 - x0, t)

def buho2(eye_r=7.2, pup=3.3, eye_y=40, eye_dx=11.5, hair=1.3, perch=True):
    s = lk.union(silueta2(), patas())
    cuts = []
    for cx in (35 - eye_dx, 35 + eye_dx):
        cuts.append(lk.diff(C(cx, eye_y, eye_r), C(cx, eye_y, pup)))
    cuts.append(lk.polygon([(35, 46.5), (38.2, 52), (35, 57.5), (31.8, 52)]))
    for sgn in (-1, 1):
        cuts.append(hair_curve([(35 + sgn * 26, 30), (35 + sgn * 27, 52), (35 + sgn * 12, 60), (35 + sgn * 1.2, 62)], hair))
        cuts.append(hair_curve([(35 + sgn * 25, 70), (35 + sgn * 29, 98), (35 + sgn * 23, 122), (35 + sgn * 11, 134)], hair))
    o = lk.diff(s, *cuts)
    return lk.union(o, percha()) if perch else o

def buho_linea(w=1.8, eye_r=7.2, pup=3.3, eye_y=40, eye_dx=11.5, hair=1.3):
    """Versión en línea: el contorno con el trazo fino de Bodoni."""
    s = silueta2()
    contorno = lk.diff(s, lk.clean(lk.diff(s, lk.stroke(s, 2 * w))))  # borde interior de grosor w
    contorno = lk.inter(lk.stroke(s, 2 * w), s)
    parts = [contorno, patas(), percha()]
    for cx in (35 - eye_dx, 35 + eye_dx):
        parts.append(ring(cx, eye_y, eye_r, w)); parts.append(C(cx, eye_y, pup))
    parts.append(lk.polygon([(35, 46.5), (38.2, 52), (35, 57.5), (31.8, 52)]))
    for sgn in (-1, 1):
        parts.append(hair_curve([(35 + sgn * 26, 30), (35 + sgn * 27, 52), (35 + sgn * 12, 60), (35 + sgn * 1.2, 62)], hair))
        parts.append(hair_curve([(35 + sgn * 25, 70), (35 + sgn * 29, 98), (35 + sgn * 23, 122), (35 + sgn * 11, 134)], hair))
    return lk.union(*parts)
