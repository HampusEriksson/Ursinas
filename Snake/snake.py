from UClasses import *
from random import *

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.enabled = False

boardsize = 20

class Apple(Entity):

    def __init__(self):
        super(Apple, self).__init__(
            parent=scene,
            position=(randint(0,boardsize),1,randint(0,boardsize)),
            model="sphere",
            origin_y=0,
            texture="red_cube",
            color=color.red,
            collider="sphere"
        )

class Head(Entity):

    def __init__(self):
        super(Head, self).__init__(
            parent=scene,
            position=(0,1,0),
            model="sphere",
            color=color.pink,
            collider = "sphere"
        )
        self.direction = (0,0,0.1)
        self.speed = 0.1

class Part(Entity):

    def __init__(self, position):
        super(Part, self).__init__(
            parent=scene,
            position=position,
            model="cube",
            color=color.white
        )

def update():

    if held_keys["d"]:
        head.direction =  tuple([head.speed*x for x in (1,0,0)])

    if held_keys["w"]:
        head.direction =  tuple([head.speed*x for x in (0,0,1)])

    if held_keys["a"]:
        head.direction =  tuple([head.speed*x for x in (-1,0,0)])

    if held_keys["s"]:
        head.direction =  tuple([head.speed*x for x in (0,0,-1)])

    if parts != []:

        for i in range(len(parts)-1,0,-1):
            newpos = parts[i-1].position
            parts[i].position = newpos
        parts[0].position = head.position

    head.position += head.direction

    hit = raycast(head.position, head.down, distance=2, ignore=[head, ])
    print("Hejhej")
    if type(hit.entity) == Apple:
        apple.position = (randint(1,boardsize-1),1,randint(1,boardsize-1))
        head.speed +=0.01
        parts.append(Part(head.position - tuple([5*x for x in head.direction])))

    if type(hit.entity) == Wall:
        sys.exit()

def createworld():
    for z in range(boardsize):
        for x in range(boardsize):
            voxel = Ground(position = (x,0,z))

    for z in range(-1,boardsize):
            for y in range(2):
                wall = Wall((-1,y,z))
                wall = Wall(position= (boardsize, y, z))

    for x in range(-1,boardsize):
            for y in range(2):
                wall = Wall(position=(x,y,-1))
                wall = Wall(position=(x,y,boardsize))

parts = []
createworld()
head = Head()
apple = Apple()
sky = Sky()

camera.position = (boardsize/2,boardsize*3,boardsize/2)
camera.rotation = Vec3(90,0, 0)

app.run()
