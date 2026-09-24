# Gabinete Contable · Identidad

## La idea

La mirada del búho. Del búho queda solo lo esencial: los ojos, la mirada
atenta de quien revisa cada cifra. Cada ojo tiene un aro grueso, tres anillos
finos equidistantes (como el grabado de los billetes y títulos de valor) y una
pupila con brillo. Dos ojos, dos columnas: Debe y Haber.

El nombre va en Bodoni Moda: el aro grueso y los anillos finos repiten el
contraste de trazo grueso y fino de la letra.

## Archivos

| Carpeta | Contenido |
|---|---|
| `svg/` | Maestros en curvas: `vertical` (principal), `horizontal` y `simbolo` (los ojos), en `color`, `negativo`, `oro`, `tinta`, `hueso` y `blanco`; `simbolo-reducido` (aro y pupila, sin anillos) para 16–24 px. |
| `png/` | Los mismos, transparentes, a 1024 y 2048 px. |
| `iconos/` | `favicon.svg`, avatar de 1080 px e íconos de 32, 180 y 512 px (ojos en oro sobre petróleo). |
| `presentacion/` | Láminas de presentación del logo. |
| `fuente/` | Scripts que generan todo lo anterior (`marca.py` dibuja los ojos y arma los logotipos). |

- `color`: ojos y nombre en petróleo, sobre hueso o blanco.
- `negativo`: ojos en oro y nombre en hueso, solo sobre petróleo.
- La versión horizontal usa el corte de texto de Bodoni (opsz 11, 600) para
  aguantar tamaños pequeños; la vertical usa el corte display (opsz 18, 500).

## Color

| Nombre | HEX | Uso |
|---|---|---|
| Petróleo | `#134150` | Ojos, nombre y fondos de autoridad. 9,7:1 con hueso. |
| Oro viejo | `#C2A36B` | Un solo toque por pieza. 4,6:1 sobre petróleo. Nunca texto sobre fondos claros. |
| Hueso | `#F4F0E8` | Papel y fondo base. |
| Tinta | `#14252B` | Texto. 14:1 sobre hueso. |

## Tipografía

- Bodoni Moda: nombre y titulares. En curvas dentro del logo.
- Jost: texto, datos y etiquetas.
- Ambas con licencia OFL.

## Uso

- Zona de protección: el radio de un ojo por lado.
- Mínimos: vertical 120 px de ancho (30 mm), horizontal 150 px (38 mm), símbolo 32 px de ancho (10 mm).
  De 16 a 32 px, el símbolo reducido.
- No deformar, recolorear, agregar sombras o degradados, reescribir el nombre
  con otra fuente, mover el brillo de las pupilas ni poner el oro sobre fondos claros.

## Regenerar

```bash
cd marca/fuente
pip install fonttools uharfbuzz skia-pathops brotli playwright numpy scipy pillow
npm install
python3 export4.py   # maestros e íconos en out4/marca
python3 boards3.py   # láminas en board/
```
