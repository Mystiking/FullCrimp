from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')
        self.label = Label(text="WELCOME", size_hint=(1, .5))
        layout.add_widget(self.label)
        button = Button(text="Add Session",
                        background_color=[0.0, 1.0, 0.0, 1.0])
        button.bind(on_release=self.screen_transition)
        layout.add_widget(button)
        self.add_widget(layout)

    def screen_transition(self, instance):
        print(self.parent.current_user)
        self.manager.current = "training_session"

    def on_pre_enter(self, *args):
        self.label.text = "WELCOME " + self.parent.current_user.name
