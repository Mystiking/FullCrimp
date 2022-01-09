from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput


class CenteredTextInput(TextInput):

    def update_padding(self, text_input):
        print(self._lines_labels[0].width)
        #text_input.padding_x = (text_input.width - text_width)/2

    # def insert_text(self, substring, from_undo=False):
    #     self.padding_x = self.update_padding(self)
    #     s = substring.upper()
    #     return super(CenteredTextInput, self).insert_text(s, from_undo=from_undo)
