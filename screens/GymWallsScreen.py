from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from custom_kivy.CenteredTextInput import CenteredTextInput
from kivy.uix.image import Image
from kivy.core.window import Window

import os

from src.User import User


class MyImage(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(self.source)


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')


        sv = ScrollView(size=Window.size)
        logo = Image(source='assets/logo/logo_eliptic.png',
                     size_hint=(1.0, 1.0),
                     pos_hint={'center_x': .5, "center_y": .5})
        sv.add_widget(logo)

        layout.add_widget(sv)
