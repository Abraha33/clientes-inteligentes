"""
validate_no_sensitive_data.py

Propósito: Escanear archivos versionables del repositorio en busca de
posibles datos sensibles antes de hacer commit. Ayuda a prevenir la
publicación accidental de información de clientes.

Uso:
    python scripts/validate_no_sensitive_data.py [--directorio .]

Comportamiento:
    - Escanea archivos .json, .md, .py, .yml, .yaml, .txt, .toml, .cfg
    - Busca patrones de correos electrónicos, posibles teléfonos,
      documentos de identidad y archivos de extensión prohibida
    - Imprime advertencias para cada hallazgo
    - Retorna código de salida 0 si no hay problemas, 1 si se encontraron

TODO:
    - Mejorar detección de NIT/CC con formatos colombianos reales
    - Detectar direcciones con formato de calle y número
    - Detectar coordenadas geográficas exactas
    - Integrar como hook de pre-commit
"""

import os
import re
import sys
import argparse

# Extensiones de archivo a escanear (solo texto versionable)
EXTENSIONES_ESCANEAR = {".json", ".md", ".py", ".yml", ".yaml", ".txt", ".toml", ".cfg"}

# Extensiones prohibidas en el repositorio
EXTENSIONES_PROHIBIDAS = {".xlsx", ".xls", ".csv", ".ods", ".pdf", ".html", ".zip", ".7z", ".rar", ".sqlite", ".db"}

# Patrones de datos sensibles
PATRONES = {
    "correo_electronico": re.compile(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    ),
    "telefono": re.compile(
        r"\+?\d{1,3}[\s.-]?\d{3}[\s.-]?\d{3}[\s.-]?\d{4}"
    ),
    "documento_numerico_largo": re.compile(
        r"\b\d{8,11}\b"
    ),
}

# Datos ficticios permitidos SOLO dentro de data/examples/ (nunca datos reales)
DOMINIOS_EJEMPLO = {"@example.com", "@example.org", "@demo.local"}

# Archivos y directorios a ignorar completamente
IGNORAR_RUTAS = {
    ".git",
    "__pycache__",
    ".gitignore",
    "node_modules",
    ".vscode",
    ".idea",
}

# Archivos permitidos con extensión prohibida (lugares seguros)
ARCHIVOS_PERMITIDOS_PROHIBIDOS = set()


def escanear_archivo(ruta: str) -> list[dict]:
    """
    Escanea un archivo en busca de patrones de datos sensibles.

    El escaneo llama a es_valor_demo_permitido() que aplica reglas
    relajadas solo si el archivo está dentro de data/examples/.
    Fuera de data/examples/ la validación es estrictamente completa.

    Args:
        ruta: Ruta absoluta al archivo.

    Returns:
        Lista de hallazgos con {archivo, linea, patron, coincidencia}.
    """
    hallazgos = []
    try:
        with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
            for num_linea, linea in enumerate(f, 1):
                for nombre_patron, regex in PATRONES.items():
                    for match in regex.finditer(linea):
                        coincidencia = match.group()
                        # Saltar datos ficticios permitidos solo en data/examples/
                        if es_valor_demo_permitido(coincidencia, nombre_patron, ruta):
                            continue
                        # Saltar falsos positivos comunes (años, IDs con ceros, etc.)
                        if nombre_patron == "documento_numerico_largo" and _es_falso_positivo(coincidencia):
                            continue
                        hallazgos.append({
                            "archivo": ruta,
                            "linea": num_linea,
                            "patron": nombre_patron,
                            "coincidencia": coincidencia,
                        })
    except (UnicodeDecodeError, PermissionError, FileNotFoundError):
        pass
    return hallazgos


def es_ruta_examples(ruta: str) -> bool:
    """
    Devuelve True si la ruta contiene data/examples/ o data\\examples\\.

    data/examples/ solo puede contener datos ficticios para documentación
    pública. Nunca debe contener datos reales de clientes.
    """
    ruta_normalizada = ruta.replace(os.sep, "/")
    return "/data/examples/" in ruta_normalizada


