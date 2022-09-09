from tkinter import W, Widget
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.clock import Clock

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '700')

class GameLogic:
    def __init___(self, tab):
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

class MainWidget(RelativeLayout):
    def _init__(self, **kwargs):
        super(MainWidget, self).__init__()

    def update_counter(self, dt):
        self.ids["counter"].text = f"Vez do: {self.ids['grid'].who_play}"

class TicTacToe(App):
    def build(self):
        main = MainWidget()
        Clock.schedule_interval(main.update_counter, 0.1)
        return main

if __name__ == '__main__':
    TicTacToe().run()