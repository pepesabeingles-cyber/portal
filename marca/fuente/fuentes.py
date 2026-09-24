"""Genera los cortes ópticos de Bodoni Moda usados en el logotipo (licencia OFL)."""
import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

SRC = "node_modules/@fontsource-variable/bodoni-moda/files/bodoni-moda-latin-standard-normal.woff2"
CORTES = {"fonts/bodoni-op18-w500.ttf": {"wght": 500, "opsz": 18},   # display: logo principal
          "fonts/bodoni-op11-w600.ttf": {"wght": 600, "opsz": 11}}   # texto: tamaños pequeños

def asegurar():
    os.makedirs("fonts", exist_ok=True)
    for fn, axes in CORTES.items():
        if not os.path.exists(fn):
            f = TTFont(SRC); f.flavor = None
            instancer.instantiateVariableFont(f, axes).save(fn)
