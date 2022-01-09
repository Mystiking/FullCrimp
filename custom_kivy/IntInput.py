import re
from kivy.uix.textinput import TextInput


class IntInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        return super(IntInput, self).insert_text(s, from_undo=from_undo)

    def get_value(self):
        if self.text == '':
            return 0.
        return int(self.text)
