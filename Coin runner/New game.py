from UClasses import *


app = Ursina()
window.size=(1600,1000)

window.fps_counter.enabled = False
window.exit_button.enabled = False

boardsize = 20
updatecount = 0

def update():
    global updatecount
    speed = 3 + updatecount*(1/60)
    updatecount += 1


    player.position += player.forward

    if held_keys["d"]:
        player.rotation_y += 5

    if held_keys["a"]:
        player.rotation_y -= 5
    if updatecount % 60 == 0:
        obstacles.append(Ground(position = (player.x+random.randint(-5,5),player.y,player.z + 10)))

    for obstacle in obstacles:
        if player.intersects(obstacle).hit:
            print("Game over")

player = Entity(parent=scene,
            position=(10,0,20),
            model="cube",
            texture="white_cube",
            color=color.red,
            collider='box')

#sky = Sky()
camera.parent = player
camera.position = (0, 11, -15)
camera.rotation = (30, 0, 0)
obstacles = []
destroylist = []
#Startar appen
app.run()
