from tkinter import W, Widget
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock

class GameLogic:
    def __init__(self):
        self.lines = [
            [1, 2, 3], 
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

    def check_victory(self, tab):
        for line in self.lines:
            line_draw = ""
            for point in line:
                line_draw += tab[point - 1]
            if line_draw in ["XXX", "OOO"]:
                return [line_draw[0], line]
        if " " not in tab:
            return " "
        return False

class MainWidget(RelativeLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__()
        self.grid = self.ids["grid"]
        self.counter = self.ids["counter"]
        self.victory = self.ids["victory"]
        self.ids["restart"].bind(on_press=self.restart)
        self.logic = GameLogic()

    def update_counter(self, dt):
        victory = self.logic.check_victory(self.grid.tab)
        if isinstance(victory, list):
            letter = victory[0]
            self.victory.color = ((1, 0, 0, 1) if letter == "X" else (0, 0, 1, 1))
            self.victory.text = letter + " ganhou!"
        elif victory == " ":
            self.victory.color = (0, 1, 0, 1)
            self.victory.text = "Deu velha!"
        self.counter.text = f"Vez do: {self.grid.who_play}"

    def restart(self, event):
        self.victory.text = ""
        self.counter.text = "Vez do: X"
        self.grid.restart()

class TicTacToe(App):
    def build(self):
        main = MainWidget()
        Clock.schedule_interval(main.update_counter, 0.1)
        return main

if __name__ == '__main__':
    TicTacToe().run()