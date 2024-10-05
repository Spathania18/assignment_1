from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classify', views.classify_text, name='classify_text'),
    path('generate', views.generate_text, name='generate_text'),
]