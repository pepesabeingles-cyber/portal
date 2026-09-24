import os, logo_kit as lk
from owl import *
OUT = "out/marca"
for sub in ("svg", "png", "iconos"): os.makedirs(f"{OUT}/{sub}", exist_ok=True)
PAD = 2 * X  # zona de protección incluida en el lienzo
LOCKS = {"apilada": WS, "horizontal": WH, "vertical": WV, "simbolo": None}
SCHEMES = ["color", "negativo", "tinta", "hueso", "blanco"]
made = []
for name, word in LOCKS.items():
    for sc in SCHEMES:
        s = lk.svg(layers(word, sc), pad=PAD, title=f"Gabinete Contable · {name} · {sc}")
        fn = f"{OUT}/svg/gc_{name}_{sc}.svg"; open(fn, "w").write(s); made.append(fn)
        if sc in ("color", "negativo", "tinta", "hueso"):
            for w in ((1024, 2048) if name != "simbolo" else (512, 1024)):
                lk.export_png(s, f"{OUT}/png/gc_{name}_{sc}_{w}.png", w)
# reducido
for sc, ink in (("tinta", TIN), ("petroleo", PET), ("hueso", HUE), ("ambar", AMB)):
    s = lk.svg([(SMALL, ink)], pad=X, title="Gabinete Contable · símbolo reducido")
    open(f"{OUT}/svg/gc_simbolo-reducido_{sc}.svg", "w").write(s)
# favicon y avatar: búho ámbar en campo petróleo
def tile(sym, size, pad_ratio, radius_ratio, fn_svg=None, fn_png=None, px=512):
    # lienzo cuadrado de 'size' unidades con el búho centrado ópticamente (un poco arriba)
    b = lk.bounds(sym); sw, sh = b[2]-b[0], b[3]-b[1]
    s = size * (1 - 2 * pad_ratio) / max(sw, sh)
    t = lk.scale(lk.move(sym, -b[0], -b[1]), s)
    tw, th = sw * s, sh * s
    t = lk.move(t, (size - tw) / 2, (size - th) / 2 - size * 0.01)
    bg = lk.rect(0, 0, size, size, size * radius_ratio)
    svg = lk.svg([(bg, PET), (t, AMB)], box=(0, 0, size, size), title="Gabinete Contable")
    if fn_svg: open(fn_svg, "w").write(svg)
    if fn_png: lk.export_png(svg, fn_png, px)
    return svg
tile(SMALL, 32, 0.12, 0.2, f"{OUT}/iconos/favicon.svg")
for px in (32, 180, 512):
    tile(SMALL if px <= 32 else SYM, 512, 0.14 if px <= 32 else 0.2, 0.0, fn_png=f"{OUT}/iconos/gc_icono_{px}.png", px=px)
tile(SYM, 1080, 0.24, 0.0, f"{OUT}/iconos/gc_avatar.svg", f"{OUT}/iconos/gc_avatar_1080.png", 1080)
print(len(os.listdir(f"{OUT}/svg")), len(os.listdir(f"{OUT}/png")), os.listdir(f"{OUT}/iconos"))
