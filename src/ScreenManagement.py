from src.User import User
from kivy.uix.screenmanager import ScreenManager


class ScreenManagement(ScreenManager):
    current_user: User

    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

    def set_user(self, user: User):
        self.current_user = user
