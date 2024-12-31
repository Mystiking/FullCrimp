from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

import numpy as np
import os
from functools import cmp_to_key

from kivy.core.window import Window
from kivy.uix.scatter import Scatter

import cv2

from enum import Enum
from src.Grade import GradeEnum
from src.Route import Route
from src.ProblemCreationState import ProblemCreationState
from src.InteractiveImage import InteractiveImage
from src.ColorPickerLayout import ColorPickerLayout


class GymWallsScreen(Screen):
    gym_image: InteractiveImage

    size_x = 480
    size_y = 800

    setter = lambda _: _

    current_route_being_modified = None
    modify_route_image = None
    date_input_field = None
    setter_input_field = None
    modify_save_button = None
    modify_delete_button = None
    modify_save_press = lambda _: _
    modify_delete_press = lambda _: _

    grade_picker_enabled = False
    current_hold_color = ""
    color_picker = None

    def __init__(self, **kwargs):
        super(GymWallsScreen, self).__init__(**kwargs)

        self.problem_creation_state = ProblemCreationState.NONE

        self.layout = FloatLayout()

        self.modify_layout = self.create_modify_layout()

        scatter = Scatter(scale=1)
        scatter.do_rotation = False
        scatter.auto_bring_to_front = False

        gym_size = cv2.imread('assets/gym/SG_hallen.png').shape
        self.gym_image = InteractiveImage(source='assets/gym/SG_hallen.png',
                                          # size_hint=(1.0, 1.0),
                                          size=(gym_size[0] * 0.75, gym_size[1] * 0.75))
        self.gym_image.scale = 0.75
        self.gym_image.state = self.problem_creation_state
        self.gym_image.image_size = [gym_size[0], gym_size[1]]
        self.gym_image.window_size = [Window.size[0], Window.size[1]]
        self.gym_image.scatterPlane = scatter
        self.gym_image.center_x = self.size_x / 2
        self.gym_image.center_y = self.size_y / 2
        self.gym_image.routes = Route.get_routes_from_db()
        self.gym_image.setter = self.get_setter
        # gym_extents = self.gym_image.get_extents()
        scatter.add_widget(self.gym_image)

        self.layout.add_widget(scatter)

        self.add_button = Button(size_hint=(None, None),
                                 size=(100, 100),
                                 background_normal="assets/misc/Add.png",
                                 background_down="",
                                 pos_hint={'center_x': 0.15, 'center_y': 0.1})
        self.add_button.bind(on_press=self.enter_add_state)

        delete_button = Button(size_hint=(None, None),
                               size=(100, 100),
                               background_normal="assets/misc/Delete.png",
                               background_down="",
                               pos_hint={'center_x': 0.85, 'center_y': 0.1})

        delete_button.bind(on_press=self.enter_delete_state)

        add_route_specs = Button(size_hint=(None, None),
                                 size=(100, 100),
                                 background_normal="assets/misc/Edit.png",
                                 background_down="",
                                 pos_hint={'center_x': 0.50, 'center_y': 0.1})
        add_route_specs.bind(on_press=self.enter_modify_state)

        self.layout.add_widget(self.add_button)
        self.layout.add_widget(add_route_specs)
        self.layout.add_widget(delete_button)

        logout = Button(size_hint=(None, None),
                        size=(50, 50),
                        background_normal="assets/misc/Logout.png",
                        background_down="",
                        pos_hint={'center_x': 0.1, 'center_y': 0.9})
        logout.bind(on_press=self.logout)
        self.layout.add_widget(logout)

        self.current_route_being_added = Button(size_hint=(None, None),
                                                size=(50, 50),
                                                background_normal="assets/grades/4.png",
                                                background_down="",
                                                pos_hint={'center_x': 0.9, 'center_y': 0.9})
        self.current_route_being_added.bind(on_press=self.enable_grade_picker)
        self.route_added_settings = GymWallsScreen.disable_widget(self.current_route_being_added)

        self.layout.add_widget(self.current_route_being_added)

        self.grade_layout = self.create_grade_layout()

        self.grade_picker_button_settings = None
        self.grade_picker_settings = None
        self.grade_picker_enabled = True
        self.disable_grade_picker()

        self.add_widget(self.layout)

        self.gym_image.modify = self.show_modify_widget

    def get_setter(self):
        return self.parent.current_user.name

    def create_grade_layout(self):
        grades = sorted(os.listdir("assets/grades"), key=cmp_to_key(lambda a, b: GradeEnum.grade_comparison(a.split(".")[0], b.split(".")[0])))

        per_row = 4
        grade_layout = GridLayout(cols=per_row, size_hint=(0.75, 0.75), pos_hint={'center_x': 0.5, 'center_y': 0.5}, row_default_height=100, col_default_width=Window.size[1] / (per_row + 2))
        for g in grades:
            b = Button(size_hint=(None, None),
                       size=(50, 50),
                       background_normal="assets/grades/" + g,
                       background_down="")
            b.bind(on_press=lambda t, g=g: self.change_grade(t, GradeEnum.get_route_enum_from_source(g)))
            grade_layout.add_widget(b)

        with grade_layout.canvas.before:
            Color(0.83, 0.85, 0.86, 1)
            grade_layout.rect = Rectangle(size=(Window.size[0] * 0.5, Window.size[1] * 0.85), pos=[(Window.size[0] * 0.5 * 0.75) / 8, 175])

        return grade_layout

    def create_modify_layout(self):
        self.modify_route_image = Button(size_hint=(None, None),
                                         size=(50, 50),
                                         background_normal='assets/grades/7B.png',
                                         background_down="",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.modify_route_image.bind(on_press=self.enable_grade_picker)
        date_layout = BoxLayout(orientation="horizontal", size_hint=(0.75, 0.3))
        date_label = Label(text="Date set:")
        self.date_input_field = TextInput(text="01/01/2025", size_hint=(0.75, 0.45), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        date_layout.add_widget(date_label)
        date_layout.add_widget(self.date_input_field)

        setter_layout = BoxLayout(orientation="horizontal", size_hint=(0.75, 0.3))
        setter_label = Label(text="Setter:")
        self.setter_input_field = TextInput(text="", size_hint=(0.75, 0.45), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        setter_layout.add_widget(setter_label)
        setter_layout.add_widget(self.setter_input_field)

        action_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.3), spacing=50, padding=[110, 100, 0, 0])
        self.modify_save_button = Button(size_hint=(None, None),
                             size=(50, 50),
                             background_normal="assets/misc/Save.png",
                             background_down="")
        modify_cancel_button = Button(size_hint=(None, None),
                               size=(50, 50),
                               background_normal="assets/misc/Cancel.png",
                               background_down="")
        self.modify_delete_button = Button(size_hint=(None, None),
                               size=(50, 50),
                               background_normal="assets/misc/Trashcan.png",
                               background_down="")

        self.modify_save_button.bind(on_press=lambda _: self.close_modify_widget())
        modify_cancel_button.bind(on_press=lambda _: self.close_modify_widget())
        self.modify_delete_button.bind(on_press=lambda _: self.close_modify_widget())

        action_layout.add_widget(self.modify_save_button)
        action_layout.add_widget(modify_cancel_button)
        action_layout.add_widget(self.modify_delete_button)

        self.color_picker = ColorPickerLayout(orientation='horizontal', size_hint=(0.8, 0.25), padding=[0, 20, 0, 0], pos_hint={'center_x': 0.5, 'center_y': 0.5})

        modify_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        modify_layout.add_widget(self.modify_route_image)
        modify_layout.add_widget(self.color_picker)
        modify_layout.add_widget(date_layout)
        modify_layout.add_widget(setter_layout)
        modify_layout.add_widget(action_layout)

        with modify_layout.canvas.before:
            Color(0.83, 0.85, 0.86, 1)
            modify_layout.rect = Rectangle(size=(Window.size[0] * 0.5, Window.size[1] * 0.8), pos=[(Window.size[0] * 0.5 * 0.75) / 8, 150])

        return modify_layout

    def disable_grade_picker(self):
        if self.grade_picker_enabled:
            self.layout.remove_widget(self.grade_layout)
            self.grade_picker_enabled = False
        if self.gym_image.state == ProblemCreationState.MODIFY:
            self.show_modify_widget(self.current_route_being_modified)

    def enable_grade_picker(self, touch):
        if not self.grade_picker_enabled:
            self.layout.add_widget(self.grade_layout)
            self.grade_picker_enabled = True
        elif self.grade_picker_enabled and self.gym_image.state == ProblemCreationState.ADD:
            self.disable_grade_picker()

        if self.gym_image.state == ProblemCreationState.MODIFY:
            self.close_modify_widget()

    def change_grade(self, touch, grade: GradeEnum):
        # Get these from a database later on
        if self.gym_image.state == ProblemCreationState.ADD:
            self.gym_image.grade_enum = grade
            self.update_current_grade()
        if self.gym_image.state == ProblemCreationState.MODIFY:
            self.modify_route_image.background_normal = "assets/grades/" + grade.value + ".png"
            self.current_route_being_modified.grade = grade

        self.disable_grade_picker()

    def enter_add_state(self, touch):
        if self.gym_image.state == ProblemCreationState.ADD:
            self.exit_add_state()
            return

        if self.gym_image.state == ProblemCreationState.DELETE:
            self.exit_delete_state(None)

        if self.gym_image.state == ProblemCreationState.MODIFY:
            self.exit_modify_state()

        GymWallsScreen.restore_widget(self.current_route_being_added, self.route_added_settings)
        self.gym_image.state = ProblemCreationState.ADD
        self.update_current_grade()
        self.current_route_being_added.unbind(on_press=self.exit_modify_state)
        self.current_route_being_added.unbind(on_press=self.exit_delete_state)
        self.current_route_being_added.bind(on_press=self.enable_grade_picker)

    def exit_add_state(self):
        self.disable_grade_picker()
        self.route_added_settings = GymWallsScreen.disable_widget(self.current_route_being_added)
        self.gym_image.state = ProblemCreationState.NONE
        self.current_route_being_added.unbind(on_press=self.enable_grade_picker)

    def update_current_grade(self):
        self.current_route_being_added.background_normal = "assets/grades/" + self.gym_image.grade_enum.value + ".png"

    def enter_delete_state(self, touch):
        if self.gym_image.state == ProblemCreationState.DELETE:
            self.exit_delete_state(None)
            return

        if self.gym_image.state == ProblemCreationState.ADD:
            self.exit_add_state()

        if self.gym_image.state == ProblemCreationState.MODIFY:
            self.exit_modify_state(None)

        self.gym_image.state = ProblemCreationState.DELETE
        GymWallsScreen.restore_widget(self.current_route_being_added, self.route_added_settings)

        self.current_route_being_added.unbind(on_press=self.exit_modify_state)
        self.current_route_being_added.unbind(on_press=self.enable_grade_picker)
        self.current_route_being_added.bind(on_press=self.exit_delete_state)
        self.current_route_being_added.background_normal = "assets/misc/Exit.png"

    def exit_delete_state(self, touch):
        self.route_added_settings = GymWallsScreen.disable_widget(self.current_route_being_added)
        self.gym_image.state = ProblemCreationState.NONE
        self.current_route_being_added.unbind(on_press=self.exit_delete_state)

    def enter_modify_state(self, touch):
        if self.gym_image.state == ProblemCreationState.ADD:
            self.exit_modify_state(touch)
            return

        if self.gym_image.state == ProblemCreationState.ADD:
            self.exit_add_state()
            self.disable_grade_picker()

        if self.gym_image.state == ProblemCreationState.DELETE:
            self.exit_delete_state(touch)

        self.gym_image.state = ProblemCreationState.MODIFY
        GymWallsScreen.restore_widget(self.current_route_being_added, self.route_added_settings)

        self.current_route_being_added.unbind(on_press=self.exit_delete_state)
        self.current_route_being_added.unbind(on_press=self.enable_grade_picker)
        self.current_route_being_added.bind(on_press=self.exit_modify_state)
        self.current_route_being_added.background_normal = "assets/misc/Exit.png"

    def close_modify_widget(self):
        self.layout.remove_widget(self.modify_layout)
        try:
            self.modify_save_button.unbind(on_press=self.modify_save_press)
            self.modify_delete_button.unbind(on_press=self.modify_delete_press)
        except:
            pass

    def modify_delete(self, route):
        self.gym_image.source = self.gym_image.original_source
        self.gym_image.newImageCreated = False
        self.gym_image.routes.remove(route)
        route.delete_from_db()
        self.gym_image.add_routes_to_image()

    def modify(self, route):
        route_index = self.gym_image.routes.index(route)
        self.gym_image.routes[route_index].modify_db(self.date_input_field.text, self.setter_input_field.text, GymWallsScreen.grade_enum_from_path(self.modify_route_image.background_normal), self.color_picker.get_current_color())
        self.gym_image.add_routes_to_image()

    def show_modify_widget(self, route):
        self.current_route_being_modified = route
        self.modify_route_image.background_normal = "assets/grades/" + route.grade.value + ".png"
        self.date_input_field.text = route.date_set
        self.setter_input_field.text = route.setter
        self.color_picker.set_color_raw(route.hold_color)

        self.modify_save_press = lambda _: self.modify(route)
        self.modify_delete_press = lambda _: self.modify_delete(route)

        self.modify_save_button.unbind(on_press=self.update)
        self.modify_delete_button.unbind(on_press=self.update)

        self.modify_save_button.bind(on_press=self.modify_save_press)
        self.modify_save_button.bind(on_press=self.update)

        self.modify_delete_button.bind(on_press=self.modify_delete_press)
        self.modify_delete_button.bind(on_press=self.update)

        self.layout.add_widget(self.modify_layout)

    def exit_modify_state(self, touch):
        self.close_modify_widget()
        self.route_added_settings = GymWallsScreen.disable_widget(self.current_route_being_added)
        self.gym_image.state = ProblemCreationState.NONE
        self.current_route_being_added.unbind(on_press=self.exit_modify_state)

    def update(self, touch):
        self.gym_image.add_routes_to_image()

    def logout(self, touch):
        self.manager.transition.direction = "right"
        self.manager.current = "MainMenu"

    @staticmethod
    def grade_enum_from_path(path):
        filename = path if "/" not in path else path.split("/")[-1]
        return GradeEnum.get_route_enum_from_source(filename)

    @staticmethod
    def disable_widget(widget):
        settings = (widget.height, widget.size_hint_y, widget.opacity, widget.disabled)
        widget.height, widget.size_hint_y, widget.opacity, widget.disabled = 0, None, 0, True
        return settings

    @staticmethod
    def restore_widget(widget, settings):
        widget.height, widget.size_hint_y, widget.opacity, widget.disabled = settings