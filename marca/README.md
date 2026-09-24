# Gabinete Contable · Identidad

## La idea

Un búho que es también una plumilla. De frente es un búho: la mirada atenta
del que revisa. Como objeto es la plumilla de una pluma fuente, el instrumento
con el que el profesional firma el balance. El pico es el respiradero de la
plumilla (el único toque de oro), la ranura son las alas cerradas y la punta
es la firma.

El nombre va en Bodoni Moda, la letra que nació de la plumilla de punta fina:
el símbolo y la letra salen del mismo instrumento.

## Archivos

| Carpeta | Contenido |
|---|---|
| `svg/` | Maestros en curvas: `vertical` (principal), `horizontal` y `simbolo`, en `color`, `negativo`, `oro`, `tinta`, `hueso` y `blanco`; `simbolo-reducido` para 16–24 px. |
| `png/` | Los mismos, transparentes, a 1024 y 2048 px. |
| `iconos/` | `favicon.svg`, avatar de 1080 px e íconos de 32, 180 y 512 px (búho en oro sobre petróleo). |
| `presentacion/` | Láminas de presentación del logo. |
| `fuente/` | Scripts que generan todo lo anterior (`nib.py` dibuja el búho; `marca2.py` arma los logotipos). |

- `color`: búho petróleo con el pico en oro y nombre petróleo, sobre hueso o blanco.
- `negativo`: búho oro y nombre hueso, solo sobre petróleo.
- La versión horizontal usa el corte de texto de Bodoni (opsz 11, 600) para
  aguantar tamaños pequeños; la vertical usa el corte display (opsz 18, 500).

## Color

| Nombre | HEX | Uso |
|---|---|---|
| Petróleo | `#134150` | Búho, nombre y fondos de autoridad. 9,7:1 con hueso. |
| Oro viejo | `#C2A36B` | Un solo toque por pieza. 4,6:1 sobre petróleo. Nunca texto sobre fondos claros. |
| Hueso | `#F4F0E8` | Papel y fondo base. |
| Tinta | `#14252B` | Texto. 14:1 sobre hueso. |

## Tipografía

- Bodoni Moda: nombre y titulares. En curvas dentro del logo.
- Jost: texto, datos y etiquetas.
- Ambas con licencia OFL.

## Uso

- Módulo x = 1/12 del ancho del búho. Zona de protección: 2x por lado.
- Mínimos: vertical 120 px de ancho (30 mm), horizontal 140 px (35 mm), símbolo 24 px (8 mm).
  De 16 a 24 px, el símbolo reducido.
- No deformar, recolorear, agregar sombras o degradados, reescribir el nombre
  con otra fuente ni poner el oro sobre fondos claros.

## Regenerar

```bash
cd marca/fuente
pip install fonttools uharfbuzz skia-pathops brotli playwright numpy scipy pillow
npm install
python3 export3.py   # maestros e íconos en out3/marca
python3 boards.py    # láminas en board/
```
