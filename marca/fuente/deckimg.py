import shutil, logo_kit as lk
from PIL import Image
from identidad import *
from identidad import _place
from real2 import owl_small
from shot import shot, HERE
M = f"file://{HERE}/out7/marca"
def inl(L, h=None, w=None, extra=""):
    s = lk.svg(L); a = (f'height="{h}" ' if h else "") + (f'width="{w}" ' if w else "") + extra
    return s.replace("<svg ", f"<svg {a}", 1)
CSS = f"body{{font-family:'Jost';color:{TIN}}} .serif{{font-family:'Bodoni Moda'}}"
def page(body, bg): return f"<html><head><style>{CSS}</style></head><body style='background:{bg}'>{body}</body></html>"
def center(inner, w, h, bg): return page(f'<div style="width:{w}px;height:{h}px;display:flex;align-items:center;justify-content:center;background:{bg}">{inner}</div>', bg)

shutil.copy("out7/marca/png/gc_vertical_negativo_2048.png", "dimg/d_portada.png")
Image.open("board/02_idea.png").crop((0, 120, 1900, 1760)).save("dimg/d_idea.png")
shutil.copy("board/05_tarjeta_placa.png", "dimg/d_app1.png"); shutil.copy("board/06_papeleria_web.png", "dimg/d_app2.png")
shutil.copy("../manual/d_antes.png", "dimg/d_antes.png")  # ícono anterior (Flaticon), solo como referencia
shot(center(inl(layers(None, "color"), h=340), 520, 420, HUE), "dimg/d_ahora.png", 520, 420)

# detalle: completo, reducido y una tinta
sm = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px">{inl([(SMALL, PET)], h=s)}<span style="font-size:13px;color:{NIE}">{s} px</span></div>' for s in (16, 24, 32))
body = f'''<div style="width:1500px;height:620px;background:{HUE};display:flex;align-items:flex-end;justify-content:space-around;padding:40px 40px 50px">
  <div style="display:flex;flex-direction:column;align-items:center;gap:18px">{inl(layers(None,"color"), h=470)}<span style="font-size:18px;letter-spacing:3px;color:{NIE}">COMPLETO · DESDE 48 PX</span></div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:18px">{inl([(SMALL, PET)], h=300)}<span style="font-size:18px;letter-spacing:3px;color:{NIE}">REDUCIDO · 16 A 32 PX</span></div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:18px"><div style="display:flex;gap:26px;align-items:flex-end">{sm}</div><span style="font-size:18px;letter-spacing:3px;color:{NIE}">TAMAÑO REAL</span></div></div>'''
shot(page(body, HUE), "dimg/d_detalle.png", 1500, 620)

# versiones
for fn, inner in (("d_v_principal", inl(layers(WV, "color"), h=250)), ("d_v_horizontal", inl(layers(WH, "color"), w=330)),
                  ("d_v_buho", inl(layers(None, "color"), h=250)),
                  ("d_v_reducido", "".join(f'<span style="margin:0 14px">{inl([(SMALL, PET)], h=s)}</span>' for s in (16, 24, 32)) + f'<img src="{M}/iconos/favicon.svg" style="width:32px;margin-left:18px">')):
    shot(center(f'<div style="display:flex;align-items:flex-end">{inner}</div>', 380, 300, HUE), f"dimg/{fn}.png", 380, 300)

# espacio libre: 2x por lado, x = 1/6 del ancho del búho
Lv = layers(WV, "color"); allb = lk.bounds(lk.union(*[p for p, _ in Lv]))
x = (OB[2] - OB[0]) / 6 * (lk.bounds(V_OWL[0])[3] - lk.bounds(V_OWL[0])[1]) / (OB[3] - OB[1])
pad = 2 * x; s = 1.0
x0, y0, x1, y1 = allb[0] - pad, allb[1] - pad, allb[2] + pad, allb[3] + pad
W_, H_ = x1 - x0, y1 - y0; k = 560 / H_
paths = "".join(f'<path fill="{c}" d="{lk.d(p)}" transform="translate({-x0*k + 40},{-y0*k + 30}) scale({k})"/>' for p, c in Lv)
zone = (f'<rect x="40" y="30" width="{W_*k}" height="{H_*k}" fill="{PET}" fill-opacity=".07" stroke="{PET}" stroke-width="2" stroke-dasharray="8 6"/>'
        f'<rect x="{40 + pad*k}" y="{30 + pad*k}" width="{(W_-2*pad)*k}" height="{(H_-2*pad)*k}" fill="none" stroke="{PET}" stroke-opacity=".45" stroke-width="1.5"/>')
