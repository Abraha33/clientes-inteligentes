"""
build_clientes_mapa.py

Propósito: Construir el archivo clientes_mapa.json a partir del
maestro de clientes, preparando los datos para visualización en mapa
comercial. Esta es una versión orientada al pipeline de data/private/.

Los datos reales deben residir en data/private/ y NO ser versionados.

Uso:
    python scripts/build_clientes_mapa.py --input data/private/processed/clientes_master_real.json --output data/private/processed/clientes_mapa_real.json

TODO:
    - Extraer y simplificar campos para mapa
    - Validar que todos los registros tengan coordenadas
    - Agrupar por zona para reducir marcadores
    - Opcional: generar GeoJSON en lugar de JSON plano
"""

import json
import argparse
import sys
import os


RUTA_DEFECTO_INPUT = "data/private/processed/clientes_master_real.json"
RUTA_DEFECTO_OUTPUT = "data/private/processed/clientes_mapa_real.json"


def build_mapa(input_path: str, output_path: str) -> None:
    """
    Lee el maestro de clientes y genera el JSON para mapa.

    Args:
        input_path: Ruta al archivo clientes_master_real.json.
        output_path: Ruta de salida del JSON de mapa.
    """
    # TODO: Implementar transformación de maestro a formato mapa
    with open(input_path, "r", encoding="utf-8") as f:
        clientes = json.load(f)

    mapa = []
    for cliente in clientes:
        identificacion = cliente.get("identificacion", {})
        ubicacion = cliente.get("ubicacion", {})
        ventas = cliente.get("ventas", {})
        registro = {
            "id_cliente": identificacion.get("id_cliente"),
            "nombre": identificacion.get("nombre"),
            "latitud": ubicacion.get("latitud"),
            "longitud": ubicacion.get("longitud"),
            "direccion": ubicacion.get("direccion"),
            "barrio": ubicacion.get("barrio"),
            "ciudad": ubicacion.get("ciudad"),
            "tipo_comercio": ubicacion.get("tipo_comercio"),
            "subtipo_comercio": ubicacion.get("subtipo_comercio"),
            "nivel": ventas.get("estado_comercial"),
            "estado": ventas.get("estado_comercial"),
            "segmento": cliente.get("marketing", {}).get("segmento"),
        }
        mapa.append(registro)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(mapa, f, ensure_ascii=False, indent=2)

    print(f"Preparados {len(mapa)} registros para mapa. Guardado en {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Construye JSON para mapa comercial desde el maestro"
    )
    parser.add_argument(
        "--input", "-i",
        default=RUTA_DEFECTO_INPUT,
        help=f"Ruta al archivo clientes_master_real.json (default: {RUTA_DEFECTO_INPUT})"
    )
    parser.add_argument(
        "--output", "-o",
        default=RUTA_DEFECTO_OUTPUT,
        help=f"Ruta del JSON de mapa de salida (default: {RUTA_DEFECTO_OUTPUT})"
    )
    args = parser.parse_args()

    build_mapa(args.input, args.output)


if __name__ == "__main__":
    main()
