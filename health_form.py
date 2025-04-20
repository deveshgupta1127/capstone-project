<<<<<<< HEAD
=======
import pickle
import numpy as np
>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from db import save_health_data

<<<<<<< HEAD
=======

>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
class HealthForm(Screen):
    def __init__(self, **kwargs):
        super(HealthForm, self).__init__(**kwargs)
        self.user_email = None
        self.layout = GridLayout(cols=2, spacing=10, padding=10)
        self.inputs = {}

        self.fields = [
<<<<<<< HEAD
            'Gender(Male,Female)', 'Age', 'Education(postgraduate,primaryschool,uneducated,graduate)',
            'Current Smoker(0,1)', 'Cigarettes Per Day', 'BP Meds', 'Prevalent Stroke',
            'Prevalent Hyp', 'Diabetes', 'Total Cholesterol', 'Systolic BP',
            'Diastolic BP', 'BMI', 'Heart Rate', 'Glucose'
        ]

=======
            'Gender (Male/Female)', 'Age', 'Education (Postgraduate/PrimarySchool/Uneducated/Graduate)',
            'Current Smoker (0/1)', 'Cigarettes Per Day', 'BP Meds (0/1)', 'Prevalent Stroke (0/1)',
            'Prevalent Hyp (0/1)', 'Diabetes (0/1)', 'Total Cholesterol', 'Systolic BP',
            'Diastolic BP', 'BMI', 'Heart Rate', 'Glucose'
        ]

        # Create input fields
>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
        for field in self.fields:
            self.layout.add_widget(Label(text=field))
            self.inputs[field] = TextInput(multiline=False)
            self.layout.add_widget(self.inputs[field])

<<<<<<< HEAD
=======
        # Submit button
>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.on_submit)
        self.layout.add_widget(self.submit_button)

<<<<<<< HEAD
=======
        # Prediction result label
>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
        self.result_label = Label(text="Result will be shown here")
        self.layout.add_widget(self.result_label)

        self.add_widget(self.layout)

<<<<<<< HEAD
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
=======
        # Load the trained model
        try:
            with open('random_forest_model.pkl', 'rb') as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            self.result_label.text = "Error: Model file not found!"

    def to_int(self, value):
        """Helper to convert binary-like inputs"""
        value = value.strip().lower()
        if value in ['yes', '1', 'true']:
            return 1
        elif value in ['no', '0', 'false', '']:
            return 0
        else:
            raise ValueError(f"Expected yes/no or 1/0 but got '{value}'")

    def preprocess_input(self):
        """Convert form inputs to the numeric format expected by the model"""
        try:
            gender_input = self.inputs['Gender (Male/Female)'].text.strip().lower()
            gender = 1 if gender_input == 'male' else 0

            age = int(self.inputs['Age'].text.strip())

            edu_input = self.inputs['Education (Postgraduate/PrimarySchool/Uneducated/Graduate)'].text.strip().lower()
            education_map = {
                'postgraduate': 4,
                'graduate': 3,
                'primaryschool': 2,
                'uneducated': 1
            }
            education = education_map.get(edu_input)
            if education is None:
                raise ValueError("Invalid education input")

            smoker = self.to_int(self.inputs['Current Smoker (0/1)'].text)
            cigs_per_day = float(self.inputs['Cigarettes Per Day'].text)
            bp_meds = self.to_int(self.inputs['BP Meds (0/1)'].text)
            stroke = self.to_int(self.inputs['Prevalent Stroke (0/1)'].text)
            hyp = self.to_int(self.inputs['Prevalent Hyp (0/1)'].text)
            diabetes = self.to_int(self.inputs['Diabetes (0/1)'].text)
            chol = float(self.inputs['Total Cholesterol'].text)
            sys_bp = float(self.inputs['Systolic BP'].text)
            dia_bp = float(self.inputs['Diastolic BP'].text)
            bmi = float(self.inputs['BMI'].text)
            heart_rate = float(self.inputs['Heart Rate'].text)
            glucose = float(self.inputs['Glucose'].text)

            # Feature vector expected by model
            features = [
                gender, age, education, smoker, cigs_per_day,
                bp_meds, stroke, hyp, diabetes, chol,
                sys_bp, dia_bp, bmi, heart_rate, glucose
            ]

            return np.array([features])
        except Exception as e:
            raise ValueError(f"Input Error: {e}")

    def on_submit(self, instance):
        """Handles submission, model prediction, and storing to DB"""
        try:
            features = self.preprocess_input()
            prediction = self.model.predict(features)[0]

            risk = "High Risk" if prediction >= 0.5 else "Low Risk"
            self.result_label.text = f"Prediction: {risk} (Score: {prediction:.2f})"

            # Save inputs + result to database
            data = {field: self.inputs[field].text for field in self.fields}
            data['risk'] = risk
            if self.user_email:
                save_health_data(self.user_email, data)

        except ValueError as ve:
            self.result_label.text = f"Invalid input: {ve}"
        except Exception as e:
            self.result_label.text = f"Unexpected error: {e}"
>>>>>>> 586fa6ad2e53dd92bb456fa21097f796060179a0
