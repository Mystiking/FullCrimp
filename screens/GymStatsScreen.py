from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

from src.Grade import GradeEnum
from src.Route import Route


class GymStatsScreen(Screen):
    def __init__(self, **kwargs):
        super(GymStatsScreen, self).__init__(**kwargs)

        self.layout = FloatLayout(size_hint=(1, 1))
        stat_container = BoxLayout(orientation='vertical', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        stats = GymStatsScreen.get_stats()

        main_menu_button = Button(background_normal='assets/misc/Logout.png', size_hint=(None, None), size=(50, 50), pos_hint={'center_x': 0.1, 'center_y': 0.965})
        main_menu_button.bind(on_press=self.main_menu)

        for k in stats:
            stat_layout = BoxLayout(orientation='horizontal', size_hint=(0.8, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
            stat_image = Image(source='assets/difficulties/' + k.replace(' ', '') + '.png', size_hint=(1, 1), pos_hint={'center_x': 0.9, 'center_y': 0.5})
            stat_label = Label(text='[color=#000000]{0} routes[/color]'.format(stats[k]), pos_hint={'center_x': 0.5, 'center_y': 0.5}, markup=True)
            stat_layout.add_widget(stat_image)
            stat_layout.add_widget(stat_label)

            stat_container.add_widget(stat_layout)

        with self.canvas.before:
            Color(0.83, 0.85, 0.86, 1)
            self.rect = Rectangle(size=(480, 800))
        self.layout.add_widget(stat_container)
        self.layout.add_widget(main_menu_button)
        self.add_widget(self.layout)

    @staticmethod
    def get_stats():
        routes = Route.get_routes_from_db()
        difficulties = {'Easy': 0, 'Tricky': 0, 'Difficult': 0, 'Hard': 0, 'Very Hard': 0, 'Extreme': 0}
        for r in routes:
            print(GradeEnum.map_to_range(r.grade))
            difficulties[GradeEnum.map_to_range(r.grade)] += 1

        return difficulties

    def main_menu(self, touch):
        self.manager.transition.direction = "right"
        self.manager.current = "MainMenu"
