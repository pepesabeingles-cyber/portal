import os, shutil, logo_kit as lk
from sereno import *
OUT = "out5/marca"
shutil.rmtree("out5", ignore_errors=True)
for sub in ("svg", "png", "iconos"): os.makedirs(f"{OUT}/{sub}", exist_ok=True)
PAD = 2 * X
LOCKS = {"vertical": WV, "horizontal": WH, "simbolo": None}
for name, word in LOCKS.items():
    for sc in ("color", "negativo", "oro", "tinta", "hueso", "blanco"):
        s = lk.svg(layers(word, sc), pad=PAD, title=f"Gabinete Contable · {name} · {sc}")
        open(f"{OUT}/svg/gc_{name}_{sc}.svg", "w").write(s)
        if sc in ("color", "negativo", "tinta", "hueso"):
            for w in (1024, 2048):
                lk.export_png(s, f"{OUT}/png/gc_{name}_{sc}_{w}.png", w if name != "simbolo" else w // 2)
for sc, ink in (("petroleo", PET), ("oro", ORO), ("tinta", TIN), ("hueso", HUE)):
    open(f"{OUT}/svg/gc_simbolo-reducido_{sc}.svg", "w").write(lk.svg([(SMALL, ink)], pad=X, title="Gabinete Contable · símbolo reducido"))
def tile(sym, size, pad_ratio, radius, fn_svg=None, fn_png=None, px=512, bg=PET, fg=ORO):
    b = lk.bounds(sym); sw, sh = b[2] - b[0], b[3] - b[1]
    s = size * (1 - 2 * pad_ratio) / max(sw, sh)
    t = lk.scale(lk.move(sym, -b[0], -b[1]), s)
    t = lk.move(t, (size - sw * s) / 2, (size - sh * s) / 2)
    svg = lk.svg([(lk.rect(0, 0, size, size, size * radius), bg), (t, fg)], box=(0, 0, size, size), title="Gabinete Contable")
    if fn_svg: open(fn_svg, "w").write(svg)
    if fn_png: lk.export_png(svg, fn_png, px)
tile(SMALL, 32, 0.1, 0.18, f"{OUT}/iconos/favicon.svg")
for px in (32, 180, 512):
    tile(SMALL if px <= 32 else SYM, 512, 0.1 if px <= 32 else 0.26, 0, fn_png=f"{OUT}/iconos/gc_icono_{px}.png", px=px)
tile(SYM, 1080, 0.3, 0, f"{OUT}/iconos/gc_avatar.svg", f"{OUT}/iconos/gc_avatar_1080.png", 1080)
print(len(os.listdir(f"{OUT}/svg")), len(os.listdir(f"{OUT}/png")), sorted(os.listdir(f"{OUT}/iconos")))
