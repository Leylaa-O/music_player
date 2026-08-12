import vlc
import time

ruta_cancion =r"C:\Users\leyla\Music\metal\Purple Reign.mp3"

instancia = vlc.Instance()
reproductor = instancia.media_player_new()
media = instancia.media_new(ruta_cancion)
reproductor.set_media(media)

reproductor.play()

print("Reproduciendo...")
time.sleep(15)
reproductor.stop()