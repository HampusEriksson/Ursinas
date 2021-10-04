from ursina import *

app = Ursina()

def update():
    ent1.rotation += Vec3(1,1,1) * time.dt
    ent1.position += ent1.forward * time.dt

window.exit_button.enabled = True
window.fps_counter.enabled = False
window.cog_button.enabled = False
window.fullscreen = False

ent1 = Entity(
    model="cube",
    color=color.rgb(255, 0, 0),
    texture="brick",
    position = Vec3(3,3,3),
    rotation = Vec3(0,0,0),
    scale = (1,1,1)
)

ent2 = Entity(parent=ent1, model = "sphere", position = (1,1,1))

EditorCamera()


app.run()
