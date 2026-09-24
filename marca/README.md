# Gabinete Contable · Marca v2

Manual completo: https://claude.ai/artifact/GMjPyEie1hh3dhzVC9cmtm

## La idea

Un búho que cuadra las cuentas. Sus dos ojos son las dos columnas del libro,
Debe y Haber, y el signo igual del pecho dice que la cuenta cuadra. Es un
búho propio, dibujado a medida, que reemplaza al ícono de catálogo (Flaticon)
y al sello G de la versión 1.

Se conservan el nombre, la firma "Cada cuenta, explicada.", la paleta y las
tipografías de la web.

## Archivos

| Carpeta | Contenido |
|---|---|
| `svg/` | Maestros en curvas: `apilada`, `horizontal`, `vertical`, `simbolo` en `color`, `negativo`, `tinta`, `hueso` y `blanco`; `simbolo-reducido` para 16–24 px. |
| `png/` | Los mismos, transparentes, a 1024 y 2048 px (símbolo a 512 y 1024). |
| `iconos/` | `favicon.svg`, avatar de 1080 px e íconos de 32, 180 y 512 px (búho ámbar sobre petróleo). |
| `manual/` | Imágenes usadas en el manual. |
| `fuente/` | Scripts que generan todo lo anterior (`owl.py` define el búho y los logotipos). |

La versión `negativo` (búho ámbar y nombre hueso) va solo sobre petróleo.

## Color

| Nombre | HEX | Uso |
|---|---|---|
| Petróleo | `#134150` | Búho y fondos de autoridad. 9,98:1 con hueso. |
| Hueso | `#F6F3EC` | Fondo base. |
| Tinta | `#14252B` | Texto largo. 14,26:1 sobre hueso. |
| Ámbar | `#E2A13C` | Pico, igual y botones. Nunca texto sobre fondos claros (2,02:1). |

## Tipografía

Bricolage Grotesque 700 para titulares y logotipo (en curvas), Hanken Grotesk
para texto y tablas. Ambas con licencia OFL.

## Construcción y uso

- Módulo x = 1/12 del ancho del búho. Zona de protección: 2x por lado.
- Mínimos: apilada 32 px de alto (12 mm), horizontal 140 px de ancho (35 mm),
  símbolo 24 px (8 mm); de 16 a 24 px, usar el símbolo reducido.
- No deformar, recolorear, agregar efectos, reescribir el nombre con otra
  fuente ni quitar el igual del pecho.

## Regenerar

```bash
cd marca/fuente
pip install fonttools uharfbuzz skia-pathops brotli playwright numpy scipy pillow
npm install
python3 export.py   # maestros SVG/PNG e íconos en out/marca
```
