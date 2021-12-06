from UClasses import *

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(letters))

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.enabled = False

class ClickerButton(Button):

    def __init__(self, game, letter, x, y):
        super().__init__()
        self.text = Text(text=letter, scale=2, x=x-0.025, y=y+0.025)
        self.game = game
        self.letter = letter
        self.x = x
        self.y = y
        self.scale = 0.1
        self.disabled = False
        self.highlight_color = self.color.tint(.2)
        self.pressed_color = self.color.tint(-.2)
        self.color = color.azure

    def on_click(self):
        if self.letter in self.game.word:
            self.color = color.green
            self.disabled = True
            self.game.updateword(self.letter)
        else:
            self.color = color.red
            self.disabled = True
            self.game.wrongcount += 1


class Game():
    def __init__(self):
        with open('words.txt') as f:
            lines = f.readlines()
        self.word = random.choice(lines)
        self.spaces = ["_" for _ in self.word]
        self.wrong_words = []
        self.right_words = []
        self.wrongcount = 0

    def updateword(self, letter):
        for i in range(len(self.word)):
            print(i,len(self.word), len(self.spaces))
            if self.word[i] == letter:
                self.spaces[i] = letter


def update():
    if game.wrongcount >= 10:
        print("Game over")
    t = ""
    for c in game.spaces:
        t += c + " "
    lines.text = t


game = Game()
buttons = []
l = 0
lines = Text(text="", scale = 8)
lines.origin = ((lines.get_width()+lines.get_x())/2, 0.25)
for y in range(-2,-4,-1):
    for x in range(-6,7):
        buttons.append(ClickerButton(game, letters[l], x/8, y/8))
        l += 1

app.run()
