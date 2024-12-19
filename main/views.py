from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Home page')

def about(request):
    return HttpResponse('About page')

def appointment(request):
    return HttpResponse('Appointment page')

def trainers(request):
    return HttpResponse('trainers page')

def contact(request):
    return HttpResponse('contact page')

