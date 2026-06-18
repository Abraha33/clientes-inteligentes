# Privacidad y manejo de datos

## Datos considerados sensibles

Cualquier información que permita identificar directa o indirectamente a un cliente real de Envax debe tratarse como sensible:

- NIT / CC / RUC / número de documento.
- Teléfonos fijos y móviles.
- Correos electrónicos.
- Direcciones exactas (incluyendo coordenadas).
- Nombres completos de personas naturales.
- Saldos pendientes y datos de cartera.
- Historial de compras por cliente.
- Informes de ventas reales.
- Datos fiscales o tributarios.
- Coordenadas exactas de ubicación.
- Notas internas que referencien a personas identificables.

## Por qué no deben subirse al repositorio

Este repositorio es **público**. Subir datos reales de clientes expone información sensible a terceros, lo cual puede:

- Violar la privacidad de los clientes.
- Incumplir regulaciones de protección de datos.
- Generar riesgos legales y reputacionales.
- Facilitar uso malintencionado de la información.

## Carpetas prohibidas para datos reales

Las siguientes carpetas están en `.gitignore` y **no deben contener archivos versionados**:

| Carpeta | Motivo |
|---|---|
| `data/raw/` | Datos crudos exportados de Wappsi |
| `data/manual/` | Clasificaciones manuales con datos reales |
| `data/private/` | Carpeta local para datos reales (no versionada) |
| `data/processed/` | JSONs generados con datos reales |
| `data/exports/` | Exportaciones varias |
| `data/wappsi_real/` | Respaldo de datos de Wappsi |
| `data/informes_reales/` | Informes de ventas reales |

La **única** carpeta que puede contener datos en el repositorio es `data/examples/`, y solo con información completamente ficticia.

## Cómo trabajar con datos reales localmente

1. Coloca los archivos reales en `data/private/` siguiendo la estructura de `docs/estructura_local_privada.md`.
2. Ejecuta los scripts apuntando a `data/private/` para procesarlos.
3. Los resultados procesados se guardan en `data/private/processed/`.
4. Nunca muevas archivos de `data/private/` a `data/examples/`.

## Cómo compartir solo ejemplos anonimizados

1. Toma los datos reales de `data/private/`.
2. Aplica las reglas de anonimización de `docs/politica_anonimizacion.md`.
3. Guarda el resultado anonimizado en `data/examples/`.
4. Verifica que no queden datos reales con `scripts/validate_no_sensitive_data.py`.

## Excepciones

- No se permite compartir datos reales con terceros sin autorización explícita de Envax.
- No se permite usar datos reales en ejemplos, demos o presentaciones públicas.
- Los scripts pueden procesar datos reales desde `data/private/`, pero sus salidas no deben publicarse sin anonimizar.
