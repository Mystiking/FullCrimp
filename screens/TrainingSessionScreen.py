from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image



class TrainingSessionScreen(Screen):
    def __init__(self, **kwargs):
        super(TrainingSessionScreen, self).__init__(**kwargs)

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
        yoga_button = Button(text="Yoga",
                             background_color=[0.24, 0.44, 0.40, 1.0])
        strength_button = Button(text="Strength",
                                 background_color=[0.24, 0.44, 0.40, 1.0])
        climbing_button = Button(text="Climbing",
                                 background_color=[0.24, 0.44, 0.40, 1.0])
        running_button = Button(text="Running",
                                background_color=[0.24, 0.44, 0.40, 1.0])

        yoga_button.bind(on_release=self.yoga_session_transition)
        strength_button.bind(on_release=self.strength_session_transition)
        climbing_button.bind(on_release=self.climbing_session_transition)
        running_button.bind(on_release=self.running_session_transition)

        button_layout.add_widget(running_button)
        button_layout.add_widget(climbing_button)
        button_layout.add_widget(strength_button)
        button_layout.add_widget(yoga_button)
        layout.add_widget(button_layout)

        self.add_widget(layout)

    def yoga_session_transition(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "yoga"

    def strength_session_transition(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "strength"

    def climbing_session_transition(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "climbing"

    def running_session_transition(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "running"

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"
