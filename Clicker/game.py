from constants import *
from testfile import ok

app = Ursina()

def button_click():
    global player
    player.gold  += 1
    counter.text = str(player.gold )

player = Player()

counter = Text(text='0', y=.35, scale=2, origin=(0,0), background=True)
button = Button(text='+',y = 0.2, color=color.azure, scale= .125, )
button.on_click = button_click


for i in range(-5,5):
    buttons.append( ClickerButton(player, 10, i/5))

def update():
    global player, seccounter, ok

    stop = time.time()
    if stop-STARTTIME > seccounter:
        seccounter +=1
        ok += 1
        player.gold += player.gold_per_sec
    counter.text = str(player.gold)
    for b in (buttons):
        if player.gold  >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.red





app.run()