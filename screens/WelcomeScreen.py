from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(padding=50, orientation='vertical')
        label = Label(text="[color=#404040][font=assets/fonts/vonique/Vonique64.ttf]Fu llC r i m p[/font][/color]", size_hint=(1, .5),
                      markup=True, font_size=26)

        logo = Image(source='assets/logo/logo_eliptic.png',
                     size_hint=(1.0, 1.0),
                     pos_hint={'center_x': .5, "center_y": .5})

        layout.add_widget(logo)
        layout.add_widget(label)

        self.personal_label = Label(text="[color=#404040]Welcome[/color]",
                                    size_hint=(1, .5),
                                    markup=True,
                                    font_size=20)
        layout.add_widget(self.personal_label)

        add_session_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, .65))
        add_session_button = Button(text="Add New Session",
                                    background_color=[0.24, 0.44, 0.40, 1.0])
        add_session_button.bind(on_release=self.add_new_sessions_transition)
        add_session_layout.add_widget(add_session_button)

        add_weight_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, .65))
        add_weight_button = Button(text="Add new weight",
                                   background_color=[0.24, 0.44, 0.40, 1.0])
        add_weight_button.bind(on_release=self.add_new_weight_transition)
        add_weight_layout.add_widget(add_weight_button)

        data_and_logout_layout = BoxLayout(orientation='vertical', size_hint=(1.0, .65))
        data_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, .65))
        data_button = Button(text="View data",
                             background_color=[0.8, 0.8, 0.8, 1.0])
        data_button.bind(on_release=self.view_data)
        data_layout.add_widget(data_button)

        logout_layout = BoxLayout(padding=5, orientation='vertical', size_hint=(1.0, .65))
        logout_button = Button(text="Logout",
                               background_color=[0.8, 0.1, 0.1, 1.0])
        logout_button.bind(on_release=self.logout)
        logout_layout.add_widget(logout_button)

        data_and_logout_layout.add_widget(data_layout)
        data_and_logout_layout.add_widget(logout_layout)

        layout.add_widget(add_session_layout)
        layout.add_widget(add_weight_layout)
        layout.add_widget(data_and_logout_layout)
        self.add_widget(layout)

    def add_new_sessions_transition(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "training_session"

    def add_new_weight_transition(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "weight"

    def logout(self, *args):
        self.manager.current = "login"
        self.manager.transition.direction = "right"

    def on_pre_enter(self, *args):
        self.personal_label.text = "[color=#404040]Welcome, {0}![/color]".format(self.parent.current_user.name)

    def view_data(self, *args):
        print("Not implemented yet.")
