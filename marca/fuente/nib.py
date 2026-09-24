import logo_kit as lk
FS = "node_modules/@fontsource"
def font(fam, w): return f"{FS}/{fam}/files/{fam}-latin-{w}-normal.woff2"

def silhouette(W=100, H=150, dip=15, shoulder=(101, 70), taper=(66, 120)):
    p = lk.pathops.Path()
    p.moveTo(0, 0)
    p.quadTo(W / 2, 2 * dip, W, 0)
    p.cubicTo(shoulder[0], shoulder[1], taper[0], taper[1], W / 2, H)
    p.cubicTo(W - taper[0], taper[1], W - shoulder[0], shoulder[1], 0, 0)
    p.close()
    return lk.clean(p)

def owl(eye="ring", slit=True, ex=30, ey=42, er=15, rim=3.2, pup=7, beak=(64, 5, 7), slit_w=2.4, **kw):
    s = silhouette(**kw)
    cuts = []
    for cx in (ex, 100 - ex):
        if eye == "ring":      # aro fino, iris sólido
            cuts.append(lk.diff(lk.circle(cx, ey, er), lk.circle(cx, ey, er - rim)))
        elif eye == "ringpupil":  # aro + pupila
            cuts.append(lk.diff(lk.circle(cx, ey, er), lk.circle(cx, ey, er - rim)))
            cuts.append(lk.diff(lk.circle(cx, ey, er - rim - 2.6), lk.circle(cx, ey, pup)))
        elif eye == "disc":    # disco claro con pupila
            cuts.append(lk.diff(lk.circle(cx, ey, er), lk.circle(cx, ey, pup)))
    by, bw, bh = beak
    cuts.append(lk.polygon([(50, by - bh), (50 + bw, by), (50, by + bh), (50 - bw, by)]))
    if slit:
        cuts.append(lk.polygon([(50 - slit_w / 2, by + bh - 1), (50 + slit_w / 2, by + bh - 1), (50 + 0.01, 152), (50 - 0.01, 152)]))
    return lk.diff(s, *cuts)
