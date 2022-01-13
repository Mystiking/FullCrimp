from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from custom_kivy.FloatInput import FloatInput
from src.Weight import Weight


class WeightScreen(Screen):
    def __init__(self, **kwargs):
        super(WeightScreen, self).__init__(**kwargs)

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

        # Duration label and button
        weight_layout = BoxLayout(orientation='vertical')
        weight_label = Label(text="[color=#404040]Weight[/color]", pos_hint={'x': 0., 'y': .5}, markup=True)
        self.weight_input_field = FloatInput()
        weight_layout.add_widget(weight_label)
        weight_layout.add_widget(self.weight_input_field)

        # Date label and button
        date_layout = BoxLayout(orientation='vertical')
        self.date_label = Label(text="[color=#404040]Date[/color]",
                                pos_hint={'x': 0., 'y': .5},
                                markup=True)
        date_button = Button(text="Select date",
                             background_color=[0.24, 0.44, 0.40, 1.0],
                             size_hint=(0.5, 1),
                             pos_hint={'center_x': .5, "center_y": .5})
        date_button.bind(on_release=self.date_picker_transition)
        date_layout.add_widget(self.date_label)
        date_layout.add_widget(date_button)

        body_layout.add_widget(date_layout)

        body_layout.add_widget(weight_layout)

        button_layout = BoxLayout(orientation='vertical')
        button = Button(text="Add Weight",
                        background_color=[0.24, 0.44, 0.40, 1.0],
                        pos_hint={'center_x': .5, "center_y": .5},
                        size_hint=(0.5, 1))
        button.bind(on_release=self.add_weight)
        button_layout.add_widget(Label(text=""))
        button_layout.add_widget(button)

        body_layout.add_widget(button_layout)
        layout.add_widget(body_layout)
        self.add_widget(layout)

    def add_weight(self, instance):
        Weight(weight=self.weight_input_field.get_value(),
               weighed_at=self.parent.chosen_date,
               user_id=self.parent.current_user.id).create()
        self.welcome(instance)

    def date_picker_transition(self, instance):
        self.manager.transition.direction = "left"
        self.parent.previous = "weight"
        self.manager.current = "date_picker"

    def on_pre_enter(self, *args):
        self.date_label.text = "[color=#404040]Date: {0}[/color]".format(self.parent.chosen_date)

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"