from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login_screen import LoginScreen
from health_form import HealthForm

class HealthApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HealthForm(name='health'))
        return sm

<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
    HealthApp().run()
