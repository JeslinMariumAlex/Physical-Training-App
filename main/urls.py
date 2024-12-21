from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('trainers/', views.trainers, name='trainers'),
    path('workouts/', views.workouts, name='workouts'),
    path('contact/', views.contact, name='contact'),
]
