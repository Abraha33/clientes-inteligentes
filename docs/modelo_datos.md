# Modelo de datos — Cliente maestro

> **Nota de seguridad:** El modelo de datos presentado aquí representa información potencialmente sensible. Los ejemplos incluidos son completamente ficticios. No documentar clientes reales en ejemplos públicos. Para pruebas, usar siempre datos anonimizados siguiendo la política en `docs/politica_anonimizacion.md`.

Cada cliente se representa como un objeto JSON con las siguientes secciones.

## Estructura general

```json
{
  "identificacion": { ... },
  "contacto": { ... },
  "ubicacion": { ... },
  "clasificacion_manual": { ... },
  "ventas": { ... },
  "productos": { ... },
  "marketing": { ... },
  "riesgo": { ... },
  "control": { ... }
}
```

## identificacion

| Campo | Tipo | Descripción |
|---|---|---|
| id_cliente | string | Identificador único interno |
| id_wappsi | string | ID en Wappsi (si existe) |
| nombre | string | Nombre del cliente o razón social |
| tipo_documento | string | RUC, DNI, etc. |
| numero_documento | string | Número de documento |
| fecha_alta | string (date) | Fecha de alta en el sistema |

## contacto

| Campo | Tipo | Descripción |
|---|---|---|
| telefono | string | Teléfono principal |
| telefono_secundario | string | Teléfono alternativo |
| email | string | Correo electrónico |
| contacto_nombre | string | Nombre de la persona de contacto |
| contacto_cargo | string | Cargo de la persona de contacto |

## ubicacion

| Campo | Tipo | Descripción |
|---|---|---|
| direccion | string | Dirección completa |
| barrio | string | Barrio |
| ciudad | string | Ciudad |
| provincia | string | Provincia |
| codigo_postal | string | Código postal |
| latitud | float | Latitud (geocodificación futura) |
| longitud | float | Longitud (geocodificación futura) |
| tipo_comercio | string | Tipo de comercio (ej. Restaurante) |
| subtipo_comercio | string | Subtipo (ej. Parrilla) |

## clasificacion_manual

| Campo | Tipo | Descripción |
|---|---|---|
| categoria | string | Categoría asignada por el usuario |
| subcategoria | string | Subcategoría asignada |
| notas | string | Notas libres del usuario |
| fecha_clasificacion | string (date) | Fecha de la clasificación |
| clasificado_por | string | Quién clasificó (usuario, ChatGPT, etc.) |

## ventas

| Campo | Tipo | Descripción |
|---|---|---|
| total_ventas | number | Suma total de ventas |
| promedio_mensual | number | Promedio de ventas mensual |
| ultima_compra | string (date) | Fecha de la última compra |
| primera_compra | string (date) | Fecha de la primera compra |
| frecuencia_compras | number | Días promedio entre compras |
| total_ordenes | integer | Número total de órdenes |
| estado_comercial | string | Activo / Enfriándose / Dormido / Perdido |

## productos

| Campo | Tipo | Descripción |
|---|---|---|
| productos_frecuentes | array[string] | Productos que compra regularmente |
| categoria_predominante | string | Categoría de producto más comprada |
| ticket_promedio | number | Valor promedio por orden |

## marketing

| Campo | Tipo | Descripción |
|---|---|---|
| segmento | string | Segmento asignado (ej. alto_valor, recuperacion) |
| canal_preferido | string | Canal de contacto preferido |
| acepta_marketing | boolean | Consentimiento para marketing |
| ultima_campana | string | Nombre de la última campaña enviada |
| fecha_ultima_interaccion | string (date) | Fecha de última interacción de marketing |

## riesgo

| Campo | Tipo | Descripción |
|---|---|---|
| nivel_riesgo | string | Alto / Medio / Bajo |
| saldo_pendiente | number | Saldo pendiente si aplica |
| devoluciones | integer | Número de devoluciones |
| motivo_riesgo | string | Descripción del motivo |
| alertas | array[string] | Lista de alertas activas |

## control

| Campo | Tipo | Descripción |
|---|---|---|
| fecha_actualizacion | string (datetime) | Última actualización del registro |
| version | integer | Versión del registro |
| fuente_origen | string | Fuente de los datos (Wappsi, manual, etc.) |
| hash_integridad | string | Hash para verificar integridad (futuro) |

## Ejemplo ficticio

```json
{
  "identificacion": {
    "id_cliente": "CLI-0001",
    "id_wappsi": "WAP-12345",
    "nombre": "Restaurante El Sabor",
    "tipo_documento": "RUC",
    "numero_documento": "20123456789",
    "fecha_alta": "2025-01-15"
  },
  "contacto": {
    "telefono": "+51 999 888 777",
    "telefono_secundario": "+51 111 222 333",
    "email": "contacto@elsabor.pe",
    "contacto_nombre": "Carlos Pérez",
    "contacto_cargo": "Administrador"
  },
  "ubicacion": {
    "direccion": "Av. Principal 123",
    "barrio": "Centro",
    "ciudad": "Lima",
    "provincia": "Lima",
    "codigo_postal": "15001",
    "latitud": null,
    "longitud": null,
    "tipo_comercio": "Restaurante",
    "subtipo_comercio": "Parrilla"
  },
  "clasificacion_manual": {
    "categoria": "Restaurante",
    "subcategoria": "Parrilla",
    "notas": "Cliente frecuente, buen pagador",
    "fecha_clasificacion": "2026-06-10",
    "clasificado_por": "usuario"
  },
  "ventas": {
    "total_ventas": 45000.00,
    "promedio_mensual": 3750.00,
    "ultima_compra": "2026-06-15",
    "primera_compra": "2024-03-10",
    "frecuencia_compras": 15,
    "total_ordenes": 48,
    "estado_comercial": "Activo"
  },
  "productos": {
    "productos_frecuentes": ["Pollo Entero", "Pechuga", "Alas"],
    "categoria_predominante": "Pollos",
    "ticket_promedio": 937.50
  },
  "marketing": {
    "segmento": "alto_valor",
    "canal_preferido": "WhatsApp",
    "acepta_marketing": true,
    "ultima_campana": "Oferta_pollo_junio",
    "fecha_ultima_interaccion": "2026-06-14"
  },
  "riesgo": {
    "nivel_riesgo": "Bajo",
    "saldo_pendiente": 0.00,
    "devoluciones": 1,
    "motivo_riesgo": "",
    "alertas": []
  },
  "control": {
    "fecha_actualizacion": "2026-06-17T22:00:00Z",
    "version": 3,
    "fuente_origen": "Wappsi + manual",
    "hash_integridad": null
  }
}
```
