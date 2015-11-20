class Node(object):
    """description of class"""


    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MyRootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Hello World",
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5}))