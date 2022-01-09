from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from custom_kivy.TimeInput import TimeInput
from src.ClimbingTypes import ClimbingType, ClimbingGym
from src.ClimbingSession import ClimbingSession
from src.TrainingType import TrainingType


class GymPickerScreen(Screen):
    def __init__(self, **kwargs):
        super(GymPickerScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(padding=50, orientation='vertical')

        logo_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.25))
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
        self.layout.add_widget(logo_layout)

        self.body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.8))

        self.layout.add_widget(self.body_layout)
        self.add_widget(self.layout)

    def welcome(self, instance):
        self.parent.climbs = []
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"

    def set_gym(self, gym):
        self.parent.climbing_gym = gym
        self.manager.transition.direction = "left"
        if self.parent.climbing_type == ClimbingType.BOULDERING:
            self.manager.current = "bouldering"
        else:
            self.manager.current = "rope_climbing"

    def on_pre_enter(self, *args):
        self.remove_widget(self.layout)
        self.layout.remove_widget(self.body_layout)
        self.body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.8))
        if self.parent.climbing_type == ClimbingType.LEAD or self.parent.climbing_type == ClimbingType.TOPROPE:
            blocks_and_walls_button = Button(text="Blocks & Walls",
                                             background_color=[0.24, 0.44, 0.40, 1.0],
                                             pos_hint={'center_x': .5, "center_y": .5},
                                             size_hint=(1.0, 1))
            blocks_and_walls_button.bind(on_release=lambda *args: self.set_gym(ClimbingGym.BLOCKS_AND_WALLS))
            outside_button = Button(text="Outside",
                                    background_color=[0.24, 0.44, 0.40, 1.0],
                                    pos_hint={'center_x': .5, "center_y": .5},
                                    size_hint=(1.0, 1))
            outside_button.bind(on_release=lambda *args: self.set_gym(ClimbingGym.OUTSIDE))
            self.body_layout.add_widget(blocks_and_walls_button)
            self.body_layout.add_widget(outside_button)
        else:  # This is a bouldering session
            beta_boulder_west_button = Button(text="Beta Boulders (West)",
                                              background_color=[0.24, 0.44, 0.40, 1.0],
                                              pos_hint={'center_x': .5, "center_y": .5},
                                              size_hint=(1.0, 1))
            beta_boulder_west_button.bind(on_release=lambda *args: self.set_gym(ClimbingGym.BETA_BOULDERS_WEST))
            beta_boulder_south_button = Button(text="Beta Boulders (South)",
                                               background_color=[0.24, 0.44, 0.40, 1.0],
                                               pos_hint={'center_x': .5, "center_y": .5},
                                               size_hint=(1.0, 1))
            beta_boulder_south_button.bind(on_release=lambda *args: self.set_gym(ClimbingGym.BETA_BOULDERS_SOUTH))
            self.body_layout.add_widget(beta_boulder_west_button)
            self.body_layout.add_widget(beta_boulder_south_button)
        self.layout.add_widget(self.body_layout)
        self.add_widget(self.layout)