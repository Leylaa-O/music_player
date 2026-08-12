import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from core.player import AudioPlayer, PlayState

RUTA_CANCION = r"C:\Users\leyla\Music\metal\Purple Reign.mp3"

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Reproductor")
        self.resize(300, 150)

        self.player = AudioPlayer()

        layout = QVBoxLayout(self)

        self.label = QLabel("Sin reproducir")
        layout.addWidget(self.label)

        self.boton = QPushButton("▶ Play")
        self.boton.clicked.connect(self.al_hacer_click)
        layout.addWidget(self.boton)
    
    def al_hacer_click(self):
        self.player.toggle_play_pause(RUTA_CANCION)
        self._actualizar_interfaz()

    def _actualizar_interfaz(self):
        estado = self.player.state
        if estado == PlayState.PLAYING:
            self.label.setText("Reproduciendo")
            self.boton.setText("⏸ Pausar")
        elif estado == PlayState.PAUSED:
            self.label.setText("En pausa")
            self.boton.setText("▶ Play")
        else:
            self.label.setText("Sin reproducir")
            self.boton.setText("▶ Play")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())