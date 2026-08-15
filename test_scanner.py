from database.db_manager import DBManager
from core.scanner import escanear_carpeta

CARPETA_MUSIC = r"C:\Users\leyla\Music\playlist_musica"

db=DBManager()
escanear_carpeta(CARPETA_MUSIC, db)

print("\nCanciones en la base de datos:")
for cancion in db.obtener_todas():
    print(f"- {cancion['titulo']} - {cancion['artista']}")