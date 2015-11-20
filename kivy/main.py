from kivy.app import App
# from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

import json

# Import the default model and any helper functions
from model import Sim

# root = Builder.load_string('''
# FloatLayout:
    # canvas.before:
        # Color:
            # rgba: 0, 1, 0, 1
        # Rectangle:
            # # self here refers to the widget i.e FloatLayout
            # pos: self.pos
            # size: self.size
    # Button:
        # text: 'Hello World!!'
        # size_hint: .5, .5
        # pos_hint: {'center_x':.5, 'center_y': .5}
# ''')

class MainApp(App):

    def build(self):
        print("SimMyIdea starting...")       
        #print(Sim.model["Sim"]["Factory"]["InBank"]["WaterIn"])
        
        Sim.loadModel('model.json')
        Sim.generateUnits()
        print(Sim.units)
        Sim.addUnit('GIGAWATTS')
        print(Sim.units)

        strModelJSON = json.dumps(Sim.model, indent=4, sort_keys=True)

        f = open('model.json', 'w')
        f.write(strModelJSON)

if __name__ == '__main__':
    MainApp().run()
