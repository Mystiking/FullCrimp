from kivy.uix.boxlayout import BoxLayout
from datetime import date, timedelta
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.graphics import Color, Rectangle

class DatePicker(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(DatePicker, self).__init__(**kwargs)
        self.date = date.today()
        self.orientation = "vertical"
        self.month_names = ('January',
                            'February',
                            'March',
                            'April',
                            'May',
                            'June',
                            'July',
                            'August',
                            'September',
                            'October',
                            'November',
                            'December')

        self.header = BoxLayout(orientation = 'horizontal',
                                size_hint = (1, 0.2))
        self.body = GridLayout(cols=7)
        self.add_widget(self.header)
        self.add_widget(self.body)

        self.populate_body()
        self.populate_header()

    def populate_header(self, *args, **kwargs):
        self.header.clear_widgets()
        previous_month = Button(text = "<", background_color=[0.24, 0.44, 0.40, 1.0])
        previous_month.bind(on_release=partial(self.move_previous_month))
        next_month = Button(text = ">", background_color=[0.24, 0.44, 0.40, 1.0])
        next_month.bind(on_release=lambda *args: self.move_next_month())
        month_year_text = self.month_names[self.date.month -1] + ' ' + str(self.date.year)
        current_month = Label(text="[color=#404040]" + month_year_text + "[/color]", size_hint = (2, 1), markup=True)

        self.header.add_widget(previous_month)
        self.header.add_widget(current_month)
        self.header.add_widget(next_month)

    def populate_body(self, *args, **kwargs):
        self.body.clear_widgets()
        date_cursor = date(self.date.year, self.date.month, 1)
        for filler in range(date_cursor.isoweekday()-1):
            self.body.add_widget(Label(text=""))
        while date_cursor.month == self.date.month:
            date_label = Button(text = str(date_cursor.day), background_color=[0.24, 0.44, 0.40, 1.0], background_normal="")
            date_label.bind(on_press=partial(self.set_date,
                                                  day=date_cursor.day))
            if self.date.day == date_cursor.day:
                date_label.background_normal, date_label.background_down = date_label.background_down, date_label.background_normal
            self.body.add_widget(date_label)
            date_cursor += timedelta(days = 1)

    def set_date(self, *args, **kwargs):
        self.date = date(self.date.year, self.date.month, kwargs['day'])
        self.populate_body()
        self.populate_header()

    def move_next_month(self, *args, **kwargs):
        if self.date.month == 12:
            self.date = date(self.date.year + 1, 1, self.date.day)
        else:
            self.date = date(self.date.year, self.date.month + 1, self.date.day)
        self.populate_header()
        self.populate_body()

    def move_previous_month(self, *args, **kwargs):
        if self.date.month == 1:
            self.date = date(self.date.year - 1, 12, self.date.day)
        else:
            self.date = date(self.date.year, self.date.month -1, self.date.day)
        self.populate_header()
        self.populate_body()
