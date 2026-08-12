from database.db_manager import DBManager
from core.metadata import leer_metadata

RUTA_CANCION = r"C:\Users\leyla\Music\metal\Purple Reign.mp3"

db = DBManager()

info = leer_metadata(RUTA_CANCION)
db.agregar_cancion(RUTA_CANCION, info)

print("Canciones guardadas en la base de datos:")
for cancion in db.obtener_todas():
    print(f"- {cancion['titulo']} ({cancion['artista']})")