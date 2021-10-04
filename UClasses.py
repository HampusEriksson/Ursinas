#testing
from ursina import *
from random import *

class Sky(Entity):
    def __init__(self):
        super(Sky, self).__init__(
            parent=scene,
            model="sphere",
            color=color.blue,
            scale=150,
            double_sided=True
        )

class Hand(Entity):

    def __init__(self):
        super(Hand, self).__init__(
            parent=camera.ui,
            model="assets/arm",
            texture="assets/arm_texture.png",
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)

class Ground(Entity):

    def __init__(self, position=(0, 0, 0)):
        super(Ground, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            texture="white_cube",
            color=color.green,
        )

class Wall(Entity):
    def __init__(self, position):
        super(Wall, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            color=color.black,
            collider = "cube"
        )



