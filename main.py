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
from screens.WeightScreen import WeightScreen
from screens.StrengthScreen import StrengthScreen
from screens.StrengthSessionScreen import StrengthSessionScreen
from screens.HangboardScreen import HangboardScreen
from screens.HangboardSessionScreen import HangboardSessionScreen
from screens.StrengthTestScreen import StrengthTestScreen

from src.ScreenManagement import ScreenManagement

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from custom_kivy.CenteredTextInput import CenteredTextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.scatter import ScatterPlane

import cv2

def resize(src, factor, interpolation=cv2.INTER_AREA):
    """ Resizes an image by the specified factor keeping the aspect ratio

    :param src: Image to be resized
    :param scale: Resize factor
    :param interpolation:
    :return: Resized image
    """
    height = src.shape[0]
    width = src.shape[1]
    dimensions = (int(height*factor), int(width*factor))
    return cv2.resize(src, dimensions, interpolation=interpolation)

def addToImage(pos):
    s = 'assets/logo/logo_eliptic.png'

    i = cv2.imread(s)
    i2 = resize(i, 0.25)
    i[pos[0]:pos[0]+i2.shape[0], pos[1]:pos[1]+i2.shape[1]] = i2
    o = 'assets/logo/logo_eliptic_temp.png'
    cv2.imwrite(o, i)

    return o


class MyImage(Image):

    points = []
    scatterPlane = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.points = [*touch.pos]
            self.reload()
            print(self.points, "" if (self.scatterPlane is None) else self.scatterPlane.scale)

            s = addToImage([int(p) for p in self.points])
            self.source = s
            self.reload()
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            self.points.extend(touch.pos)
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            touch.ungrab(self)
            self.points.extend(touch.pos)
        return super().on_touch_up(touch)

    def clear(self):
        self.points = []


class MyScatterPlane(ScatterPlane):
    def on_touch_down(self, touch):
        return super().on_touch_down(touch)

class MainApp(App):
    screen_manager: ScreenManager
    current_user: User

    def build(self):
        Window.clearcolor = (0.93, 0.95, 0.96, 1)

        sv = MyScatterPlane(scale=1)
        logo = MyImage(source='assets/logo/logo_eliptic.png',
                       size_hint=(None, None),
                       size=Window.size)
        logo.scatterPlane = sv
        sv.add_widget(logo)

        return sv
        # self.current_user = User.create_user("Louise1337", "password", "Louise")
        '''
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
        self.screen_manager.add_widget(WeightScreen(name="weight"))
        self.screen_manager.add_widget(StrengthScreen(name="strength"))
        self.screen_manager.add_widget(HangboardScreen(name="hangboard"))
        self.screen_manager.add_widget(HangboardSessionScreen(name="hangboard_session"))
        self.screen_manager.add_widget(StrengthSessionScreen(name="strength_session"))
        self.screen_manager.add_widget(StrengthTestScreen(name="strength_test"))

        self.screen_manager.current = "login"

        return self.screen_manager
        '''


if __name__ == '__main__':
    app = MainApp()
    app.run()
