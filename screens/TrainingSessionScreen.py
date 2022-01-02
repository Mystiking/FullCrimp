from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout


class TrainingSessionScreen(Screen):
    def __init__(self, **kwargs):
        super(TrainingSessionScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')
        self.label = Label(text="SELECT SESSION TYPE", size_hint=(1, .1))
        layout.add_widget(self.label)
        yoga_button = Button(text="Yoga",
                             background_color=[0.0, 1.0, 0.0, 1.0])
        strength_button = Button(text="Strength",
                                 background_color=[0.0, 1.0, 0.0, 1.0])
        climbing_button = Button(text="Climbing",
                                 background_color=[0.0, 1.0, 0.0, 1.0])
        running_button = Button(text="Running",
                                background_color=[0.0, 1.0, 0.0, 1.0])

        yoga_button.bind(on_release=self.yoga_session_transition)
        strength_button.bind(on_release=self.strength_session_transition)
        climbing_button.bind(on_release=self.climbing_session_transition)
        running_button.bind(on_release=self.running_session_transition)

        layout.add_widget(yoga_button)
        layout.add_widget(strength_button)
        layout.add_widget(climbing_button)
        layout.add_widget(running_button)

        self.add_widget(layout)

    def yoga_session_transition(self, instance):
        self.manager.current = "yoga"

    def strength_session_transition(self, instance):
        self.manager.current = "strength"

    def climbing_session_transition(self, instance):
        self.manager.current = "climbing"

    def running_session_transition(self, instance):
        self.manager.current = "running"