def es_valor_demo_permitido(coincidencia: str, nombre_patron: str, ruta: str) -> bool:
    """
    Verifica si una coincidencia es un dato ficticio permitido dentro de data/examples/.
    Si la ruta NO está en data/examples/, devuelve False inmediatamente.

    Reglas solo para data/examples/:
      - correos terminados en @example.com, @example.org, @demo.local
      - teléfonos demo de 10 dígitos que empiecen por 300000000
      - documentos que empiecen por DOC-DEMO-
      - ids que empiecen por DEMO- o WAP-DEMO-
    """
    if not es_ruta_examples(ruta):
        return False

    if nombre_patron == "correo_electronico":
        return any(coincidencia.lower().endswith(d) for d in DOMINIOS_EJEMPLO)
    if nombre_patron == "telefono":
        return len(coincidencia) == 10 and coincidencia.startswith("300000000")
    if nombre_patron == "documento_numerico_largo":
        if len(coincidencia) == 10 and coincidencia.startswith("300000000"):
            return True
        return False
    return False


def _es_falso_positivo(valor: str) -> bool:
    """
    Descarta falsos positivos comunes: IDs, versiones, años, etc.
    """
    # Números de 8-11 dígitos que parecen años o fechas
    if 1900 <= int(valor) <= 2100:
        return True
    # IDs de ejemplo del proyecto
    if valor.startswith("000") or valor == "00000000":
        return True
    return False


def buscar_archivos_prohibidos(directorio: str) -> list[str]:
    """
    Busca archivos con extensiones prohibidas en el árbol versionable.

    Args:
        directorio: Directorio raíz del proyecto.

    Returns:
        Lista de rutas de archivos prohibidos encontrados.
    """
    encontrados = []
    for raiz, _dirs, archivos in os.walk(directorio):
        if any(parte in IGNORAR_RUTAS for parte in raiz.split(os.sep)):
            continue
        for archivo in archivos:
            ext = os.path.splitext(archivo)[1].lower()
            if ext in EXTENSIONES_PROHIBIDAS:
                ruta_completa = os.path.join(raiz, archivo)
                if ruta_completa not in ARCHIVOS_PERMITIDOS_PROHIBIDOS:
                    encontrados.append(ruta_completa)
    return encontrados


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Valida que el repositorio no contenga datos sensibles"
    )
    parser.add_argument(
        "--directorio", "-d",
        default=".",
        help="Directorio raíz del proyecto a escanear (default: .)"
    )
    args = parser.parse_args()

    directorio = os.path.abspath(args.directorio)
    errores = 0

    # 1. Buscar archivos prohibidos por extensión
    print("🔍 Buscando archivos con extensiones prohibidas...")
    prohibidos = buscar_archivos_prohibidos(directorio)
    for archivo in prohibidos:
        print(f"  ⚠️  Archivo prohibido: {archivo}")
        errores += 1

    # 2. Escanear archivos de texto versionables
    print("🔍 Escaneando archivos versionables en busca de datos sensibles...")
    for raiz, _dirs, archivos in os.walk(directorio):
        if any(parte in IGNORAR_RUTAS for parte in raiz.split(os.sep)):
            continue
        for archivo in archivos:
            ext = os.path.splitext(archivo)[1].lower()
            if ext in EXTENSIONES_ESCANEAR:
                ruta = os.path.join(raiz, archivo)
                hallazgos = escanear_archivo(ruta)
                for h in hallazgos:
                    print(
                        f"  ⚠️  [{h['patron']}] {h['archivo']}:{h['linea']} "
                        f"→ '{h['coincidencia']}'"
                    )
                    errores += 1

    # 3. Resumen
    if errores == 0:
        print("✅ No se encontraron datos sensibles. Repositorio seguro para commit.")
        sys.exit(0)
    else:
        print(f"\n❌ Se encontraron {errores} posible(s) dato(s) sensible(s). Revisar antes de commit.")
        sys.exit(1)


if __name__ == "__main__":
    main()
