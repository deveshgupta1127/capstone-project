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

if __name__ == "__main__":
    HealthApp().run()
