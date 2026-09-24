# Gabinete Contable · Identidad

## La idea

El nombre primero. La marca es Gabinete Contable en Bodoni Moda, en mayúsculas
espaciadas: GABINETE y CONTABLE, dos líneas del mismo ancho. El búho acompaña:
sus ojos, en calma (aro fino y pupila), están entre las dos palabras, sobre la
raya que en el libro contable separa y cierra las cuentas. La raya y los ojos
son el único acento; en negativo van en oro.

## Archivos

| Carpeta | Contenido |
|---|---|
| `svg/` | Maestros en curvas: `vertical` (principal: dos líneas con filete y ojos), `horizontal` (una línea: GABINETE ◦◦ CONTABLE) y `simbolo` (los ojos), en `color`, `negativo`, `oro`, `tinta`, `hueso` y `blanco`; `simbolo-reducido` (aro más grueso) para 16–32 px. |
| `png/` | Los mismos, transparentes, a 1024 y 2048 px. |
| `iconos/` | `favicon.svg`, avatar de 1080 px e íconos de 32, 180 y 512 px (ojos en oro sobre petróleo). |
| `presentacion/` | Láminas de presentación del logo. |
| `fuente/` | Scripts que generan todo lo anterior (`sereno.py` dibuja los ojos y arma los logotipos). |

- `color`: todo en petróleo, sobre hueso o blanco.
- `negativo`: nombre en hueso, filete y ojos en oro, solo sobre petróleo.
- La versión de una línea usa el corte de texto de Bodoni (opsz 11, 600) para
  aguantar tamaños pequeños; la principal usa el corte display (opsz 18, 500).

## Color

| Nombre | HEX | Uso |
|---|---|---|
| Petróleo | `#134150` | Nombre, filete, ojos y fondos de autoridad. 9,7:1 con hueso. |
| Oro viejo | `#C2A36B` | Un solo toque por pieza. 4,6:1 sobre petróleo. Nunca texto sobre fondos claros. |
| Hueso | `#F4F0E8` | Papel y fondo base. |
| Tinta | `#14252B` | Texto. 14:1 sobre hueso. |

## Tipografía

- Bodoni Moda: nombre y titulares. En curvas dentro del logo.
- Jost: texto, datos y etiquetas.
- Ambas con licencia OFL.

## Uso

- Zona de protección: dos diámetros de ojo por lado.
- Mínimos: principal 160 px de ancho (40 mm), una línea 150 px (38 mm).
  Los ojos solos, desde 32 px; de 16 a 32 px, el reducido.
- No deformar, recolorear, agregar sombras o degradados, reescribir el nombre
  con otra fuente, sacar los ojos del filete ni poner el oro sobre fondos claros.

## Regenerar

```bash
cd marca/fuente
pip install fonttools uharfbuzz skia-pathops brotli playwright numpy scipy pillow
npm install
python3 export5.py   # maestros e íconos en out5/marca
python3 boards4.py   # láminas en board/
```
