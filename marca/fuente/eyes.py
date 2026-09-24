"""Solo los ojos del búho: variantes."""
import math, logo_kit as lk
C = lambda x, y, r: lk.circle(x, y, r)
ring = lambda x, y, R, t: lk.diff(C(x, y, R), C(x, y, R - t))

def half_plane(x0, side, y0=-200, y1=400):
    return lk.rect(-400, y0, x0 + 400, y1 - y0) if side == "L" else lk.rect(x0, y0, 800, y1 - y0)

def brow(cx, cy, R, t, lift, side, mid):
    """Ceja en media luna: gruesa arriba, fina en los extremos (contraste de plumilla)."""
    outer = C(cx, cy - lift, R + t)
    inner = C(cx, cy, R)
    cres = lk.diff(outer, inner)
    cres = lk.inter(cres, lk.rect(-400, -400, 1200, cy - R * 0.05 + 400))  # solo la mitad superior
    return lk.inter(cres, half_plane(mid, side))

def A_mirada(R=34, gap=14, t=7, pup=13, brow_t=12, lift=10, gapb=5):
    cx1 = R; cx2 = 3 * R + gap; cy = R + 24; mid = (cx1 + cx2) / 2
    eyes = lk.union(ring(cx1, cy, R, t), ring(cx2, cy, R, t), C(cx1, cy, pup), C(cx2, cy, pup))
    b = lk.union(brow(cx1, cy, R + gapb, brow_t, lift, "L", mid), brow(cx2, cy, R + gapb, brow_t, lift, "R", mid))
    return lk.union(eyes, b)

def A2_ceja(R=34, gap=14, pup=14, brow_t=13, lift=11, gapb=4):
    """Sin aros: ceja + pupila. Lo mínimo."""
    cx1 = R; cx2 = 3 * R + gap; cy = R + 24; mid = (cx1 + cx2) / 2
    b = lk.union(brow(cx1, cy, R + gapb, brow_t, lift, "L", mid), brow(cx2, cy, R + gapb, brow_t, lift, "R", mid))
    return lk.union(b, C(cx1, cy, pup), C(cx2, cy, pup))

def B_grabado(R=36, gap=12, n=4, t=2.6, pup=12):
    """Anillos concéntricos como el grabado de un billete."""
    cx1 = R; cx2 = 3 * R + gap; cy = R
    p = lk.union(C(cx1, cy, pup), C(cx2, cy, pup))
    step = (R - pup - 4) / n
    for i in range(n):
        r = R - i * step
        p = lk.union(p, ring(cx1, cy, r, t if i else t + 1.4), ring(cx2, cy, r, t if i else t + 1.4))
    return p

def C_noche(R=34, gap=10, pup=15):
    """Dos discos (ojos encendidos) con pupila calada."""
    cx1 = R; cx2 = 3 * R + gap; cy = R
    return lk.union(lk.diff(C(cx1, cy, R), C(cx1, cy, pup)), lk.diff(C(cx2, cy, R), C(cx2, cy, pup)))

def C_disc_layers(R=34, gap=10, pup=15, ink="#C2A36B", pupc="#134150"):
    cx1 = R; cx2 = 3 * R + gap; cy = R
    return [(lk.union(C(cx1, cy, R), C(cx2, cy, R)), ink), (lk.union(C(cx1, cy, pup), C(cx2, cy, pup)), pupc)]

def D_iniciales(font_path, size=100):
    """Ojo izquierdo G, ojo derecho C, con pupila."""
    g, mg = lk.text(font_path, "G", size); c, mc = lk.text(font_path, "C", size)
    gb, cb = lk.bounds(g), lk.bounds(c)
    g = lk.move(g, -gb[0], -gb[1]); c = lk.move(c, -cb[0], -cb[1])
    gw, gh = gb[2] - gb[0], gb[3] - gb[1]
    c = lk.move(c, gw + size * 0.12, (gh - (cb[3] - cb[1])) / 2)
    cb = lk.bounds(c)
    pr = gh * 0.14
    return lk.union(g, c, C(gw / 2 + gw * 0.02, gh / 2, pr), C((cb[0] + cb[2]) / 2 + (cb[2]-cb[0]) * 0.02, (cb[1] + cb[3]) / 2, pr))

def eye_engraved(cx, cy, R=36, rim=4.2, rings=3, fine=1.5, pup=11.5, glint=True, radial=0, radial_w=1.3):
    p = ring(cx, cy, R, rim)
    inner_R = R - rim - 3.2
    if radial:
        spokes = lk.pathops.Path()
        for i in range(radial):
            a = 2 * math.pi * i / radial
            x1, y1 = cx + (pup + 3.5) * math.cos(a), cy + (pup + 3.5) * math.sin(a)
            x2, y2 = cx + inner_R * math.cos(a), cy + inner_R * math.sin(a)
            ln = lk.pathops.Path(); ln.moveTo(x1, y1); ln.lineTo(x2, y2)
            spokes = lk.union(spokes, lk.stroke(ln, radial_w, cap="butt")) if i else lk.stroke(ln, radial_w, cap="butt")
        p = lk.union(p, spokes, ring(cx, cy, inner_R + fine, fine))
    else:
        step = (inner_R - pup - 3) / max(rings - 1, 1)
        for i in range(rings):
            p = lk.union(p, ring(cx, cy, inner_R - i * step, fine))
    pu = C(cx, cy, pup)
    if glint:
        pu = lk.diff(pu, C(cx + pup * 0.36, cy - pup * 0.36, pup * 0.26))
    return lk.union(p, pu)

def pair(R=36, gap=8, **kw):
    cx1 = R; cx2 = 3 * R + gap
    return lk.union(eye_engraved(cx1, R, R, **kw), eye_engraved(cx2, R, R, **kw))

def hairline_brow(R=36, gap=8, w=1.6, rise=10):
    """Ceja fina en V: el borde del disco facial, dos arcos que se juntan en punta."""
    cx1 = R; cx2 = 3 * R + gap; mid = (cx1 + cx2) / 2
    p = lk.pathops.Path()
    p.moveTo(cx1 - R * 0.95, R - R * 0.35)
    p.cubicTo(cx1 - R * 0.6, -rise, cx1 + R * 0.7, -rise, mid, R * 0.28)
    p.cubicTo(cx2 - R * 0.7, -rise, cx2 + R * 0.6, -rise, cx2 + R * 0.95, R - R * 0.35)
    return lk.stroke(p, w, cap="round")

def small_pair(R=36, gap=10):
    """Reducido: aro grueso + pupila."""
    cx1 = R; cx2 = 3 * R + gap
    return lk.union(ring(cx1, R, R, 8), ring(cx2, R, R, 8), C(cx1, R, 14), C(cx2, R, 14))
