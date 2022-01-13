import re
from kivy.uix.textinput import TextInput


class TimeInput(TextInput):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if self.text.count(':') >= 2:
            s = re.sub(pat, '', substring)
        else:
            s = ':'.join([re.sub(pat, '', s) for s in substring.split(':', 2)])
        return super(TimeInput, self).insert_text(s, from_undo=from_undo)

    def to_seconds(self):
        if self.text == '':
            return 0
        if self.text == ':':
            return 0

        if self.text.count(':') == 0:
            return int(self.text)

        if self.text.count(':') == 1:
            minutes, seconds = self.text.split(':')
            return (int(minutes) if minutes != '' else 0) * 60 + (int(seconds) if seconds != '' else 0)

        hours, minutes, seconds = self.text.split(':')
        return (int(hours) if hours != '' else 0) * 3600 + (int(minutes) if minutes != '' else 0) * 60 + (int(seconds) if seconds != '' else 0)
