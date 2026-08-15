from pathlib import Path
from core.metadata import leer_metadata
from database.db_manager import DBManager

FORMATOS_SOPORTADOS = {".mp3", ".wav", ".flac", ".aac", ".m4a", ".ogg"}

def escanear_carpeta(carpeta: str, db: DBManager):
    """    Escanea y  guarda en la base de datos. """
    ruta = Path(carpeta)
    archivos_encontrados = [
        p for p in ruta.rglob("*")
        if p.suffix.lower() in FORMATOS_SOPORTADOS and p.is_file()
    ]

    print(f"Se encontraron {len(archivos_encontrados)} archivos de audios")

    for i, archivo in enumerate(archivos_encontrados, start=1):
        info = leer_metadata(str(archivo))
        db.agregar_cancion(str(archivo), info)
        print(f"[{i}/{len(archivos_encontrados)}] Guardado: {info['titulo']}")

    print("Escaneo completo.")