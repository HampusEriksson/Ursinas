import controller
from constants import *

player = Player()
buttons = []
c = 1
for i in range(-5, 5):
    buttons.append(ClickerButton(player, c, i / 5))
    c *= 10

def getgold():
    global player
    return int(player.gold)

def getgps():
    global player
    return player.gold_per_sec

def addgold():
    global player
    player.gold += 1
    controller.changetext()

