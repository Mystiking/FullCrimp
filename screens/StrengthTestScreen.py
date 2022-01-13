from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from src.TrainingType import TrainingType
from src.YogaSession import YogaSession
from custom_kivy.FloatInput import FloatInput
from custom_kivy.TimeInput import TimeInput
from src.Weight import Weight
from src.StrengthTest9c import StrengthTest9c
from kivy.uix.checkbox import CheckBox


class StrengthTestScreen(Screen):
    def __init__(self, **kwargs):
        super(StrengthTestScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')

        logo_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 0.1))
        label = Button(text="[color=#404040][font=assets/fonts/vonique/Vonique64.ttf]Fu llC r i m p[/font][/color]", size_hint=(0.25, .5),
                       background_color=[0.93, 0.95, 0.96, 1],
                       background_normal="",
                       background_down="",
                       markup=True,
                       font_size=26,
                       pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label.bind(on_press=self.welcome)

        logo_layout.add_widget(label)
        # layout.add_widget(logo_layout)

        body_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, 1.0))

        top_fields = BoxLayout(orientation='vertical', size_hint=(1.0, 0.25))
        bottom_fields = BoxLayout(orientation='vertical', size_hint=(1.0, 0.75))

        weight_layout = BoxLayout(orientation='vertical')
        weight_label = Label(text="[color=#404040]Weight[/color]", pos_hint={'x': 0., 'y': .5}, markup=True)
        self.weight_input = FloatInput(size_hint=(0.25, 1), pos_hint={'x': 0.375, 'y': .5})
        weight_layout.add_widget(weight_label)
        weight_layout.add_widget(self.weight_input)

        # Date label and button
        date_layout = BoxLayout(orientation='vertical')
        self.date_label = Label(text="[color=#404040]Date[/color]",
                                pos_hint={'x': 0., 'y': .5},
                                markup=True)
        date_button = Button(text="Select date",
                             background_color=[0.24, 0.44, 0.40, 1.0],
                             size_hint=(0.5, 1),
                             pos_hint={'center_x': .5, "center_y": .5})
        date_button.bind(on_release=self.date_picker_transition)
        date_layout.add_widget(self.date_label)
        date_layout.add_widget(date_button)

        core_layout = BoxLayout(orientation='vertical')
        self.core_label = Label(text="[color=#404040]Core (Seconds): 0 Points[/color]", pos_hint={'x': 0., 'y': 0}, markup=True)
        self.core_input = TimeInput(size_hint=(0.25, 1.1), pos_hint={'x': 0.375, 'y': 0})
        level_0_label = Label(text="[color=#404040]Level 0:[/color]", markup=True)
        level_1_label = Label(text="[color=#404040]Level 1:[/color]", markup=True)
        level_2_label = Label(text="[color=#404040]Level 2:[/color]", markup=True)
        self.level_0 = CheckBox(color=[0.15, 0.15, 0.15, 1], group='1')
        self.level_1 = CheckBox(color=[0.15, 0.15, 0.15, 1], group='1')
        self.level_2 = CheckBox(color=[0.15, 0.15, 0.15, 1], group='1')
        checkbutton_layout = BoxLayout(orientation='horizontal')
        checkbutton_layout.add_widget(level_0_label)
        checkbutton_layout.add_widget(self.level_0)
        checkbutton_layout.add_widget(level_1_label)
        checkbutton_layout.add_widget(self.level_1)
        checkbutton_layout.add_widget(level_2_label)
        checkbutton_layout.add_widget(self.level_2)
        core_layout.add_widget(self.core_label)
        core_layout.add_widget(checkbutton_layout)
        core_layout.add_widget(self.core_input)

        pull_up_layout = BoxLayout(orientation='vertical')
        self.pull_up_label = Label(text="[color=#404040]Pull-ups (X kg): 0 Points[/color]", pos_hint={'x': 0., 'y': 0}, markup=True)
        self.pull_up_input = FloatInput(size_hint=(0.25, 1), pos_hint={'x': 0.375, 'y': 0})
        pull_up_layout.add_widget(self.pull_up_label)
        pull_up_layout.add_widget(self.pull_up_input)

        hangtime_layout = BoxLayout(orientation='vertical')
        self.hangtime_label = Label(text="[color=#404040]Hang time (Seconds): 0 Points[/color]", pos_hint={'x': 0., 'y': 0}, markup=True)
        self.hangtime_input = TimeInput(size_hint=(0.25, 1), pos_hint={'x': 0.375, 'y': 0})
        hangtime_layout.add_widget(self.hangtime_label)
        hangtime_layout.add_widget(self.hangtime_input)

        hangboard_layout = BoxLayout(orientation='vertical')
        self.hangboard_label = Label(text="[color=#404040]Hang board (20mm, +X kg): 0 Points[/color]", pos_hint={'x': 0., 'y': 0},
                                     markup=True)
        self.hangboard_input = FloatInput(size_hint=(0.25, 1), pos_hint={'x': 0.375, 'y': 0})
        hangboard_layout.add_widget(self.hangboard_label)
        hangboard_layout.add_widget(self.hangboard_input)

        button_layout = BoxLayout(orientation='horizontal')
        update_button = Button(text="Update Points",
                               background_color=[0.24, 0.44, 0.40, 1.0],
                               pos_hint={'center_x': .5, "center_y": .5},
                               size_hint=(0.25, 0.5))
        update_button.bind(on_release=self.update_points)
        add_button = Button(text="Save Results",
                            background_color=[0.24, 0.44, 0.40, 1.0],
                            pos_hint={'center_x': .5, "center_y": .5},
                            size_hint=(0.25, 0.5))
        add_button.bind(on_release=self.add_result)
        button_layout.add_widget(update_button)
        button_layout.add_widget(add_button)

        self.grade_label = Label(text="[color=#404040]Climbing grade: ?[/color]", pos_hint={'x': 0., 'y': 0},
                                 markup=True)

        top_fields.add_widget(weight_layout)
        top_fields.add_widget(date_layout)

        bottom_fields.add_widget(core_layout)
        bottom_fields.add_widget(pull_up_layout)
        bottom_fields.add_widget(hangtime_layout)
        bottom_fields.add_widget(hangboard_layout)
        bottom_fields.add_widget(button_layout)
        bottom_fields.add_widget(self.grade_label)

        body_layout.add_widget(top_fields)
        body_layout.add_widget(bottom_fields)
        layout.add_widget(body_layout)
        self.add_widget(layout)

    def date_picker_transition(self, instance):
        self.manager.transition.direction = "left"
        self.parent.previous = "strength_test"
        self.manager.current = "date_picker"

    def welcome(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "welcome"

    def on_pre_enter(self, *args):
        self.date_label.text = "[color=#404040]Date: {0}[/color]".format(self.parent.chosen_date)
        self.try_get_weight()
        self.level_0.active = True

    def add_result(self, instance):
        current_weight = self.weight_input.get_value()
        level = 0 if self.level_0.active else (1 if self.level_1.active else 2)
        core_exercise = ['L_sit_bend_knees', 'L_sit', 'Front_Lever'][level]
        core_time = self.core_input.to_seconds()
        hang_time = self.hangtime_input.to_seconds()
        pull_up_weight = self.pull_up_input.get_value()
        hangboard_weight = self.hangboard_input.get_value()
        StrengthTest9c(
            weight=current_weight,
            core_level=core_exercise,
            core_time=core_time,
            pull_up_weight=pull_up_weight,
            hangtime=hang_time,
            hangboard_weight=hangboard_weight,
            performed_at=self.parent.chosen_date
        ).create(self.parent.current_user.id)
        self.welcome(instance)

    def try_get_weight(self):
        current_weight = Weight.get_latest_weight(self.parent.current_user.id)
        if not (current_weight is None):
            self.weight_input.text = str(current_weight)

    def update_points(self, instance):
        current_weight = self.weight_input.get_value()
        level = 0 if self.level_0.active else (1 if self.level_1.active else 2)
        core_exercise = ['L_sit_bend_knees', 'L_sit', 'Front_Lever'][level]
        core_time = self.core_input.to_seconds()
        hang_time = self.hangtime_input.to_seconds()
        pull_up_weight = self.pull_up_input.get_value()
        hangboard_weight = self.hangboard_input.get_value()
        points, grade = StrengthTest9c(
            weight=current_weight,
            core_level=core_exercise,
            core_time=core_time,
            pull_up_weight=pull_up_weight,
            hangtime=hang_time,
            hangboard_weight=hangboard_weight,
            performed_at=self.parent.chosen_date
        ).calc_points_and_grade()

        self.core_label.text = "[color=#404040]Core (Seconds): {0} Points[/color]".format(points['core'])
        self.pull_up_label.text = "[color=#404040]Pull-ups (X kg): {0} Points[/color]".format(points['pull_up'])
        self.hangtime_label.text = "[color=#404040]Hang time (Seconds): {0} Points[/color]".format(points['hang_time'])
        self.hangboard_label.text = "[color=#404040]Hang board (20mm, +X kg): {0} Points[/color]".format(points['hang_board'])
        self.grade_label.text = "[color=#404040]Climbing grade: {0}[/color]".format(grade)
