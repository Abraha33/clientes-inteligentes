# Política de anonimización

Procedimiento para convertir datos reales de clientes en ejemplos públicos seguros.

## Reglas generales

- Los datos anonimizados no deben permitir reconstruir la identidad del cliente original.
- La anonimización debe ser irreversible.
- No usar datos reales como base para generar ejemplos "modificados".
- Siempre verificar con `scripts/validate_no_sensitive_data.py` antes de publicar.

## Tabla de transformación

| Campo real | Transformación | Ejemplo |
|---|---|---|
| Nombre del cliente | `Cliente Demo {N}` | `Restaurante El Sabor` → `Cliente Demo 001` |
| NIT / CC / RUC | `DOC-DEMO-{N}` | `20123456789` → `DOC-DEMO-001` |
| Teléfono | `3000000000` + correlativo | `+57 311 555 1234` → `3000000000` |
| Correo electrónico | `cliente{N}@example.com` | `juan@empresa.com` → `cliente001@example.com` |
| Dirección exacta | Calle/Carrera genérica + barrio ficticio | `Av. Siempre Viva 742` → `Calle Ejemplo 123, Centro Ficticio` |
| Coordenadas exactas | `null` o coordenadas aproximadas de zona demo | `-12.046374, -77.042793` → `null` |
| Valor financiero | Entero sin decimales | `3,750.50` → `3750` |
| Historial de compras | Fechas desplazadas, productos genéricos | Productos reales → `Pollo Entero`, `Pechuga`, `Alas` |

## Procedimiento paso a paso

1. Identifica los campos sensibles en el registro original.
2. Reemplaza cada campo según la tabla de transformación.
3. No conserves ningún valor original, ni siquiera ofuscado.
4. Verifica que el resultado no contenga:
   - Dominios de correo reales (solo `example.com`, `example.org`, `test.pe`).
   - Prefijos telefónicos reales.
   - Números de documento reales.
   - Direcciones reales.
5. Guarda el resultado en `data/examples/`.
6. Ejecuta `python scripts/validate_no_sensitive_data.py` para confirmar.

## Procedimiento automatizado (futuro)

```python
# Pseudocódigo para script de anonimización
def anonimizar(cliente: dict, idx: int) -> dict:
    cliente["identificacion"]["nombre"] = f"Cliente Demo {idx:03d}"
    cliente["identificacion"]["numero_documento"] = f"DOC-DEMO-{idx:03d}"
    cliente["contacto"]["telefono"] = f"300000000{idx}"
    cliente["contacto"]["email"] = f"cliente{idx:03d}@example.com"
    cliente["ubicacion"]["direccion"] = "Dirección de ejemplo genérica"
    cliente["ubicacion"]["latitud"] = None
    cliente["ubicacion"]["longitud"] = None
    if "ventas" in cliente and "total_ventas" in cliente["ventas"]:
        cliente["ventas"]["total_ventas"] = round(cliente["ventas"]["total_ventas"], -2)
    return cliente
```

> **Nota:** Este script aún no está implementado. No ejecutar sobre datos reales sin revisión manual.
