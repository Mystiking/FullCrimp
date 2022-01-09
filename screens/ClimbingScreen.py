from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from src.ClimbingTypes import ClimbingType


class ClimbingSessionScreen(Screen):
    def __init__(self, **kwargs):
        super(ClimbingSessionScreen, self).__init__(**kwargs)

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

        button_layout = BoxLayout(orientation='vertical', size_hint=(0.75, 0.75), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        toprope_button = Button(text="Toprope",
                                background_color=[0.24, 0.44, 0.40, 1.0])
        lead_button = Button(text="Lead",
                             background_color=[0.24, 0.44, 0.40, 1.0])
        bouldering_button = Button(text="Bouldering",
                                   background_color=[0.24, 0.44, 0.40, 1.0])
        home_wall_button = Button(text="Home Wall",
                                  background_color=[0.24, 0.44, 0.40, 1.0])

        toprope_button.bind(on_release=self.toprope_session_transition)
        lead_button.bind(on_release=self.lead_session_transition)
        bouldering_button.bind(on_release=self.bouldering_session_transition)
        home_wall_button.bind(on_release=self.home_wall_session_transition)

        button_layout.add_widget(bouldering_button)
        button_layout.add_widget(lead_button)
        button_layout.add_widget(toprope_button)
        button_layout.add_widget(home_wall_button)
        layout.add_widget(button_layout)

        self.add_widget(layout)

    def toprope_session_transition(self, instance):
        self.parent.climbing_type = ClimbingType.TOPROPE
        self.manager.transition.direction = "left"
        self.manager.current = "gym_picker"

    def lead_session_transition(self, instance):
        self.parent.climbing_type = ClimbingType.LEAD
        self.manager.transition.direction = "left"
        self.manager.current = "gym_picker"

    def bouldering_session_transition(self, instance):
        self.parent.climbing_type = ClimbingType.BOULDERING
        self.manager.transition.direction = "left"
        self.manager.current = "gym_picker"

    def home_wall_session_transition(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "home_wall"

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"
