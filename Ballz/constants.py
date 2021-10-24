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

class Brick(Entity):

    def __init__(self, x, hits = 5):
        super().__init__()
        self.model = "cube"
        self.color = color.green
        self.scale = 0.45
        self.x = x
        self.y = 1.5
        self.hits = hits
        self.text = str(hits)

    def move_down(self):
        self.y -= 0.45

