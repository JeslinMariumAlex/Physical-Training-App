from django import forms

from .models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['booked_date']

        widgets = {
            'appointment_date': DateInput(),
            'appointment_time': TimeInput()
        }

        labels = {
            'person_name': 'Full Name',
            'person_phone': 'Phone Number',
            'person_email': 'Email Address',
            'trainer_name': 'Trainer',
            'appointment_date': 'Date',
            'appointment_time': 'Time'
        }