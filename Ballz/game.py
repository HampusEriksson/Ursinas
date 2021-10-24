from constants import *

"""
def addbricks(level):
    for i in range(-5,6,1):
        Brick(window.aspect_ratio*i, level)



addbricks(5)
app.run()"""


app = Ursina(size=(WIDTH, HEIGHT), position= ((FULLWIDTH-WIDTH)/2,(FULLHEIGHT-HEIGHT)/2))
level = 1
camera.orthographic = True
camera.fov = 4
Text.default_resolution *= 2
bricks = []

for x in [-0.25 + x * 0.5 for x in range(-2, 4)]:
    print(x)
    bricks.append(Brick(x, level))

def update():
    for b in bricks:
        b.move_down()
    
    time.sleep(1)
        
    
app.run()


