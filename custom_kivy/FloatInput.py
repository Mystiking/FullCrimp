import re
from kivy.uix.textinput import TextInput


class FloatInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)

    def get_value(self):
        if self.text == '':
            return 0.
        if self.text == '.':
            return 0.
        if '.' not in self.text:
            return float(self.text)
        i, d = self.text.split('.')
        value = 0.
        if len(i) == 0:
            value += float('0.' + d)
        elif len(d) == 0:
            value += float(i)
        else:
            value += float(self.text)
        return value
