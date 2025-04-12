from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from db import save_health_data

class HealthForm(Screen):
    def __init__(self, **kwargs):
        super(HealthForm, self).__init__(**kwargs)
        self.user_email = None
        self.layout = GridLayout(cols=2, spacing=10, padding=10)
        self.inputs = {}

        self.fields = [
            'Gender(Male,Female)', 'Age', 'Education(postgraduate,primaryschool,uneducated,graduate)',
            'Current Smoker(0,1)', 'Cigarettes Per Day', 'BP Meds', 'Prevalent Stroke',
            'Prevalent Hyp', 'Diabetes', 'Total Cholesterol', 'Systolic BP',
            'Diastolic BP', 'BMI', 'Heart Rate', 'Glucose'
        ]

        for field in self.fields:
            self.layout.add_widget(Label(text=field))
            self.inputs[field] = TextInput(multiline=False)
            self.layout.add_widget(self.inputs[field])

        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.on_submit)
        self.layout.add_widget(self.submit_button)

        self.result_label = Label(text="Result will be shown here")
        self.layout.add_widget(self.result_label)

        self.add_widget(self.layout)

    def on_submit(self, instance):
        try:
            age = int(self.inputs['Age'].text)
            bpm = int(self.inputs['Heart Rate'].text)
            bmi = float(self.inputs['BMI'].text)
            if age > 50 or bmi > 30 or bpm > 100:
                result = "High Risk"
            else:
                result = "Low Risk"
        except Exception as e:
            result = "Invalid input"

        self.result_label.text = f"Result: {result}"

        # Save to MongoDB
        data = {field: self.inputs[field].text for field in self.fields}
        data['risk'] = result
        if self.user_email:
            save_health_data(self.user_email, data)
