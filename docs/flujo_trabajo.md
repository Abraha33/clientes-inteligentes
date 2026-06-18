# Flujo de trabajo

## Diagrama del flujo

```
Usuario (conversación en lenguaje natural)
        │
        ▼
ChatGPT limpia y estructura la información
        │
        ▼
OpenCode actualiza JSON y documentación
        │
        ▼
Se cruzan datos con Wappsi e informes de ventas
        │
        ▼
Se genera JSON para mapa, marketing y cartera
```

## Paso 1 — Dictado del usuario

El usuario conversa con ChatGPT en lenguaje natural y dicta información sobre clientes: nombre, dirección, teléfono, tipo de comercio, observaciones, etc.

Ejemplo:

> "El cliente Juan Pérez de la ferretería 'El Martillo' en la Av. Siempre Viva 456, compra pollo cada 15 días."

## Paso 2 — Limpieza y estructuración (ChatGPT)

ChatGPT procesa el texto del usuario y lo convierte en un JSON estructurado según el modelo de datos (`docs/modelo_datos.md`). La clasificación manual se almacena en `data/manual/clientes_clasificacion_manual.json`.

## Paso 3 — Actualización de JSON (OpenCode)

OpenCode toma la salida de ChatGPT y actualiza:

- `data/manual/clientes_clasificacion_manual.json` — nuevas clasificaciones.
- `data/processed/clientes_master.json` — registro maestro unificado.
- Documentación si es necesario.

## Paso 4 — Cruce con fuentes de datos

Los registros maestros se enriquecen cruzando:

- **Wappsi**: lista de clientes, datos de contacto e IDs.
- **Informes de ventas**: historial de compras, montos, frecuencias.

Este cruce se realiza mediante los scripts en `scripts/`:

| Script | Propósito |
|---|---|
| `parse_clientes.py` | Parsear datos crudos de Wappsi |
| `merge_clientes_ventas.py` | Fusionar clientes con ventas |
| `geocode_clientes.py` | Geocodificar direcciones (futuro) |
| `build_mapa_json.py` | Construir JSON para mapa comercial |

## Paso 5 — Generación de salidas

Con los datos completos se generan:

- `clientes_mapa.json` — datos listos para visualización en mapa.
- `clientes_marketing.json` — datos listos para segmentación y campañas.
- (Futuro) JSON para rutas de visita y cartera.

## Consideraciones

- Cada paso puede iterarse múltiples veces.
- La clasificación manual del usuario tiene prioridad sobre la automatizada.
- Los datos de ventas se actualizan según la periodicidad de los informes.
- No se conectan APIs externas en esta fase inicial.
