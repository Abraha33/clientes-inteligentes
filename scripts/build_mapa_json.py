"""
build_mapa_json.py

Propósito: Construir el archivo clientes_mapa.json a partir de la
base maestra, preparando los datos para su visualización en un mapa
comercial interactivo.

Los datos reales deben residir en data/private/ y NO ser versionados.
Las coordenadas son datos sensibles — no publicarlas sin anonimizar.

Uso:
    python scripts/build_mapa_json.py --input data/private/processed/clientes_master_real.json --output data/private/processed/clientes_mapa_real.json

TODO:
    - Seleccionar campos relevantes para el mapa (ubicación, tipo, ventas)
    - Agrupar por coordenadas para evitar superposición de marcadores
    - Calcular datos agregados por zona (barrio, ciudad)
    - Generar colores o íconos según tipo de comercio
    - Preparar formato compatible con Leaflet, Mapbox o Google Maps
    - Excluir clientes sin coordenadas
    - Opcional: filtro por segmento, nivel o estado comercial
"""

import json
import argparse
import sys
import os


RUTA_DEFECTO_INPUT = "data/private/processed/clientes_master_real.json"
RUTA_DEFECTO_OUTPUT = "data/private/processed/clientes_mapa_real.json"


def cargar_clientes(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_mapa(clientes: list[dict]) -> list[dict]:
    """
    Transforma los datos maestros en registros optimizados para mapa.

    Args:
        clientes: Lista de clientes del maestro.

    Returns:
        Lista de registros simplificados para mapa.
    """
    # TODO: Implementar transformación a formato mapa
    # - Extraer coordenadas, nombre, tipo, nivel, estado
    # - Agrupar por ubicación si hay duplicados
    # - Calcular métricas por zona
    mapa = []
    for cliente in clientes:
        ubicacion = cliente.get("ubicacion", {})
        if ubicacion.get("latitud") is not None and ubicacion.get("longitud") is not None:
            registro = {
                "id_cliente": cliente.get("identificacion", {}).get("id_cliente"),
                "nombre": cliente.get("identificacion", {}).get("nombre"),
                "latitud": ubicacion.get("latitud"),
                "longitud": ubicacion.get("longitud"),
                "direccion": ubicacion.get("direccion"),
                "barrio": ubicacion.get("barrio"),
                "ciudad": ubicacion.get("ciudad"),
                "tipo_comercio": ubicacion.get("tipo_comercio"),
                "subtipo_comercio": ubicacion.get("subtipo_comercio"),
                "nivel": cliente.get("ventas", {}).get("estado_comercial"),
                "estado": cliente.get("ventas", {}).get("estado_comercial"),
            }
            mapa.append(registro)
    return mapa


def guardar_json(data: list[dict], output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Construye JSON para mapa comercial a partir del maestro"
    )
    parser.add_argument(
        "--input", "-i",
        default=RUTA_DEFECTO_INPUT,
        help=f"Ruta al archivo clientes_master.json (default: {RUTA_DEFECTO_INPUT})"
    )
    parser.add_argument(
        "--output", "-o",
        default=RUTA_DEFECTO_OUTPUT,
        help=f"Ruta del archivo JSON de mapa de salida (default: {RUTA_DEFECTO_OUTPUT})"
    )
    args = parser.parse_args()

    clientes = cargar_clientes(args.input)
    mapa = build_mapa(clientes)
    guardar_json(mapa, args.output)
    print(f"Preparados {len(mapa)} registros para mapa. Guardado en {args.output}")


if __name__ == "__main__":
    main()
