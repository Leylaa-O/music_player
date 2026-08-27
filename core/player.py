import vlc
from enum import Enum, auto

class PlayState(Enum):
    STOPPED = auto()
    PLAYING = auto()
    PAUSED = auto()

class AudioPlayer:
    def __init__(self):
        self._instance = vlc.Instance("--no-video")
        self._media_player = self._instance.media_player_new()
        self.state = PlayState.STOPPED
    
    def load(self, filepath: str):
        media = self._instance.media_new(filepath)
        self._media_player.set_media(media)

    def play(self, filepath: str):
        self.load(filepath)
        self._media_player.play()
        self.state = PlayState.PLAYING

    def pause(self):
        if self.state == PlayState.PLAYING:
            self._media_player.pause()
            self.state = PlayState.PAUSED

    def resume(self):
        if self.state == PlayState.PAUSED:
            self._media_player.play()
            self.state = PlayState.PLAYING

    def toggle_play_pause(self):
        if self.state == PlayState.PLAYING:
            self.pause()
        elif self.state == PlayState.PAUSED:
            self.resume()
        #elif self.state == PlayState.STOPPED:
        #    self.play(filepath)