t = lambda xx, yy, s_: f'<text x="{xx}" y="{yy}" text-anchor="middle" font-family="Jost" font-size="22" fill="{PET}">{s_}</text>'
marks = t(40 + W_*k/2, 30 + pad*k/2 + 8, "2x") + t(40 + W_*k/2, 30 + H_*k - pad*k/2 + 8, "2x") + t(40 + pad*k/2, 30 + H_*k/2, "2x") + t(40 + W_*k - pad*k/2, 30 + H_*k/2, "2x")
Wt, Ht = int(W_*k + 80), int(H_*k + 60)
shot(page(f'<svg width="{Wt}" height="{Ht}" xmlns="http://www.w3.org/2000/svg">{zone}{paths}{marks}</svg>', HUE), "dimg/d_espacio.png", Wt, Ht)
print("espacio", Wt, Ht)

# usos incorrectos
w, h = 480, 240
def card(inner, fn, bg=HUE): shot(center(inner, w, h, bg), f"dimg/{fn}.png", w, h)
card(inl(layers(WH, "color"), h=80, w=420, extra='preserveAspectRatio="none" '), "x_deformar")
brown = [(p, {PET: "#7A4A1E", HUE: "#FFD37F", ORO: "#E07B22"}.get(c, c)) for p, c in layers(WH, "color")]
card(inl(brown, w=380), "x_recolorear")
grad = '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d7a92"/><stop offset="1" stop-color="#0a2530"/></linearGradient></defs>'
s_ = lk.svg(layers(WH, "color")).replace(f'fill="{PET}"', 'fill="url(#g)"').replace("<title>", grad + "<title>", 1).replace("<svg ", '<svg width="380" style="filter:drop-shadow(6px 8px 6px rgba(0,0,0,.45))" ', 1)
card(s_, "x_efectos")
card(f'<div style="display:flex;align-items:center;gap:20px">{inl(owl_layers(H_OWL, "color"), h=120)}<div style="font-family:\'DejaVu Serif\';font-style:italic;font-size:40px;line-height:1.1;color:{PET}">Gabinete<br>Contable</div></div>', "x_fuente")
card(inl([(p, ORO) for p, _ in layers(WH, "color")], w=380), "x_oro")
big = owl_layers(_place(THS * 3.2, lambda b: BBS[0] - THS * 0.42 - b[2], lambda b: BBS[3] + THS * 0.08 - b[3]), "color") + [(BLOCK_S, PET)]
card(inl(big, h=200), "x_grande")

# combinaciones
for fn, sch, bg in (("c_hueso", "color", HUE), ("c_petroleo", "negativo", PET), ("c_blanco", "tinta", "#FFFFFF"), ("c_oro", "tinta", ORO)):
    shot(center(inl(layers(WH, sch), w=320), 380, 214, bg), f"dimg/{fn}.png", 380, 214)

# trama del plumaje (recurso gráfico)
marks = []
for j, yy in enumerate(range(18, 300, 16)):
    off = 11 if j % 2 else 0
    for xx in range(-10 + off, 1620, 22):
        marks.append(f'<path d="M{xx-8} {yy} C{xx-3} {yy-2.4} {xx+3} {yy+2.4} {xx+8} {yy}" stroke="{PET}" stroke-width="2" fill="none" stroke-linecap="round"/>')
band = lambda op, bg: f'<svg width="1600" height="300" xmlns="http://www.w3.org/2000/svg" style="background:{bg}"><g opacity="{op}">{"".join(marks)}</g></svg>'
shot(page(f'<div style="display:flex;flex-direction:column">{band(1, HUE)}{band(0.12, HUE)}</div>', HUE), "dimg/d_trama.png", 1600, 600)
