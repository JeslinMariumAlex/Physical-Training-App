from django.contrib import admin
from .models import Workout, Trainer, Appointment

# Register your models here.

admin.site.register(Workout)
admin.site.register(Trainer)
admin.site.register(Appointment)

