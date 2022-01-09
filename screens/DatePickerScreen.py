from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from src.TrainingType import TrainingType
from src.RunningSession import RunningSession
from datetime import date
from custom_kivy.DatePicker import DatePicker
from kivy.uix.image import Image


class DatePickerScreen(Screen):
    def __init__(self, **kwargs):
        super(DatePickerScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')
        logo_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.35))
        label = Button(text="[color=#404040][font=assets/fonts/vonique/Vonique64.ttf]Fu llC r i m p[/font][/color]",
                       size_hint=(0.25, .5),
                       background_color=[0.93, 0.95, 0.96, 1],
                       background_normal="",
                       background_down="",
                       markup=True,
                       font_size=26,
                       pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label.bind(on_press=self.welcome)
        logo = Image(source='assets/logo/logo_eliptic.png',
                     size_hint=(1.0, 1.0),
                     pos_hint={'center_x': .5, "center_y": .5})

        logo_layout.add_widget(logo)
        logo_layout.add_widget(label)
        layout.add_widget(logo_layout)

        self.date_input_field = DatePicker()
        layout.add_widget(self.date_input_field)

        button_layout = BoxLayout(padding=10, orientation='vertical', size_hint=(1, 0.25))
        button = Button(text="Select date",
                        background_color=[0.24, 0.44, 0.40, 1.0],
                        size_hint=(0.75, 0.25),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_release=self.select_date)
        button_layout.add_widget(button)

        layout.add_widget(button_layout)
        self.add_widget(layout)

    def select_date(self, instance):
        self.parent.chosen_date = self.date_input_field.date
        self.manager.transition.direction = "right"
        self.manager.current = self.parent.previous

    def screen_transition(self, instance):
        self.manager.current = "welcome"

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"