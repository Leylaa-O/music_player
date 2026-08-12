from pathlib import Path
from mutagen import File as MutagenFile

def leer_metadata(filepath:str) -> dict:
    datos = {
        "titulo": Path(filepath).stem,
        "artista": "Desconocido",
        "album": "Desconocido",
        "genero": "Desconocido",
        "anio": None,
        "duracion": 0.0,
    }

    try:
        audio = MutagenFile(filepath, easy=True)
        if audio is not None:
            datos["titulo"] = _primero(audio.get("title")) or datos["titulo"]
            datos["artista"] = _primero(audio.get("artist")) or datos["artista"]
            datos["album"] = _primero(audio.get("album")) or datos["album"]
            datos["genero"] = _primero(audio.get("genre")) or datos["genero"]

            anio_texto = _primero(audio.get("date")) or _primero(audio.get("year"))
            datos["anio"] = _a_entero(anio_texto)

            if audio.info is not None:
                datos["duracion"] = round(audio.info.length, 2)
    
    except Exception as e:
        print(f"No se pudo leer metadata de {filepath}: {e}")

    return datos

def _primero(valor): 
    """  Devuelve el primer elemento de una lista o None si la lista está vacía o es None."""
    if isinstance(valor, list) and valor:
        return str(valor[0])
    return None

def _a_entero(valor):
    try:
        return int(str(valor)[:4])
    except (ValueError, TypeError):
        return None

def formaterar_duracion(segundos: float) -> str:
    """Convierte la duración en segundos a un formato de minutos y segundos."""
    segundos = int(segundos)
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return f"{minutos}:{segundos_restantes:02d}"