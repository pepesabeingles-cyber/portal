# Gabinete Contable · Identidad

Manual de marca: https://claude.ai/artifact/GMjPyEie1hh3dhzVC9cmtm

## La idea

Un halcón de verdad. El símbolo es un halcón peregrino (Falco peregrinus),
especie que también vive en Bolivia, dibujado como un grabado de historia
natural: de perfil, con la capucha oscura y la bigotera que baja del ojo, la
garganta clara, el pecho barrado, el ala plegada y posado en una rama. Es el ave
que ve el detalle desde lejos: la mirada de quien revisa las cuentas. El anillo
del ojo es el único toque de oro.

El nombre, GABINETE / CONTABLE en Bodoni Moda, lleva la marca; el halcón la
acompaña.

## Archivos

| Carpeta | Contenido |
|---|---|
| `svg/` | Maestros en curvas: `vertical` (principal: halcón sobre el nombre), `horizontal` (halcón a la izquierda del nombre) y `simbolo` (el halcón), en `color`, `negativo`, `oro`, `tinta`, `hueso` y `blanco`; `simbolo-reducido` (la cabeza sola: capucha, bigotera, garganta y ojo, sin barrado) para 16–32 px. |
| `png/` | Los mismos, transparentes, a 1024 y 2048 px. |
| `iconos/` | `favicon.svg`, avatar de 1080 px e íconos de 32, 180 y 512 px (halcón hueso con el ojo en oro sobre petróleo; el favicon usa la cabeza reducida). |
| `manual/` | Imágenes usadas en el manual. |
| `presentacion/` | Láminas de presentación del logo. |
| `fuente/` | Scripts que generan todo lo anterior (`halcon.py` dibuja el halcón; `identidad.py` arma los logotipos). |

- `color`: halcón y nombre en petróleo, anillo del ojo en oro, sobre hueso o blanco.
- `negativo`: halcón y nombre en hueso, anillo del ojo en oro, sobre petróleo.
- `oro`: halcón en oro con el ojo en petróleo, sobre petróleo.
- La versión horizontal usa el corte de texto de Bodoni (opsz 11, 600) para
  aguantar tamaños pequeños; la principal usa el corte display (opsz 18, 500).

## Color

| Nombre | HEX | Uso |
|---|---|---|
| Petróleo | `#134150` | Nombre, halcón y fondos de autoridad. 9,7:1 con hueso. |
| Oro viejo | `#C2A36B` | El anillo del ojo del halcón y un solo acento por pieza. 4,6:1 sobre petróleo. Nunca texto sobre fondos claros. |
| Hueso | `#F4F0E8` | Papel y fondo base. |
| Tinta | `#14252B` | Texto. 14:1 sobre hueso. |

## Tipografía

- Bodoni Moda: nombre y titulares. En curvas dentro del logo.
- Jost: texto, datos y etiquetas.
- Ambas con licencia OFL.

## Uso

- Zona de protección: 2x por lado; x es un sexto del ancho del símbolo.
- Mínimos: principal 160 px de ancho (40 mm), horizontal 44 px de alto (12 mm),
  halcón completo 48 px (15 mm); de 16 a 32 px, el reducido.
- No deformar, recolorear, agregar sombras o degradados, reescribir el nombre
  con otra fuente, agrandar el halcón ni poner el oro sobre fondos claros.

## Regenerar

```bash
cd marca/fuente
pip install fonttools uharfbuzz skia-pathops brotli playwright numpy scipy pillow
npm install
python3 export7.py   # maestros e íconos en out7/marca
python3 boards6.py   # láminas en board/
python3 deckimg.py   # imágenes del manual en dimg/
```
