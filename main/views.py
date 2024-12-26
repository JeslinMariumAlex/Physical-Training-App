from django.shortcuts import render
from .models import Workout, Trainer
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = AppointmentForm()
    dict_form = {
        'form': form
    }
    return render(request, 'appointment.html', dict_form)

@login_required
def trainers(request):
    dict_trainers = {
        'trainers': Trainer.objects.all()
    }
    return render(request, 'trainers.html', dict_trainers)

@login_required
def workouts(request):
    dict_workouts = {
        'workouts': Workout.objects.all()
    }
    return render(request, 'workouts.html', dict_workouts)

@login_required
def contact(request):
    return render(request, 'contact.html')

