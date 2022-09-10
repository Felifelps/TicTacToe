from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file("gridlayout.kv")

class Tile(Label):
    def __init__(self, grid, id, **kwargs):
        super(Tile, self).__init__()
        self.grid = grid
        self.n_id = id
        self.clicked = False
    
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y) and not self.clicked:
            self.text = self.grid.who_play
            self.color = ((1, 0, 0, 1) if self.grid.who_play == "X" else (0, 0, 1, 1))
            self.grid.update_tab(self.n_id)
            self.grid.update_who_play()
            self.clicked = True
            return True
        return super().on_touch_down(touch)
        

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__()
        self.restart()
    
    def update_who_play(self):
        self.who_play = ("X" if self.who_play == "O" else "O")
    
    def update_tab(self, pos):
        self.tab[pos - 1] = self.who_play
    
    def restart(self):
        self.clear_widgets()
        self.who_play = "X"
        self.tab = []
        for i in range(1, 10):
            self.add_widget(Tile(self, i))
            self.tab.append(" ")
