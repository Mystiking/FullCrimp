from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.lang import Builder

kv = '''
<RoundedButton>
    canvas.before:
        RoundedRectangle:
            size: self.size
            pos: self.pos
'''

Builder.load_string(kv)


class RoundedButton(ButtonBehavior, Widget):
    pass
