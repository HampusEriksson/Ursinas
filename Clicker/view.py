from constants import *

app = Ursina()
player = Player()

def setup(x):
    global gpsCounter, counter, timecounter, button
    gpsCounter = Text(text='0', y=-.25, scale=2, origin=(0, 0), background=True)
    counter = Text(text='0', y=.35, scale=2, origin=(0, 0), background=True)
    timecounter = Text(text='0', y=.45, scale=2, origin=(0, 0))
    button = Button(text='+', y=0.2, color=color.azure, scale=.125, on_click = x)
    app.run()

def addbuttons():
    pass










