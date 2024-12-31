from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
import os


class ColorPickerLayout(BoxLayout):
    selected_color = ""
    color = (0.93, 0.95, 0.96, 1)

    def __init__(self, **kwargs):
        super(ColorPickerLayout, self).__init__(**kwargs)

        colors = os.listdir('assets/gym/hold_colors')
        self.layout = BoxLayout(orientation="vertical", size_hint=(0.8, 1))
        self.button_layout = BoxLayout(orientation="horizontal", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        for c in colors:
            color_path = 'assets/gym/hold_colors/' + c
            b = Button(size_hint=(None, None),
                       size=(25, 25),
                       background_normal=color_path,
                       background_down="")

            b.bind(on_press=lambda t, c=color_path: self.set_color(c))
            self.button_layout.add_widget(b)

        self.selected_color_layout = BoxLayout(orientation="horizontal", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.selected_color_image = Image(source=self.selected_color,
                                          size=(25, 25),
                                          size_hint=(None, None),
                                          pos_hint={'center_x': 0.0, 'center_y': 0.5})
        selected_color_label = Label(text="Hold color:", size_hint=(0.5, 1))
        self.selected_color_layout.add_widget(selected_color_label)
        self.selected_color_layout.add_widget(self.selected_color_image)

        self.layout.add_widget(self.selected_color_layout)
        self.layout.add_widget(self.button_layout)

        self.add_widget(self.layout)

    def set_color(self, c):
        self.selected_color = c
        self.update()

    def get_current_color(self):
        return self.selected_color.split("/")[-1].split(".")[0]

    def set_color_raw(self, c):
        self.selected_color = 'assets/gym/hold_colors/' + c + '.png'
        self.update()

    def update(self):
        self.selected_color_image.source = self.selected_color
        self.selected_color_image.reload()