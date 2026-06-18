"""
geocode_clientes.py

Propósito: Geocodificar las direcciones de los clientes para obtener
coordenadas (latitud, longitud). Prepara los datos para su uso en
mapas comerciales y generación de rutas.

Los datos reales deben residir en data/private/ y NO ser versionados.
Las coordenadas son datos sensibles — no publicarlas sin anonimizar.

Uso:
    python scripts/geocode_clientes.py --input data/private/processed/clientes_master_real.json --output data/private/processed/clientes_master_real.json

TODO:
    - Implementar geocodificación por lotes (batch)
    - Soporte para Google Maps Geocoding API
    - Soporte para OpenStreetMap / Nominatim
    - Manejo de tasa de límites (rate limiting)
    - Cache de geocodificaciones para evitar llamadas repetidas
    - Manejo de direcciones incompletas o incorrectas
    - Reporte de direcciones no geocodificables
"""

import json
import argparse
import sys
import os


RUTA_DEFECTO_INPUT = "data/private/processed/clientes_master_real.json"
RUTA_DEFECTO_OUTPUT = "data/private/processed/clientes_master_real.json"


def cargar_clientes(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def geocodificar(clientes: list[dict]) -> list[dict]:
    """
    Geocodifica las direcciones de cada cliente.

    Args:
        clientes: Lista de clientes con direcciones.

    Returns:
        Lista de clientes con coordenadas (latitud, longitud) actualizadas.
    """
    # TODO: Implementar geocodificación real
    # - Extraer dirección de cada cliente
    # - Consultar API de geocodificación
    # - Actualizar campos latitud y longitud
    # - Marcar clientes con error de geocodificación
    for cliente in clientes:
        ubicacion = cliente.get("ubicacion", {})
        if ubicacion.get("direccion"):
            ubicacion["latitud"] = None
            ubicacion["longitud"] = None
    return clientes


def guardar_json(clientes: list[dict], output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Geocodifica direcciones de clientes"
    )
    parser.add_argument(
        "--input", "-i",
        default=RUTA_DEFECTO_INPUT,
        help=f"Ruta al archivo JSON de clientes (default: {RUTA_DEFECTO_INPUT})"
    )
    parser.add_argument(
        "--output", "-o",
        default=RUTA_DEFECTO_OUTPUT,
        help=f"Ruta del archivo JSON de salida (default: {RUTA_DEFECTO_OUTPUT})"
    )
    args = parser.parse_args()

    clientes = cargar_clientes(args.input)
    clientes = geocodificar(clientes)
    guardar_json(clientes, args.output)
    print(f"Geocodificados {len(clientes)} clientes. Guardado en {args.output}")


if __name__ == "__main__":
    main()
