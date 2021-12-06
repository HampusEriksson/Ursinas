from UClasses import *

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.enabled = False


class ClickerButton(Button):
    def __init__(self, game_object, letter, pos_x, pos_y):
        super().__init__()
        self.text = Text(text=letter, scale=2, x=pos_x - 0.025, y=pos_y + 0.025)
        self.game = game_object
        self.letter = letter
        self.x = pos_x
        self.y = pos_y
        self.scale = 0.1
        self.disabled = False
        self.highlight_color = self.color.tint(0.2)
        self.pressed_color = self.color.tint(-0.2)
        self.color = color.azure

    def on_click(self):
        self.disabled = True

        if self.letter in self.game.word:
            self.color = color.green
            self.game.update_word(self.letter)
        else:
            self.color = color.red
            self.game.wrong_count += 1


class Game:
    def __init__(self):
        with open("words.txt") as f:
            words = f.readlines()
        self.word = random.choice(words).upper().strip("\n")
        self.spaces = ["_" for _ in self.word]
        self.wrong_words = []
        self.right_words = []
        self.wrong_count = 0

    def update_word(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.spaces[i] = letter


def update():
    if game.wrong_count >= 10:
        print("Game over")
    t = "".join(c + " " for c in game.spaces)
    lines.text = t


game = Game()
buttons = []
letter_number = 0
lines = Text(text="", scale=8)
lines.origin = ((lines.get_width()) / 2, 0.25)
for y in range(-2, -4, -1):
    for x in range(-6, 7):
        buttons.append(ClickerButton(game, letters[letter_number], x / 8, y / 8))
        letter_number += 1

app.run()
