from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from src.TrainingType import TrainingType
from src.RunningSession import RunningSession
from datetime import date


class RunningScreen(Screen):
    def __init__(self, **kwargs):
        super(RunningScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')
        self.label = Label(text="New Running Session", size_hint=(1, .1))
        layout.add_widget(self.label)

        duration_label = Label(text="duration", pos_hint={'x': 0., 'y': .5})
        self.duration_input_field = TextInput()

        date_label = Label(text="date", pos_hint={'x': 0., 'y': .5})
        self.date_input_field = TextInput()

        location_label = Label(text="location", pos_hint={'x': 0., 'y': .5})
        self.location_input_field = TextInput()

        distance_label = Label(text="distance", pos_hint={'x': 0., 'y': .5})
        self.distance_input_field = TextInput()

        layout.add_widget(duration_label)
        layout.add_widget(self.duration_input_field)
        layout.add_widget(date_label)
        layout.add_widget(self.date_input_field)
        layout.add_widget(location_label)
        layout.add_widget(self.location_input_field)
        layout.add_widget(distance_label)
        layout.add_widget(self.distance_input_field)

        button = Button(text="Add Running Session",
                        background_color=[0.0, 1.0, 0.0, 1.0])
        button.bind(on_release=self.add_running_session)
        layout.add_widget(button)
        self.add_widget(layout)

    def screen_transition(self, instance):
        self.manager.current = "welcome"

    def add_running_session(self, instance):
        RunningSession(duration=float(self.duration_input_field.text),
                       location=self.location_input_field.text,
                       training_type=TrainingType.RUNNING,
                       user_id=self.parent.current_user.id,
                       distance=float(self.distance_input_field.text),
                       performed_at=date.today()).create()
        self.screen_transition(instance)
