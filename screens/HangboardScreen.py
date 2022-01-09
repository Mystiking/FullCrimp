from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from src.TrainingType import TrainingType
from src.YogaSession import YogaSession
from custom_kivy.FloatInput import FloatInput
from custom_kivy.TimeInput import TimeInput


class HangboardScreen(Screen):
    def __init__(self, **kwargs):
        super(HangboardScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')

        logo_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.25))
        label = Button(text="[color=#404040][font=assets/fonts/vonique/Vonique64.ttf]Fu llC r i m p[/font][/color]", size_hint=(0.25, .5),
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

        body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.8))

        button_layout = BoxLayout(orientation='vertical')
        button = Button(text="Add Hangboard Session",
                        background_color=[0.24, 0.44, 0.40, 1.0],
                        pos_hint={'center_x': .5, "center_y": .5},
                        size_hint=(0.5, 1))
        button.bind(on_release=self.add_hangboard_session)
        button_layout.add_widget(button)

        new_button_layout = BoxLayout(orientation='vertical')
        new_button = Button(text="Start New",
                            background_color=[0.8, 0.8, 0.8, 1.0],
                            pos_hint={'center_x': .5, "center_y": .5},
                            size_hint=(0.5, 1))
        new_button.bind(on_release=self.start_new_hangboard_session)
        new_button_layout.add_widget(new_button)

        body_layout.add_widget(button_layout)
        body_layout.add_widget(new_button_layout)
        layout.add_widget(body_layout)
        self.add_widget(layout)

    def add_hangboard_session(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "hangboard_session"

    def start_new_hangboard_session(self, instance):
        pass

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"