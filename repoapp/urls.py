from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
