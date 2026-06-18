# Reglas de segmentación

Reglas iniciales para clasificar clientes según su comportamiento comercial.

## Estado comercial

Define el estado del cliente según el tiempo transcurrido desde su última compra.

| Estado | Días desde última compra | Descripción |
|---|---|---|
| Activo | 0 a 30 días | Compró recientemente |
| Enfriándose | 31 a 60 días | Comienza a mostrar desinterés |
| Dormido | 61 a 90 días | Riesgo alto de pérdida |
| Perdido | Más de 90 días | Cliente inactivo |

### Reglas de transición

- Un cliente **Activo** pasa a **Enfriándose** si no compra en 31 días.
- Un cliente **Enfriándose** pasa a **Dormido** si llega a 61 días sin comprar.
- Un cliente **Dormido** pasa a **Perdido** si supera los 90 días.
- Cualquier compra reinicia el contador y devuelve al cliente a **Activo**.

## Nivel de cliente

Clasificación basada en valor (volumen de compra) y frecuencia.

| Nivel | Criterio | Descripción |
|---|---|---|
| A | Alto valor y alta frecuencia | Cliente estrella: compra mucho y seguido |
| B | Valor medio | Cliente regular: compra consistente pero no destacada |
| C | Bajo valor | Cliente de bajo volumen de compra |
| D | Ocasional o débil | Cliente esporádico o de muy bajo valor |

### Criterios específicos (pendiente de ajuste con datos reales)

- **Nivel A**: ticket promedio > percentil 75 y frecuencia < 20 días.
- **Nivel B**: ticket promedio entre percentil 25 y 75, o frecuencia entre 20 y 40 días.
- **Nivel C**: ticket promedio < percentil 25, frecuencia > 40 días.
- **Nivel D**: una sola compra o compras muy espaciadas (> 90 días).

## Riesgo

Indicadores de riesgo que pueden activar alertas.

| Indicador | Descripción |
|---|---|
| Saldo pendiente alto | Cliente debe dinero o tiene facturas vencidas |
| Muchas devoluciones | Historial alto de devoluciones de producto |
| Mucho tiempo sin comprar | Cliente en estado Dormido o Perdido |
| Cliente sin clasificación | No tiene categoría asignada, puede estar mal clasificado |

### Niveles de riesgo

| Nivel | Criterio |
|---|---|
| Alto | 2 o más indicadores activos |
| Medio | 1 indicador activo |
| Bajo | 0 indicadores activos |

## Priorización para rutas de visita

Combinación de nivel de cliente y estado comercial para determinar prioridad.

| Prioridad | Combinación |
|---|---|
| Crítica | Nivel A + Activo |
| Alta | Nivel A + Enfriándose, Nivel B + Activo |
| Media | Nivel B + Enfriándose, Nivel C + Activo |
| Baja | Nivel C/D + Dormido/Perdido |
| Sin prioridad | Perdido sin recuperación posible |

## Notas

- Estas reglas son iniciales y se ajustarán con datos reales.
- La clasificación manual del usuario puede sobreescribir la segmentación automática.
- Los percentiles y umbrales se calcularán una vez se tengan datos suficientes en `clientes_master.json`.
