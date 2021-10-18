from ursina import *
from constants import *

app = Ursina()
player = Player()
def setup(x):
    global counter, buttons
    buttons = []
    for i in range(-5, 5):
        buttons.append(ClickerButton(player, 10, i / 5))
    counter = Text(text='0', y=.35, scale=2, origin=(0, 0), background=True)
    button = Button(text='+', y=0.2, color=color.azure, scale=.125)
    button.on_click = x
    app.run()

def addbutton():
    button = Button(text='+', y=0.4, color=color.red, scale=.125)










