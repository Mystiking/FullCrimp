from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from custom_kivy.TimeInput import TimeInput
from src.ClimbingTypes import ClimbingType, ClimbingGym
from src.ClimbingSession import ClimbingSession
from src.TrainingType import TrainingType


class BoulderingScreen(Screen):
    gym_strings = {
        ClimbingGym.BETA_BOULDERS_WEST: "Beta Boulders (West)",
        ClimbingGym.BETA_BOULDERS_SOUTH: "Beta Boulders (South)",
        ClimbingGym.BLOCKS_AND_WALLS: "Blocks & Walls",
        ClimbingGym.OUTSIDE: "Outside"
    }

    def __init__(self, **kwargs):
        super(BoulderingScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')

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
        layout.add_widget(logo_layout)

        body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.8))

        # Gym label
        gym_layout = BoxLayout(orientation='vertical')
        self.gym_label = Label(text="",
                               pos_hint={'x': 0., 'y': .5},
                               markup=True)
        gym_layout.add_widget(self.gym_label)

        # Duration label and button
        duration_layout = BoxLayout(orientation='vertical')
        duration_label = Label(text="[color=#404040]Duration[/color]", pos_hint={'x': 0., 'y': .5}, markup=True)
        self.duration_input_field = TimeInput()
        duration_layout.add_widget(duration_label)
        duration_layout.add_widget(self.duration_input_field)

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

        climbs_layout = BoxLayout(orientation='vertical')
        self.climbs_label = Label(text="[color=#404040]Climbs:[/color]",
                                  pos_hint={'x': 0., 'y': .5},
                                  markup=True)
        add_climb_button = Button(text="Add another climb",
                                  background_color=[0.24, 0.44, 0.40, 1.0],
                                  size_hint=(0.5, 1),
                                  pos_hint={'center_x': .5, "center_y": .5})
        add_climb_button.bind(on_release=self.add_climb)

        climbs_layout.add_widget(self.climbs_label)
        climbs_layout.add_widget(add_climb_button)

        body_layout.add_widget(gym_layout)

        body_layout.add_widget(date_layout)

        body_layout.add_widget(duration_layout)

        body_layout.add_widget(climbs_layout)

        button_layout = BoxLayout(orientation='vertical')
        button = Button(text="Add Session",
                        background_color=[0.24, 0.44, 0.40, 1.0],
                        pos_hint={'center_x': .5, "center_y": .5},
                        size_hint=(0.5, 1))
        button.bind(on_release=self.add_bouldering_session)
        button_layout.add_widget(Label(text=""))
        button_layout.add_widget(button)

        body_layout.add_widget(button_layout)
        layout.add_widget(body_layout)
        self.add_widget(layout)

    def add_bouldering_session(self, instance):
        ClimbingSession(duration=float(self.duration_input_field.text) if self.duration_input_field.text != '' else 0.0,
                        location="",
                        training_type=TrainingType.CLIMBING,
                        user_id=self.parent.current_user.id,
                        climbing_gym=self.parent.current_gym,
                        climbing_type=self.parent.climbing_type,
                        climbs=self.parent.climbs,
                        performed_at=self.parent.chosen_date).create()
        self.welcome(instance)

    def add_climb(self, instance):
        self.manager.transition.direction = "left"
        self.parent.previous = "bouldering"
        self.parent.climbing_type = ClimbingType.BOULDERING
        self.manager.current = "grade_picker"

    def date_picker_transition(self, instance):
        self.manager.transition.direction = "left"
        self.parent.previous = "bouldering"
        self.manager.current = "date_picker"

    def welcome(self, instance):
        self.parent.climbs = []
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"

    def create_climbs_text(self, climbs):
        keys = set(climbs)
        num_occurences = []
        for key in keys:
            num_occurences.append("{0} x {1}".format(key, climbs.count(key)))
        return ", ".join(num_occurences)

    def on_pre_enter(self, *args):
        self.date_label.text = "[color=#404040]Date: {0}[/color]".format(self.parent.chosen_date)
        self.gym_label.text = "[color=#404040]Gym: {0}[/color]".format(self.gym_strings[self.parent.climbing_gym])
        self.climbs_label.text = "[color=#404040]Climbs: {0}[/color]".format(self.create_climbs_text(self.parent.climbs))