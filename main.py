from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from src.User import User
from src.TrainingType import TrainingType
from src.RunningSession import RunningSession

from screens.LoginScreen import LoginScreen
from screens.WelcomeScreen import WelcomeScreen
from screens.RunningScreen import RunningScreen
from screens.TrainingSessionScreen import TrainingSessionScreen
from src.ScreenManagement import ScreenManagement


class MainApp(App):
    screen_manager: ScreenManager
    current_user: User

    def create_tables(self):
        pass

    def build(self):
        # self.current_user = User.create_user("Louise1337", "password", "Louise")
        self.screen_manager = ScreenManagement()
        # Add the different screens
        self.screen_manager.add_widget(LoginScreen(name="login"))
        self.screen_manager.add_widget(WelcomeScreen(name="welcome"))
        self.screen_manager.add_widget(TrainingSessionScreen(name="training_session"))
        self.screen_manager.add_widget(RunningScreen(name="running"))

        self.screen_manager.current = "login"

        #User.get_user()
        #self.login("Louise1337", "password")

        #session = RunningSession(0.0, "Home", TrainingType.RUNNING, self.current_user.id, 100.0)
        #session.create()

        return self.screen_manager


if __name__ == '__main__':
    app = MainApp()
    app.run()
