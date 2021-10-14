from ursina import *
from ursina.prefabs.first_person_controller import *


def update():
    if player.y < 0:
        player.position = (16,0,-18)

app = Ursina()



maze = Entity(model = "maze", texture = "brick", scale = 20, collider = "mesh")

player = FirstPersonController(position = (16,0,-18))

app.run()
