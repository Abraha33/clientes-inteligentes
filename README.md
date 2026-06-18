# clientes-inteligentes-envax

Base comercial inteligente de clientes para Envax.

## ¿Qué es?

Una base de datos estructurada, documentada y procesable de los clientes de Envax, construida a partir de:

1. Lista de clientes de Wappsi.
2. Ficha detallada del cliente.
3. Informe de ventas por cliente.
4. Clasificación manual dictada por el usuario.
5. Dirección normalizada, barrio, ciudad, tipo de comercio y subtipo.

## ¿Qué problema resuelve?

Envax necesita centralizar, normalizar y enriquecer la información de sus clientes para poder tomar decisiones comerciales basadas en datos. Actualmente los datos están dispersos en Wappsi, informes de ventas y conocimiento del usuario. Este proyecto los unifica en un modelo JSON maestro que permite:

- Segmentación comercial.
- Generación de rutas de visita.
- Marketing dirigido.
- Análisis de cartera.
- Visualización en mapa comercial.

## ¿Qué datos usa?

| Fuente | Descripción |
|---|---|
| Wappsi | Lista de clientes con datos de contacto y ubicación |
| Informes de ventas | Historial de compras por cliente |
| Clasificación manual | Categorización dictada por el usuario vía ChatGPT |
| Dirección normalizada | Datos de barrio, ciudad, tipo y subtipo de comercio |

## ¿Qué archivos se generan?

| Archivo | Contenido |
|---|---|
| `data/examples/clientes_ejemplo.json` | Ejemplo ficticio de clientes (público) |
| `data/examples/informe_ventas_ejemplo.json` | Ejemplo ficticio de ventas (público) |
| `data/examples/clientes_mapa_ejemplo.json` | Ejemplo ficticio de mapa (público) |
| `data/private/clientes/` | Datos reales de Wappsi (local, no versionado) |
| `data/private/informes_ventas/` | Informes reales de ventas (local, no versionado) |
| `data/private/processed/` | JSONs reales procesados (local, no versionado) |

## ¿Qué NO hace todavía?

- No tiene un mapa visual funcional.
- No consume APIs externas (geocodificación, maps).
- No tiene interfaz web ni app interactiva.
- No realiza scraping automatizado.
- No tiene lógica compleja de segmentación implementada.

El objetivo inicial no es un mapa bonito, sino una **base comercial inteligente** que sirva como cimiento para todo lo demás.

## Modo repositorio público seguro

Este repositorio está diseñado para ser público. No debe contener datos reales de clientes.

- Los datos reales deben guardarse únicamente fuera de Git, en `data/private/` (carpeta ignorada por `.gitignore`).
- Las exportaciones reales de Wappsi, Excel, CSV, PDF, HTML o informes de ventas no deben subirse.
- El repositorio solo debe contener **código, documentación, plantillas y ejemplos ficticios**.
- La carpeta `data/examples/` es la única que puede incluir datos en el repositorio, y deben ser completamente inventados.

## Privacidad y manejo de datos reales

Este proyecto puede manejar información sensible de clientes (NIT/CC, teléfonos, correos, direcciones, saldos, historial de compras).

- **No se deben subir datos reales a un repositorio público.**
- Los archivos reales deben mantenerse en `data/private/`, fuera de Git.
- Antes de compartir el proyecto, se debe revisar que no existan datos reales versionados.

Ver:
- `docs/privacidad_datos.md` — política completa de privacidad.
- `docs/estructura_local_privada.md` — estructura recomendada para datos reales locales.
- `docs/checklist_antes_commit.md` — lista de verificación pre-commit.
- `docs/politica_anonimizacion.md` — procedimiento de anonimización.
- `.gitignore` — reglas para excluir datos sensibles.
- `scripts/validate_no_sensitive_data.py` — escáner de seguridad pre-commit.
