"""
build_clientes_master.py

Propósito: Construir el archivo clientes_master.json combinando datos
de Wappsi, clasificación manual e informes de ventas. Es el orquestador
que llama a parse_clientes, merge_clientes_ventas y geocode_clientes.

Los datos reales deben residir en data/private/ y NO ser versionados.

Uso:
    python scripts/build_clientes_master.py --clientes data/private/clientes/customers_real.xlsx --ventas data/private/informes_ventas/ --output data/private/processed/clientes_master_real.json

TODO:
    - Integrar llamadas a parse_clientes, merge_clientes_ventas y geocode_clientes
    - Manejo de errores por etapa
    - Reporte de resultados al finalizar
"""

import json
import argparse
import sys
import os


RUTA_DEFECTO_CLIENTES = "data/private/clientes"
RUTA_DEFECTO_VENTAS = "data/private/informes_ventas"
RUTA_DEFECTO_OUTPUT = "data/private/processed/clientes_master_real.json"


def build_master(
    clientes_path: str,
    ventas_dir: str,
    output_path: str
) -> None:
    """
    Construye el JSON maestro ejecutando las etapas de parseo, fusión y geocodificación.

    Args:
        clientes_path: Ruta al archivo de clientes (Wappsi).
        ventas_dir: Directorio con informes de ventas.
        output_path: Ruta del archivo JSON maestro de salida.
    """
    # TODO: Integrar pipeline completo:
    # 1. parse_clientes(clientes_path) -> lista de clientes
    # 2. merge_clientes_ventas(clientes, ventas_dir) -> clientes con ventas
    # 3. geocode_clientes(clientes) -> clientes con coordenadas
    # 4. guardar JSON en output_path
    clientes = []
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=2)
    print(f"Pipeline completado. {len(clientes)} clientes en {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Construye el JSON maestro de clientes (pipeline completo)"
    )
    parser.add_argument(
        "--clientes", "-c",
        default=os.path.join(RUTA_DEFECTO_CLIENTES, "customers_real.xlsx"),
        help=f"Ruta al archivo de clientes Wappsi (default: {RUTA_DEFECTO_CLIENTES}/customers_real.xlsx)"
    )
    parser.add_argument(
        "--ventas", "-v",
        default=RUTA_DEFECTO_VENTAS,
        help=f"Directorio con informes de ventas (default: {RUTA_DEFECTO_VENTAS})"
    )
    parser.add_argument(
        "--output", "-o",
        default=RUTA_DEFECTO_OUTPUT,
        help=f"Ruta de salida del JSON maestro (default: {RUTA_DEFECTO_OUTPUT})"
    )
    args = parser.parse_args()

    build_master(args.clientes, args.ventas, args.output)


if __name__ == "__main__":
    main()
