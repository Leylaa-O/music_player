from core.metadata import leer_metadata, formaterar_duracion

RUTA_CANCION = r"C:\Users\leyla\Music\metal\Purple Reign.mp3"

info = leer_metadata(RUTA_CANCION)

print("Título :", info["titulo"])
print("Artista:", info["artista"])
print("Álbum  :", info["album"])
print("Género :", info["genero"])
print("Año    :", info["anio"])
print("Duración:", formaterar_duracion(info["duracion"]))