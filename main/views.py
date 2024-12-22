from django.shortcuts import render
from .models import Workout, Trainer
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def appointment(request):
    return render(request, 'appointment.html')

def trainers(request):
    dict_trainers = {
        'trainers': Trainer.objects.all()
    }
    return render(request, 'trainers.html', dict_trainers)

def workouts(request):
    dict_workouts = {
        'workouts': Workout.objects.all()
    }
    return render(request, 'workouts.html', dict_workouts)

def contact(request):
    return render(request, 'contact.html')

