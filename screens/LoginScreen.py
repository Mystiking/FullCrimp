from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from custom_kivy.CenteredTextInput import CenteredTextInput
from kivy.uix.image import Image

import os

from src.User import User


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')
        label = Label(text="[color=#404040][font=assets/fonts/vonique/Vonique64.ttf]Fu llC r i m p[/font][/color]", size_hint=(1, .5),
                      markup=True, font_size=26)

        logo = Image(source='assets/logo/logo_eliptic.png',
                     size_hint=(1.0, 1.0),
                     pos_hint={'center_x': .5, "center_y": .5})

        layout.add_widget(logo)
        layout.add_widget(label)

        username_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.5))
        password_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.5))

        username_label = Label(text="[color=#404040]Username[/color]",
                               markup=True,
                               size_hint=(0.75, 0.5),
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.5},
                               )
        self.username_input_field = CenteredTextInput(size_hint=(0.75, 0.5),
                                                      pos_hint={'center_x': 0.5,
                                                                'center_y': 0.5},
                                                      multiline=False)

        def text_changed(text_input, text):
            if len(text) > 0:
                if text[-1] == '\t':
                    text_input.text = text[:-1]
                    if self.username_input_field.focus:
                        self.username_input_field.focus = False
                        self.password_input_field.focus = True
                    else:
                        self.username_input_field.focus = True
                        self.password_input_field.focus = False

        self.username_input_field.bind(text=text_changed)
        self.username_input_field.bind(
            on_text_validate=lambda *args: self.login(self.username_input_field.text, self.password_input_field.text))
        password_label = Label(text="[color=#404040]Password[/color]",
                               markup=True,
                               size_hint=(0.75, 0.5),
                               pos_hint={'center_x': 0.5,
                                         'center_y': 0.5}
                               )
        self.password_input_field = TextInput(password=True,
                                              size_hint=(0.75, 0.5),
                                              pos_hint={'center_x': 0.5,
                                                        'center_y': 0.5},
                                              multiline=False,
                                              on_text=lambda args: print(args))
        self.password_input_field.bind(text=text_changed)
        self.password_input_field.bind(
            on_text_validate=lambda *args: self.login(self.username_input_field.text, self.password_input_field.text))
        username_layout.add_widget(username_label)
        username_layout.add_widget(self.username_input_field)

        password_layout.add_widget(password_label)
        password_layout.add_widget(self.password_input_field)

        login_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, .3))
        login_button = Button(text="Login",
                              background_color=[0.24, 0.44, 0.40, 1.0],
                              size_hint=(0.75, 1.0),
                              pos_hint={'center_x': 0.5,
                                        'center_y': 0.1},
                              )
        login_button.bind(on_release=lambda _: self.login(self.username_input_field.text, self.password_input_field.text))

        login_layout.add_widget(login_button)

        self.notification_label = Label(text="",
                                        markup=True,
                                        size_hint=(0.75, 0.1),
                                        pos_hint={'center_x': 0.5,
                                                  'center_y': 0.5})

        layout.add_widget(username_layout)
        layout.add_widget(password_layout)
        layout.add_widget(login_layout)
        layout.add_widget(self.notification_label)

        self.username_input_field.focus = True
        self.get_cached_login_info()
        self.add_widget(layout)

    def get_cached_login_info(self):
        if os.path.exists('.cache/.logincache'):
            with open('.cache/.logincache', 'r') as fh:
                data = fh.read().split(' ')
                self.username_input_field.text = data[0]
                self.password_input_field.text = data[1]

    def cache_login_info(self):
        with open('.cache/.logincache', 'w') as fh:
            fh.write('{0} {1}'.format(self.username_input_field.text, self.password_input_field.text))

    def screen_transition(self):
        self.manager.transition.direction = "left"
        self.manager.current = "welcome"

    def login(self, username: str, password: str):
        try:
            self.parent.current_user = User.get_user(username, password)
            self.cache_login_info()
            self.screen_transition()
        except User.UsernameOrPasswordWrong:
            self.get_cached_login_info()
            self.notification_label.text = "[color=#FF4040]Wrong username or password.[/color]"

            if self.password_input_field.focus:
                self.password_input_field.focus = False
                self.username_input_field.focus = True
            else:
                self.password_input_field.focus = True
                self.username_input_field.focus = False

