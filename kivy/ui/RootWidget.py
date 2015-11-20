from kivy.uix.floatlayout import FloatLayout

class RootWidget(FloatLayout):
    """description of class"""

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

    def printHello(self, val):
        print('RootWidget says hallo!!')
