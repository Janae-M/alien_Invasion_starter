from pathlib import path
class Settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.scren_w = 1200
        self.scren_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'