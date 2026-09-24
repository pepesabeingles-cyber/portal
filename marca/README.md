# Gabinete Contable · Identidad

Manual de marca: https://claude.ai/artifact/GMjPyEie1hh3dhzVC9cmtm

## La idea

Un búho de verdad. El símbolo es un búho americano (Bubo virginianus), especie
que también vive en Bolivia, dibujado como un grabado de historia natural:
penachos, disco facial, pecho barrado, alas plegadas y posado en una rama.
Mira tranquilo y atento: el párpado apenas baja y las cejas son suaves. El iris
es el único toque de oro.

El nombre, GABINETE / CONTABLE en Bodoni Moda, lleva la marca; el búho la
acompaña.

## Archivos

| Carpeta | Contenido |
|---|---|
| `svg/` | Maestros en curvas: `vertical` (principal: búho sobre el nombre), `horizontal` (búho a la izquierda del nombre) y `simbolo` (el búho), en `color`, `negativo`, `oro`, `tinta`, `hueso` y `blanco`; `simbolo-reducido` (silueta, disco facial y ojos, sin barrado) para 16–32 px. |
| `png/` | Los mismos, transparentes, a 1024 y 2048 px. |
| `iconos/` | `favicon.svg`, avatar de 1080 px e íconos de 32, 180 y 512 px (búho hueso con iris en oro sobre petróleo). |
| `manual/` | Imágenes usadas en el manual. |
| `presentacion/` | Láminas de presentación del logo. |
| `fuente/` | Scripts que generan todo lo anterior (`real2.py` dibuja el búho; `identidad.py` arma los logotipos). |

- `color`: búho y nombre en petróleo, iris en oro, sobre hueso o blanco.
- `negativo`: búho y nombre en hueso, iris en oro, sobre petróleo.
- `oro`: búho en oro con ojos en petróleo, sobre petróleo.
- La versión horizontal usa el corte de texto de Bodoni (opsz 11, 600) para
  aguantar tamaños pequeños; la principal usa el corte display (opsz 18, 500).

## Color

| Nombre | HEX | Uso |
|---|---|---|
| Petróleo | `#134150` | Nombre, búho y fondos de autoridad. 9,7:1 con hueso. |
| Oro viejo | `#C2A36B` | El iris del búho y un solo acento por pieza. 4,6:1 sobre petróleo. Nunca texto sobre fondos claros. |
| Hueso | `#F4F0E8` | Papel y fondo base. |
| Tinta | `#14252B` | Texto. 14:1 sobre hueso. |

## Tipografía

- Bodoni Moda: nombre y titulares. En curvas dentro del logo.
- Jost: texto, datos y etiquetas.
- Ambas con licencia OFL.

## Uso

- Zona de protección: 2x por lado; x es un sexto del ancho del búho.
- Mínimos: principal 160 px de ancho (40 mm), horizontal 44 px de alto (12 mm),
  búho completo 48 px (15 mm); de 16 a 32 px, el reducido.
- No deformar, recolorear, agregar sombras o degradados, reescribir el nombre
  con otra fuente, agrandar el búho ni poner el oro sobre fondos claros.

## Regenerar

```bash
cd marca/fuente
pip install fonttools uharfbuzz skia-pathops brotli playwright numpy scipy pillow
npm install
python3 export7.py   # maestros e íconos en out7/marca
python3 boards6.py   # láminas en board/
python3 deckimg.py   # imágenes del manual en dimg/
```
