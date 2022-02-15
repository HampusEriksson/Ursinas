#Classes
from ursina import *

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
            collider='box'
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

class WordleButton(Button):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale = 0.1,
            disabled = False,
            highlight_color=self.color.tint(0.2),
            pressed_color=self.color.tint(-0.2),
            color=color.gray

        )
        self.text =Text(parent=self, text="Test", scale=10)


    def on_click(self):
        for key in held_keys:
            if len(key) == 1:
                print(self.text)

