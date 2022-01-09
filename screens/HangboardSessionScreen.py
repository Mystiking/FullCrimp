import os

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from src.TrainingType import TrainingType
from src.HangboardSession import HangboardSession
from datetime import date
from custom_kivy.FloatInput import FloatInput
from custom_kivy.TimeInput import TimeInput
from custom_kivy.IntInput import IntInput


class HangboardSessionScreen(Screen):
    def __init__(self, **kwargs):
        super(HangboardSessionScreen, self).__init__(**kwargs)

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

        # Edge size label and button
        edge_size_layout = BoxLayout(orientation='vertical')
        edge_size_label = Label(text="[color=#404040]Edge size[/color]", pos_hint={'x': 0., 'y': .5}, markup=True)
        self.edge_size_input_field = IntInput()
        edge_size_layout.add_widget(edge_size_label)
        edge_size_layout.add_widget(self.edge_size_input_field)

        # Date label and button
        date_layout = BoxLayout(orientation='vertical')
        self.date_label = Label(text="[color=#404040]Date[/color]",
                                pos_hint={'x': 0., 'y': .5},
                                markup=True)
        date_button = Button(text="Select other date",
                             background_color=[0.24, 0.44, 0.40, 1.0],
                             size_hint=(0.5, 1),
                             pos_hint={'center_x': .5, "center_y": .5})
        date_button.bind(on_release=self.date_picker_transition)
        date_layout.add_widget(self.date_label)
        date_layout.add_widget(date_button)

        # num_sets label and button
        num_sets_layout = BoxLayout(orientation='vertical')
        num_sets_label = Label(text="[color=#404040]Number of Sets[/color]", pos_hint={'x': 0., 'y': .5}, markup=True)
        self.num_sets_input_field = IntInput()
        num_sets_layout.add_widget(num_sets_label)
        num_sets_layout.add_widget(self.num_sets_input_field)

        # Hang time label and button
        hangtime_layout = BoxLayout(orientation='vertical')
        hangtime_label = Label(text="[color=#404040]Hangtime[/color]", pos_hint={'x': 0., 'y': .5}, markup=True)
        self.hangtime_input_field = IntInput()
        hangtime_layout.add_widget(hangtime_label)
        hangtime_layout.add_widget(self.hangtime_input_field)

        body_layout.add_widget(date_layout)

        body_layout.add_widget(edge_size_layout)

        body_layout.add_widget(num_sets_layout)

        body_layout.add_widget(hangtime_layout)

        button_layout = BoxLayout(orientation='vertical')
        button = Button(text="Add Hangboard Session",
                        background_color=[0.24, 0.44, 0.40, 1.0],
                        pos_hint={'center_x': .5, "center_y": .5},
                        size_hint=(0.5, 1))
        button.bind(on_release=self.add_hangboard_session)
        button_layout.add_widget(Label(text=""))
        button_layout.add_widget(button)

        body_layout.add_widget(button_layout)
        layout.add_widget(body_layout)
        self.add_widget(layout)

    def add_hangboard_session(self, instance):
        HangboardSession(edge_size=self.edge_size_input_field.get_value(),
                         num_sets=self.num_sets_input_field.get_value(),
                         set_hang_time=self.hangtime_input_field.get_value(),
                         user_id=self.parent.current_user.id,
                         performed_at=self.parent.chosen_date).create()
        with open('.cache/.hangboard_cache', 'w') as fh:
            fh.write(self.edge_size_input_field.text + '\n')
            fh.write(self.num_sets_input_field.text + '\n')
            fh.write(self.hangtime_input_field.text + '\n')

        self.manager.current = "welcome"

    def date_picker_transition(self, instance):
        self.manager.transition.direction = "left"
        self.parent.previous = "hangboard_session"
        self.manager.current = "date_picker"

    def on_pre_enter(self, *args):
        self.date_label.text = "[color=#404040]Date: {0}[/color]".format(self.parent.chosen_date)
        if os.path.exists('.cache/.hangboard_cache'):
            values = open('.cache/.hangboard_cache').readlines()
            if len(values) == 3:
                self.edge_size_input_field.text = values[0][:-1]
                self.num_sets_input_field.text = values[1][:-1]
                self.hangtime_input_field.text = values[2][:-1]

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"