from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from UClasses import *

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.enabled = False

boardsize = 20

class Target(Entity):

    def __init__(self):
        super(Target, self).__init__(
            parent=scene,
            position=(10,2,10),
            model="cube",
            origin_y=0,
            texture="white_cube",
            color=color.red,
            scale=(1,2),
        )
        self.speed = 1
        self.dt = 1

class Bullet(Entity):

    def __init__(self, position):
        super(Bullet, self).__init__(
            parent=scene,
            position=position,
            model="sphere",
            origin_y=0,
            texture="white_cube",
            color=color.black,
            scale=0.2,
        )

def update():

    if held_keys["left mouse"]:
        hand.active()
        bullet.position = player.position + (0.4, -0.6,0) + (0,2,0)
        print(mouse.position, mouse.delta,mouse.velocity, mouse.delta_dragu)

    else:
        hand.passive()

    target.x += target.dt*target.speed*time.dt

    if target.x > boardsize or target.x < 0:
        target.dt *= -1


def createworld():
    for z in range(boardsize):
        for x in range(boardsize):
            voxel = Ground(position = (x,0,z))


createworld()
target = Target()
player = FirstPersonController(position = (10,10,10))
sky = Sky()
hand = Hand()
bullet = Bullet((0,2,0))
#Startar appen
app.run()
