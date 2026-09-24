import os, sys, logo_kit as lk
from owl import *
from shot import shot, HERE
M = f"file://{HERE}/out/marca"
def inl(L, h=None, w=None, pad=0, extra=""):
    s = lk.svg(L, pad=pad)
    attr = (f'height="{h}" ' if h else "") + (f'width="{w}" ' if w else "") + extra
    return s.replace("<svg ", f"<svg {attr} ", 1)
def page(body, bg, css=""):
    return f"<html><head><style>body{{background:{bg};font-family:'Hanken Grotesk';color:{TIN}}}{css}</style></head><body>{body}</body></html>"
def center(inner, w, h, bg):
    return page(f'<div style="width:{w}px;height:{h}px;display:flex;align-items:center;justify-content:center;background:{bg}">{inner}</div>', bg)
only = set(sys.argv[1:])
def want(k): return not only or k in only

# ---------- idea: búho anotado ----------
if want("idea"):
    s = 4.2
    owl = inl(color(P), w=W * s)
    lab = f"font-family:'Hanken Grotesk';font-weight:600;font-size:22px;letter-spacing:2px;text-transform:uppercase;color:{NIE}"
    line = f"position:absolute;height:2px;background:{NIE}"
    ox, oy = 330, 40
    ex1, ex2, ey = ox + 26 * s, ox + 70 * s, oy + 40 * s
    eqy = oy + 84 * s
    body = f'''<div style="position:relative;width:1100px;height:600px;background:{HUE}">
<div style="position:absolute;left:{ox}px;top:{oy}px">{owl}</div>
<div style="{line};left:40px;top:{ey}px;width:{ex1 - 40 - 18*s}px"></div><div style="position:absolute;left:40px;top:{ey-40}px;{lab}">Debe</div>
<div style="{line};left:{ex2 + 18*s}px;top:{ey}px;width:{1060 - ex2 - 18*s}px"></div><div style="position:absolute;right:40px;top:{ey-40}px;{lab};text-align:right">Haber</div>
<div style="{line};left:{ox + 64*s + 12}px;top:{eqy}px;width:{1060 - ox - 64*s - 12}px"></div><div style="position:absolute;right:40px;top:{eqy-40}px;{lab};text-align:right">La cuenta cuadra</div>
</div>'''
    shot(page(body, HUE), "img/idea.png", 1100, 600)

# ---------- construcción ----------
if want("construccion"):
    s = 5.0; mx, my = 110, 70
    grid = "".join(f'<line x1="{mx + i*X*s}" y1="{my}" x2="{mx + i*X*s}" y2="{my + H*s}" stroke="#8FA3A9" stroke-opacity=".55" stroke-width="1.5"/>' for i in range(13))
    grid += "".join(f'<line x1="{mx}" y1="{my + j*X*s}" x2="{mx + W*s}" y2="{my + j*X*s}" stroke="#8FA3A9" stroke-opacity=".55" stroke-width="1.5"/>' for j in range(16))
    owl = "".join(f'<path fill="{c}" d="{lk.d(p)}" transform="translate({mx},{my}) scale({s})"/>' for p, c in color(P))
    t = lambda x, y, txt, a="middle": f'<text x="{x}" y="{y}" text-anchor="{a}" font-family="Hanken Grotesk" font-weight="600" font-size="24" fill="{TIN}">{txt}</text>'
    dims = (f'<line x1="{mx}" y1="{my-30}" x2="{mx+W*s}" y2="{my-30}" stroke="{TIN}" stroke-width="2"/>{t(mx+W*s/2, my-42, "12x")}'
            f'<line x1="{mx-40}" y1="{my}" x2="{mx-40}" y2="{my+H*s}" stroke="{TIN}" stroke-width="2"/>{t(mx-56, my+H*s/2+8, "15x", "end")}')
    # callouts
    cx = mx + W*s + 40
    def call(y_target, x_target, txt):
        return (f'<line x1="{x_target}" y1="{y_target}" x2="{cx}" y2="{y_target}" stroke="{TIN}" stroke-width="2"/>'
                f'<circle cx="{x_target}" cy="{y_target}" r="5" fill="{TIN}"/>{t(cx+14, y_target+8, txt, "start")}')
    elbow = (f'<polyline points="{mx+48*s},{my+40*s} {mx+48*s},{my+19*s} {cx},{my+19*s}" fill="none" stroke="{TIN}" stroke-width="2"/>'
             f'<circle cx="{mx+48*s}" cy="{my+40*s}" r="5" fill="{TIN}"/>{t(cx+14, my+19*s+8, "separación entre ojos: 1x", "start")}')
    callouts = (elbow + call(my + 40*s, mx + 84*s, "anillo del ojo: 1x")
                + call(my + 80*s, mx + 64*s, "barras del igual: 4x · 1x")
                + call(my + 88*s, mx + 48*s, "espacio entre barras: 1x"))
    body = f'<svg width="1000" height="720" xmlns="http://www.w3.org/2000/svg" style="background:{HUE}">{owl}{grid}{dims}{callouts}</svg>'
    shot(page(body, HUE), "img/construccion.png", 1000, 720)

