"""
parse_clientes.py

Propósito: Parsear datos crudos de clientes exportados desde Wappsi
y convertirlos al formato JSON maestro definido en docs/modelo_datos.md.

Los datos reales deben residir en data/private/ y NO ser versionados.

Uso:
    python scripts/parse_clientes.py --input data/private/clientes/customers_real.xlsx --output data/private/processed/clientes_master_real.json

TODO:
    - Implementar parser según el formato de exportación de Wappsi (CSV, Excel, etc.)
    - Mapear columnas de Wappsi a los campos del modelo maestro
    - Validar datos obligatorios (nombre, documento, dirección)
    - Detectar y reportar duplicados
    - Manejar caracteres especiales y codificación UTF-8
"""

import json
import argparse
import sys
import os


RUTA_DEFECTO_INPUT = "data/private/clientes"
RUTA_DEFECTO_OUTPUT = "data/private/processed"


def parse_clientes(input_path: str) -> list[dict]:
    """
    Lee un archivo crudo de Wappsi y retorna una lista de diccionarios
    con la estructura parcial del modelo maestro.

    Args:
        input_path: Ruta al archivo de entrada.

    Returns:
        Lista de clientes parseados.
    """
    # TODO: Implementar parseo real según formato de Wappsi
    clientes = []
    return clientes


def guardar_json(clientes: list[dict], output_path: str) -> None:
    """
    Guarda la lista de clientes en un archivo JSON.

    Args:
        clientes: Lista de clientes a guardar.
        output_path: Ruta del archivo de salida.
    """
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parsea datos crudos de Wappsi a JSON maestro"
    )
    parser.add_argument(
        "--input", "-i",
        default=os.path.join(RUTA_DEFECTO_INPUT, "customers_real.xlsx"),
        help=f"Ruta al archivo crudo de Wappsi (default: {RUTA_DEFECTO_INPUT}/customers_real.xlsx)"
    )
    parser.add_argument(
        "--output", "-o",
        default=os.path.join(RUTA_DEFECTO_OUTPUT, "clientes_master_real.json"),
        help=f"Ruta del archivo JSON de salida (default: {RUTA_DEFECTO_OUTPUT}/clientes_master_real.json)"
    )
    args = parser.parse_args()

    clientes = parse_clientes(args.input)
    guardar_json(clientes, args.output)
    print(f"Procesados {len(clientes)} clientes. Guardado en {args.output}")


if __name__ == "__main__":
    main()
