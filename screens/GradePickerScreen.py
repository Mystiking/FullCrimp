from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from src.TrainingType import TrainingType
from src.RunningSession import RunningSession
from datetime import date
from custom_kivy.DatePicker import DatePicker
from kivy.uix.image import Image
from src.ClimbingTypes import ClimbingGym
from src.ClimbingTypes import ClimbingType
from src.ClimbingTypes import BetaBouldersGrade


class GradePickerScreen(Screen):
    grade_options = {
        ClimbingType.TOPROPE: 'font',
        ClimbingType.LEAD: 'font',
        ClimbingType.BOULDERING:
            {
                ClimbingGym.BETA_BOULDERS_WEST: [
                    BetaBouldersGrade.CYAN,
                    BetaBouldersGrade.GREEN,
                    BetaBouldersGrade.YELLOW,
                    BetaBouldersGrade.BLUE,
                    BetaBouldersGrade.ORANGE,
                    BetaBouldersGrade.RED,
                    BetaBouldersGrade.BLACK],
                ClimbingGym.BETA_BOULDERS_SOUTH: [
                    BetaBouldersGrade.CYAN,
                    BetaBouldersGrade.GREEN,
                    BetaBouldersGrade.YELLOW,
                    BetaBouldersGrade.BLUE,
                    BetaBouldersGrade.ORANGE,
                    BetaBouldersGrade.RED,
                    BetaBouldersGrade.BLACK]
            }
    }

    def __init__(self, **kwargs):
        super(GradePickerScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(padding=50, orientation='vertical',)
        logo_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.35))
        label = Button(text="[color=#404040][font=assets/fonts/vonique/Vonique64.ttf]Fu llC r i m p[/font][/color]",
                       size_hint=(0.25, .5),
                       background_color=[0.93, 0.95, 0.96, 1],
                       background_normal="",
                       background_down="",
                       markup=True,
                       font_size=26,
                       pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label.bind(on_press=self.welcome)
        logo = Image(source='assets/logo/logo_eliptic.png',
                     size_hint=(1.0, 1.0),
                     pos_hint={'center_x': .5, "center_y": .5})

        logo_layout.add_widget(logo)
        logo_layout.add_widget(label)
        self.layout.add_widget(logo_layout)

        self.body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.65))

        self.layout.add_widget(self.body_layout)
        self.add_widget(self.layout)

    def select_grade(self, instance):
        self.parent.chosen_date = self.date_input_field.date
        self.manager.transition.direction = "right"
        self.manager.current = self.parent.previous

    def outer_grades(self, gym):
        self.parent.current_gym = gym
        self.remove_widget(self.layout)
        self.layout.remove_widget(self.body_layout)

        self.body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.65))
        if self.parent.climbing_type != ClimbingType.BOULDERING:
            grades = ['4', '5', '6', '7']
            for grade in grades:
                button = Button(text="{0}".format(grade),
                                background_color=[0.24, 0.44, 0.40, 1.0],
                                pos_hint={'center_x': .5, "center_y": .5},
                                size_hint=(1.0, 1))
                button.bind(on_release=lambda btn: self.inner_grades(btn.text))
                self.body_layout.add_widget(button)
        else:
            grades = self.grade_options[self.parent.climbing_type][gym]
            for grade in grades:
                button = Button(text="{0}".format(grade.value[0].upper() + grade.value[1:]),
                                background_color=[0.24, 0.44, 0.40, 1.0],
                                pos_hint={'center_x': .5, "center_y": .5},
                                size_hint=(1.0, 1))
                button.bind(on_release=lambda btn: self.add_grade(btn.text))
                self.body_layout.add_widget(button)

        self.layout.add_widget(self.body_layout)
        self.add_widget(self.layout)

    def inner_grades(self, grade):
        self.remove_widget(self.layout)
        self.layout.remove_widget(self.body_layout)

        self.body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.65))
        grades = ['a', 'a+', 'b', 'b+', 'c', 'c+']
        for subgrade in grades:
            button = Button(text="{0}".format(subgrade),
                            background_color=[0.24, 0.44, 0.40, 1.0],
                            pos_hint={'center_x': .5, "center_y": .5},
                            size_hint=(1.0, 1))
            button.bind(on_release=lambda btn: self.add_grade(grade + btn.text))
            self.body_layout.add_widget(button)

        self.layout.add_widget(self.body_layout)
        self.add_widget(self.layout)

    def add_grade(self, grade):
        self.parent.climbs.append(grade)
        self.manager.transition.direction = "right"
        self.manager.current = self.parent.previous

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"
        self.parent.climbs = []

    def on_pre_enter(self, *args):
        self.outer_grades(self.parent.climbing_gym)
        '''
        if self.parent.climbing_type == ClimbingType.TOPROPE or self.parent.climbing_type == ClimbingType.LEAD:
            self.remove_widget(self.layout)
            self.layout.remove_widget(self.body_layout)

            self.body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.65))
            outside_button = Button(text="Outside",
                                    background_color=[0.24, 0.44, 0.40, 1.0],
                                    pos_hint={'center_x': .5, "center_y": .5},
                                    size_hint=(1.0, 1))
            outside_button.bind(on_release=lambda *args: self.outer_grades(ClimbingGym.OUTSIDE))
            inside_button = Button(text="Blocks & Walls",
                                   background_color=[0.24, 0.44, 0.40, 1.0],
                                   pos_hint={'center_x': .5, "center_y": .5},
                                   size_hint=(1.0, 1))
            inside_button.bind(on_release=lambda *args: self.outer_grades(ClimbingGym.BLOCKS_AND_WALLS))
            self.body_layout.add_widget(inside_button)
            self.body_layout.add_widget(outside_button)

            self.layout.add_widget(self.body_layout)
            self.add_widget(self.layout)
        else:  # This is a bouldering session
            self.remove_widget(self.layout)
            self.layout.remove_widget(self.body_layout)

            self.body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.65))

            beta_boulder_west_button = Button(text="Beta Boulders (West)",
                                              background_color=[0.24, 0.44, 0.40, 1.0],
                                              pos_hint={'center_x': .5, "center_y": .5},
                                              size_hint=(1.0, 1))
            beta_boulder_west_button.bind(on_release=lambda *args: self.outer_grades(ClimbingGym.BETA_BOULDERS_WEST))
            beta_boulder_south_button = Button(text="Beta Boulders (South)",
                                               background_color=[0.24, 0.44, 0.40, 1.0],
                                               pos_hint={'center_x': .5, "center_y": .5},
                                               size_hint=(1.0, 1))
            beta_boulder_south_button.bind(on_release=lambda *args: self.outer_grades(ClimbingGym.BETA_BOULDERS_SOUTH))
            self.body_layout.add_widget(beta_boulder_west_button)
            self.body_layout.add_widget(beta_boulder_south_button)

            self.layout.add_widget(self.body_layout)
            self.add_widget(self.layout)
        '''