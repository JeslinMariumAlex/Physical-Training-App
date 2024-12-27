from django import forms
from datetime import datetime, timedelta
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

    def clean(self):
        cleaned_data = super().clean()
        appointment_date = cleaned_data.get('appointment_date')
        appointment_time = cleaned_data.get('appointment_time')
        trainer_name = cleaned_data.get('trainer_name')


        if appointment_date and appointment_time and trainer_name:
            # Combine date and time to get a full datetime
            appointment_datetime = datetime.combine(appointment_date, appointment_time)

            # Define the margin for checking (30 minutes before and after the proposed time)
            time_margin = timedelta(minutes=30)

            # Check for any appointment that overlaps with the proposed time (within +/- 30 minutes)
            overlapping_appointments = Appointment.objects.filter(
                appointment_date=appointment_date,
                trainer_name=trainer_name,  # Check only for the same trainer
                appointment_time__range=(
                    (appointment_datetime - time_margin).time(),
                    (appointment_datetime + time_margin).time()
                )
            )

            # If there's an overlapping appointment, raise a validation error
            if overlapping_appointments.exists():
                raise forms.ValidationError("This time slot is already booked or overlaps with another appointment.")

        return cleaned_data