# Estructura local privada (no versionada)

Los datos reales de clientes nunca deben subirse al repositorio público.
Se recomienda mantener la siguiente estructura únicamente en el computador del usuario:

```
data/private/
├── clientes/
│   ├── customers_real.xlsx           # Exportación real de Wappsi
│   ├── clientes_historico.csv        # Histórico de clientes
│   └── fichas_clientes.pdf           # Fichas detalladas
├── informes_ventas/
│   ├── ventas_2026_q1.csv            # Ventas trimestre 1
│   ├── ventas_2026_q2.xlsx           # Ventas trimestre 2
│   └── cliente_001.txt               # Informe individual
├── processed/
│   ├── clientes_master_real.json     # Base maestra con datos reales
│   ├── clientes_mapa_real.json       # Datos para mapa (reales)
│   └── clientes_marketing_real.json  # Segmentación real
└── config/
    ├── .env                          # Variables de entorno locales
    └── api_keys.json                 # Claves de API (nunca versionar)
```

## Reglas

- Esta carpeta `data/private/` está ignorada por `.gitignore`.
- No crear archivos dentro de `data/private/` que deban compartirse.
- No mover archivos de `data/private/` a `data/examples/`.
- Si necesitas compartir datos, anonimízalos primero (ver `docs/politica_anonimizacion.md`).
- Los scripts del proyecto leen por defecto desde `data/private/` cuando se ejecutan localmente.

## Flujo de trabajo local

1. Coloca los archivos reales en `data/private/clientes/` o `data/private/informes_ventas/`.
2. Ejecuta los scripts apuntando a `data/private/`:
   ```
   python scripts/parse_clientes.py --input data/private/clientes/customers_real.xlsx --output data/private/processed/clientes_master_real.json
   ```
3. Los resultados se guardan en `data/private/processed/`.
4. Para compartir ejemplos, copia los datos anonimizados a `data/examples/`.
5. Siempre ejecuta `scripts/validate_no_sensitive_data.py` antes de hacer commit.
