from ursina import *

FULLWIDTH, FULLHEIGHT = 1920, 1080
WIDTH, HEIGHT = 600,800

class Ball(Entity):

    def __init__(self):
        super().__init__()
        self.model = "sphere"
        self.color = color.red
        self.scale = 0.1
        self.x = 0
        self.y = -4
