from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('trainers/', views.trainers, name='trainers'),
    path('contact/', views.contact, name='contact'),
]
