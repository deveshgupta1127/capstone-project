from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from db import find_user, add_user, validate_user

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=2, padding=10, spacing=10)

        layout.add_widget(Label(text='Email'))
        self.email_input = TextInput(multiline=False)
        layout.add_widget(self.email_input)

        layout.add_widget(Label(text='Password'))
        self.password_input = TextInput(multiline=False, password=True)
        layout.add_widget(self.password_input)

        self.message_label = Label(text="")
        layout.add_widget(self.message_label)

        self.login_button = Button(text='Login / Register')
        self.login_button.bind(on_press=self.handle_login)
        layout.add_widget(self.login_button)

        self.add_widget(layout)

    def handle_login(self, instance):
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        if not email or not password:
            self.message_label.text = "Please enter email and password"
            return

        user = find_user(email)
        if user:
            if validate_user(email, password):
                self.manager.current = 'health'
                self.manager.get_screen('health').user_email = email
            else:
                self.message_label.text = "Wrong password!"
        else:
            add_user(email, password)
            self.manager.current = 'health'
            self.manager.get_screen('health').user_email = email