# ---------- versiones ----------
if want("versiones"):
    for name, word, w, h, hh in (("v_apilada", WS, 900, 300, 200), ("v_horizontal", WH, 520, 200, 70), ("v_vertical", WV, 520, 200, 150), ("v_simbolo", None, 520, 200, 150)):
        shot(center(inl(layers(word, "color"), h=hh), w, h, HUE), f"img/{name}.png", w, h)
    shot(center(inl([(SMALL, PET)], h=24) + '<span style="width:40px"></span>' + inl([(SMALL, PET)], h=16)
                + '<span style="width:40px"></span>' + f'<img src="{M}/iconos/favicon.svg" style="width:32px">', 520, 200, HUE), "img/v_reducido.png", 520, 200)

# ---------- espacio libre ----------
if want("espacio"):
    s = 1.9; pad = 2 * X
    b = lk.bounds(lk.union(P["body"], WS))
    x0, y0, x1, y1 = b[0] - pad, b[1] - pad, b[2] + pad, b[3] + pad
    ox, oy = 60, 50
    tr = lambda v, o, m: o + (v - m) * s
    logo = "".join(f'<path fill="{c}" d="{lk.d(p)}" transform="translate({ox - x0*s},{oy - y0*s}) scale({s})"/>' for p, c in layers(WS, "color"))
    W2, H2 = (x1 - x0) * s, (y1 - y0) * s
    zone = (f'<rect x="{ox}" y="{oy}" width="{W2}" height="{H2}" fill="{PET}" fill-opacity=".08" stroke="{PET}" stroke-width="2" stroke-dasharray="8 6"/>'
            f'<rect x="{ox + pad*s}" y="{oy + pad*s}" width="{W2 - 2*pad*s}" height="{H2 - 2*pad*s}" fill="none" stroke="{PET}" stroke-opacity=".5" stroke-width="1.5"/>')
    t = lambda x, y, txt: f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Hanken Grotesk" font-weight="600" font-size="22" fill="{PET}">{txt}</text>'
    marks = t(ox + W2/2, oy + pad*s/2 + 8, "2x") + t(ox + W2/2, oy + H2 - pad*s/2 + 8, "2x") + t(ox + pad*s/2, oy + H2/2 + 8, "2x") + t(ox + W2 - pad*s/2, oy + H2/2 + 8, "2x")
    Wt, Ht = int(W2 + 2*ox), int(H2 + 2*oy)
    body = f'<svg width="{Wt}" height="{Ht}" xmlns="http://www.w3.org/2000/svg" style="background:{HUE}">{zone}{logo}{marks}</svg>'
    shot(page(body, HUE), "img/espacio.png", Wt, Ht)
    print("espacio", Wt, Ht)

# ---------- usos incorrectos ----------
if want("incorrecto"):
    w, h = 480, 240
    def card(inner, fn, bg=HUE):
        shot(center(inner, w, h, bg), f"img/{fn}.png", w, h)
    base = lambda L, hh=120, extra="": inl(L, h=hh, extra=extra)
    card(inl(layers(WS, "color"), h=70, w=420, extra='preserveAspectRatio="none" '), "x_deformar")
    card(base(color(P, ink="#C44E14", eye="#FFD37F", accent="#F9A350") + [(WS, "#C44E14")]), "x_recolorear")
    grad = '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d7a92"/><stop offset="1" stop-color="#0a2530"/></linearGradient></defs>'
    s_ = lk.svg(layers(WS, "color"))
    s_ = s_.replace(f'fill="{PET}"', 'fill="url(#g)"').replace("<title>", grad + "<title>", 1).replace("<svg ", '<svg height="120" style="filter:drop-shadow(6px 8px 6px rgba(0,0,0,.45))" ', 1)
    card(s_, "x_efectos")
    sym_only = inl(color(P), h=120)
    card(f'<div style="display:flex;align-items:center;gap:22px">{sym_only}<div style="font-family:\'DejaVu Serif\';font-style:italic;font-size:44px;line-height:1.05;color:{PET}">Gabinete<br>Contable</div></div>', "x_fuente")
    card(base(layers(WS, "color")[:0] + [(SYM, AMB), (WS, AMB)]), "x_ambar")
    noeq = [(P["body"], PET), (P["eyes"], HUE), (P["pup"], PET), (P["beak"], AMB), (WS, PET)]
    card(base(noeq), "x_igual")

# ---------- combinaciones ----------
if want("combinaciones"):
    w, h = 380, 214
    for fn, sch, bg in (("c_hueso", "color", HUE), ("c_petroleo", "negativo", PET), ("c_blanco", "tinta", "#FFFFFF"), ("c_ambar", "sobre-ambar", AMB)):
        shot(center(inl(layers(WS, sch), h=96), w, h, bg), f"img/{fn}.png", w, h)

# ---------- antes / ahora ----------
if want("antes"):
    old = "antes_original.png"  # ícono anterior que usaba la web
    import shutil; shutil.copy(old, "img/_old.png")
    shot(center(f'<img src="file://{HERE}/img/_old.png" style="width:300px">', 520, 420, "#FFFFFF"), "img/antes.png", 520, 420)
    shot(center(inl(color(P), h=300), 520, 420, HUE), "img/ahora.png", 520, 420)

# ---------- grafismo: sello ----------
if want("grafismo"):
    shot(center(inl(layers(None, "petroleo"), h=150), 300, 300, "#FFFFFF"), "img/sello.png", 300, 300)
