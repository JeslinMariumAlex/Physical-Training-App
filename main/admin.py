from django.contrib import admin
from .models import Workout, Trainer, Appointment

# Register your models here.

admin.site.register(Workout)
admin.site.register(Trainer)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','person_name', 'person_phone', 'person_email', 'trainer_name', 'appointment_date', 'appointment_time','booked_date')

admin.site.register(Appointment, AppointmentAdmin)

