import sys
from PySide6.QtWidgets import (
   QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
   QTableWidget, QTableWidgetItem, QHeaderView 
)

from core.player import AudioPlayer, PlayState
from database.db_manager import DBManager

#RUTA_CANCION = r"C:\Users\leyla\Music\metal\Purple Reign.mp3"

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Reproductor")
        self.resize(600, 400)

        self.player = AudioPlayer()
        self.db = DBManager()
        self.canciones = []
        self.cancion_actual = None

        layout = QVBoxLayout(self)

        self.label = QLabel("Sin reproducir")
        layout.addWidget(self.label)

        self.boton = QPushButton("▶ Play")
        self.boton.clicked.connect(self.al_hacer_click)
        layout.addWidget(self.boton)

        # --- Tabla de la biblioteca ---
        self.tabla = QTableWidget(0, 3)
        self.tabla.setHorizontalHeaderLabels(["Título", "Artista", "Álbum"])
        self.tabla.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cargar_biblioteca()
        self.tabla.cellDoubleClicked.connect(self.al_hacer_doble_clic)
        layout.addWidget(self.tabla)


    def cargar_biblioteca(self):
        self.canciones = self.db.obtener_todas()
        self.tabla.setRowCount(len(self.canciones))

        for fila, cancion in enumerate(self.canciones):
            self.tabla.setItem(fila, 0, QTableWidgetItem(cancion['titulo']))
            self.tabla.setItem(fila, 1, QTableWidgetItem(cancion['artista']))
            self.tabla.setItem(fila, 2, QTableWidgetItem(cancion['album']))
    
    def al_hacer_doble_clic(self, fila, columna):
        cancion = self.canciones[fila]
        self.reproducir_cancion(cancion)

    def reproducir_cancion(self, cancion: dict):
        self.player.play(cancion["filepath"])
        self.cancion_actual = cancion
        self._actualizar_interfaz()

    def al_hacer_click(self):
        if self.cancion_actual is None:
            self.label.setText("Elige una canción de la tabla primero (doble clic)")
            return

        self.player.toggle_play_pause()
        self._actualizar_interfaz()

    def _actualizar_interfaz(self):
        estado = self.player.state
        nombre = f"{self.cancion_actual['titulo']} - {self.cancion_actual['artista']}" if self.cancion_actual else "Sin canción"

        if estado == PlayState.PLAYING:
            self.label.setText(f"▶ {nombre}")
            self.boton.setText("⏸ Pausa")
        elif estado == PlayState.PAUSED:
            self.label.setText(f"⏸ {nombre}")
            self.boton.setText("▶ Play")
        else:
            self.label.setText("Sin reproducir")
            self.boton.setText("▶ Play")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())