from ursina import *
buttons = []
STARTTIME = time.time()
seccounter = 1

class Player:
    def __init__(self):
        self.gold = 0
        self.gold_per_sec = 0

class ClickerButton(Button):

    def __init__(self,player, cost, x = 0.2, y = 0):
        super().__init__()
        self.player = player
        self.cost = cost
        self.x = x
        self.y = y
        self.scale = 0.125
        self.color = color.red
        self.disabled = True
        self.highlight_color = self.color.tint(.2)
        self.pressed_color = self.color.tint(-.2)
        self.tooltip = Tooltip(
            f'<gold>Gold Generator\n<default>Earn {self.cost//10} gold every second.\nCosts {self.cost} gold.')

    def on_click(self):

        if self.player.gold >= self.cost:
            self.player.gold -= self.cost
            self.player.gold_per_sec += self.cost // 10

