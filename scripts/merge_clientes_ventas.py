"""
merge_clientes_ventas.py

Propósito: Fusionar los datos maestros de clientes con los informes
de ventas, enriqueciendo cada registro con historial de compras,
monto total, frecuencia y estado comercial.

Los datos reales deben residir en data/private/ y NO ser versionados.

Uso:
    python scripts/merge_clientes_ventas.py --clientes data/private/processed/clientes_master_real.json --ventas data/private/informes_ventas/ventas.csv --output data/private/processed/clientes_master_real.json

TODO:
    - Implementar lectura de informes de ventas (CSV, Excel, PDF)
    - Cruce por ID de cliente o documento
    - Cálculo de total_ventas, promedio_mensual, frecuencia_compras
    - Determinación de estado comercial según reglas de segmentación
    - Identificación de productos frecuentes
    - Manejo de clientes sin ventas registradas
"""

import json
import argparse
import sys
import os


RUTA_DEFECTO_CLIENTES = "data/private/processed/clientes_master_real.json"
RUTA_DEFECTO_VENTAS = "data/private/informes_ventas"
RUTA_DEFECTO_OUTPUT = "data/private/processed/clientes_master_real.json"


def cargar_clientes(path: str) -> list[dict]:
    """
    Carga la lista de clientes desde un archivo JSON.

    Args:
        path: Ruta al archivo clientes_master.json.

    Returns:
        Lista de clientes.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def merge_ventas(clientes: list[dict], ventas_path: str) -> list[dict]:
    """
    Cruza los clientes con el informe de ventas y enriquece los registros.

    Args:
        clientes: Lista de clientes maestro.
        ventas_path: Ruta al archivo de ventas.

    Returns:
        Lista de clientes enriquecida con datos de ventas.
    """
    # TODO: Implementar cruce con datos reales de ventas
    # - Leer informe de ventas
    # - Identificar columnas relevantes
    # - Agrupar ventas por cliente
    # - Calcular métricas (total, promedio, frecuencia, etc.)
    # - Actualizar campo ventas de cada cliente
    return clientes


def guardar_json(clientes: list[dict], output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fusiona clientes maestros con informes de ventas"
    )
    parser.add_argument(
        "--clientes", "-c",
        default=RUTA_DEFECTO_CLIENTES,
        help=f"Ruta al archivo clientes_master.json (default: {RUTA_DEFECTO_CLIENTES})"
    )
    parser.add_argument(
        "--ventas", "-v",
        default=os.path.join(RUTA_DEFECTO_VENTAS, "ventas.csv"),
        help=f"Ruta al archivo de informe de ventas (default: {RUTA_DEFECTO_VENTAS}/ventas.csv)"
    )
    parser.add_argument(
        "--output", "-o",
        default=RUTA_DEFECTO_OUTPUT,
        help=f"Ruta del archivo JSON de salida (default: {RUTA_DEFECTO_OUTPUT})"
    )
    args = parser.parse_args()

    clientes = cargar_clientes(args.clientes)
    clientes = merge_ventas(clientes, args.ventas)
    guardar_json(clientes, args.output)
    print(f"Actualizados {len(clientes)} clientes con ventas. Guardado en {args.output}")


if __name__ == "__main__":
    main()
