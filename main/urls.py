from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('trainers/', views.trainers, name='trainers'),
    path('contact/', views.contact, name='contact'),
]
