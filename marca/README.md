# Gabinete Contable · Identidad

## La idea

Un búho que acompaña. El nombre lleva la marca: GABINETE / CONTABLE en Bodoni
Moda, dos líneas del mismo ancho. El búho está a su lado, de pie y sereno:
esbelto, de mirada tranquila, con el disco facial y las alas plegadas trazados
con la línea fina de la letra, posado sobre una raya como la que cierra una
cuenta en el libro. En negativo, el búho va en oro sobre petróleo.

## Archivos

| Carpeta | Contenido |
|---|---|
| `svg/` | Maestros en curvas: `vertical` (principal: búho pequeño sobre el nombre), `horizontal` (búho a la izquierda del nombre) y `simbolo` (el búho), en `color`, `negativo`, `oro`, `tinta`, `hueso` y `blanco`; `simbolo-reducido` (sin líneas finas, ojos más grandes) para 16–24 px. |
| `png/` | Los mismos, transparentes, a 1024 y 2048 px. |
| `iconos/` | `favicon.svg`, avatar de 1080 px e íconos de 32, 180 y 512 px (búho en oro sobre petróleo). |
| `presentacion/` | Láminas de presentación del logo. |
| `fuente/` | Scripts que generan todo lo anterior (`buho.py` dibuja el búho; `final.py` arma los logotipos). |

- `color`: todo en petróleo, sobre hueso o blanco.
- `negativo`: nombre en hueso y búho en oro, solo sobre petróleo.
- La versión horizontal usa el corte de texto de Bodoni (opsz 11, 600) para
  aguantar tamaños pequeños; la principal usa el corte display (opsz 18, 500).

## Color

| Nombre | HEX | Uso |
|---|---|---|
| Petróleo | `#134150` | Nombre, búho y fondos de autoridad. 9,7:1 con hueso. |
| Oro viejo | `#C2A36B` | Un solo toque por pieza. 4,6:1 sobre petróleo. Nunca texto sobre fondos claros. |
| Hueso | `#F4F0E8` | Papel y fondo base. |
| Tinta | `#14252B` | Texto. 14:1 sobre hueso. |

## Tipografía

- Bodoni Moda: nombre y titulares. En curvas dentro del logo.
- Jost: texto, datos y etiquetas.
- Ambas con licencia OFL.

## Uso

- Zona de protección: el ancho del búho por lado.
- Mínimos: principal 160 px de ancho (40 mm), horizontal 32 px de alto (9 mm).
  El búho solo, desde 32 px de alto; de 16 a 24 px, el reducido.
- El búho nunca es más grande que el nombre en la versión principal.
- No deformar, recolorear, agregar sombras o degradados, reescribir el nombre
  con otra fuente, agrandar el búho ni poner el oro sobre fondos claros.

## Regenerar

```bash
cd marca/fuente
pip install fonttools uharfbuzz skia-pathops brotli playwright numpy scipy pillow
npm install
python3 export6.py   # maestros e íconos en out6/marca
python3 boards5.py   # láminas en board/
```
