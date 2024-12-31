from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout


class MainMenuScreen(Screen):

    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', size_hint=(1, 1))

        gym_button = Button(text="Show gym", size_hint=(1, 0.25), pos_hint={'center_x' : 0.5, 'center_y': 0.5})
        stats_button = Button(text="Show stats", size_hint=(1, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        gym_button.bind(on_press=self.show_gym_screen)
        stats_button.bind(on_press=self.show_stats_screen)
        self.layout.add_widget(gym_button)
        self.layout.add_widget(stats_button)

        self.add_widget(self.layout)

    def show_gym_screen(self, touch):
        self.manager.transition.direction = "left"
        self.manager.current = "GymWalls"

    def show_stats_screen(self, touch):
        self.manager.transition.direction = "left"
        self.manager.current = "GymStats"
