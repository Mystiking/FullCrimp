from kivy.app import App
from kivy.core.window import Window
from src.ScreenManagement import ScreenManager

from src.User import User

from screens.GymWallsScreen import GymWallsScreen
from screens.LoginScreen import LoginScreen
from screens.MainMenuScreen import MainMenuScreen
from screens.GymStatsScreen import GymStatsScreen


class MainApp(App):
    screen_manager: ScreenManager
    current_user: User

    def build(self):
        Window.clearcolor = (0.93, 0.95, 0.96, 1)
        Window.size = (480, 800)

        gym_walls_screen = GymWallsScreen(name="GymWalls")
        gym_walls_screen.update(None)
        login_screen = LoginScreen(name="Login")
        main_menu_screen = MainMenuScreen(name="MainMenu")
        gym_stats_screen = GymStatsScreen(name="GymStats")

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(login_screen)
        self.screen_manager.add_widget(gym_walls_screen)
        self.screen_manager.add_widget(main_menu_screen)
        self.screen_manager.add_widget(gym_stats_screen)

        self.screen_manager.current = "Login"
        return self.screen_manager


if __name__ == '__main__':
    app = MainApp()
    app.run()
