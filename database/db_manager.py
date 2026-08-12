import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "musica.db"
DB_PATH.parent.mkdir(exist_ok=True)  # Crear la carpeta "data "si no existe

class DBManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = str(db_path)
        self._crear_tabla()
    
    def _conectar(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _crear_tabla(self):
        conn = self._conectar()
        conn.execute(""" 
            CREATE TABLE IF NOT EXISTS canciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filepath TEXT UNIQUE NOT NULL,
                titulo TEXT NOT NULL,
                artista TEXT NOT NULL,
                album TEXT NOT NULL,
                genero TEXT NOT NULL,
                anio INTEGER,
                duracion REAL DEFAULT 0
                )
            """)
        conn.commit()
        conn.close()
    
    def agregar_cancion(self, filepath: str, datos: dict):
        conn = self._conectar()
        conn.execute("""
            INSERT INTO canciones (filepath, titulo, artista, album, genero, anio, duracion)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(filepath) DO UPDATE SET
                titulo=excluded.titulo,
                artista=excluded.artista,
                album=excluded.album,
                genero=excluded.genero,
                anio=excluded.anio,
                duracion=excluded.duracion
        """, (filepath, datos["titulo"], datos["artista"], datos["album"],
              datos["genero"], datos["anio"], datos["duracion"]))
        conn.commit()
        conn.close()

    def obtener_todas(self) -> list[dict]:
        conn = self._conectar()
        filas = conn.execute("SELECT * FROM canciones ORDER BY artista, album").fetchall()
        conn.close()
        return [dict(fila) for fila in filas]