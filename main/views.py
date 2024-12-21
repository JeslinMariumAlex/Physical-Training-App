from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def appointment(request):
    return render(request, 'appointment.html')

def trainers(request):
    return render(request, 'trainers.html')

def workouts(request):
    return render(request, 'workouts.html')

def contact(request):
    return render(request, 'contact.html')

