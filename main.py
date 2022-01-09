from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.image import Image

from datetime import date

from src.User import User
from src.TrainingType import TrainingType
from src.RunningSession import RunningSession

from screens.LoginScreen import LoginScreen
from screens.WelcomeScreen import WelcomeScreen
from screens.RunningScreen import RunningScreen
from screens.YogaScreen import YogaScreen
from screens.TrainingSessionScreen import TrainingSessionScreen
from screens.DatePickerScreen import DatePickerScreen
from screens.ClimbingScreen import ClimbingSessionScreen
from screens.RopeClimbingScreen import RopeClimbingScreen
from screens.GradePickerScreen import GradePickerScreen
from screens.BoulderingScreen import BoulderingScreen
from screens.HomeWallScreen import HomeWallScreen
from screens.GymPickerScreen import GymPickerScreen

from src.ScreenManagement import ScreenManagement


class MainApp(App):
    screen_manager: ScreenManager
    current_user: User

    def build(self):
        Window.clearcolor = (0.93, 0.95, 0.96, 1)
        # self.current_user = User.create_user("Louise1337", "password", "Louise")
        self.screen_manager = ScreenManagement()

        self.screen_manager.chosen_date = date.today()
        self.screen_manager.location = ""
        self.screen_manager.previous_screen = ""
        self.screen_manager.current_user = None
        self.screen_manager.current_gym = None
        self.screen_manager.climbs = []
        self.screen_manager.climbing_type = None
        # Add the different screens
        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(WelcomeScreen(name="welcome"))
        self.screen_manager.add_widget(TrainingSessionScreen(name="training_session"))
        self.screen_manager.add_widget(RunningScreen(name="running"))
        self.screen_manager.add_widget(YogaScreen(name="yoga"))
        self.screen_manager.add_widget(DatePickerScreen(name="date_picker"))
        self.screen_manager.add_widget(ClimbingSessionScreen(name="climbing"))
        self.screen_manager.add_widget(RopeClimbingScreen(name="rope_climbing"))
        self.screen_manager.add_widget(GradePickerScreen(name="grade_picker"))
        self.screen_manager.add_widget(GymPickerScreen(name="gym_picker"))
        self.screen_manager.add_widget(BoulderingScreen(name="bouldering"))
        self.screen_manager.add_widget(HomeWallScreen(name="home_wall"))

        self.screen_manager.current = "login"

        return self.screen_manager


if __name__ == '__main__':
    app = MainApp()
    app.run()
