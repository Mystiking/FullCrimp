from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from src.User import User


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')
        label = Label(text="FULLCRIMP", size_hint=(1, .5))
        layout.add_widget(label)

        username_label = Label(text="Username", pos_hint={'x': 0., 'y': .5})
        username_input_field = TextInput()
        password_label = Label(text="Password", pos_hint={'x': 0., 'y': .5})
        password_input_field = TextInput()

        layout.add_widget(username_label)
        layout.add_widget(username_input_field)
        layout.add_widget(password_label)
        layout.add_widget(password_input_field)

        button = Button(text="Login",
                        background_color=[1.0, 0.0, 0.0, 1.0])

        button.bind(on_release=lambda _: self.login(username_input_field.text, password_input_field.text))
        layout.add_widget(button)
        self.add_widget(layout)

    def screen_transition(self):
        self.manager.current = "welcome"

    def login(self, username: str, password: str):
        try:
            self.parent.current_user = User.get_user(username, password)
        except User.UsernameOrPasswordWrong:
            print(username, password)
        print("Success!")
        self.screen_transition()
