from django.urls import path
from . import views # from this same directory import views

# URLConfig
urlpatterns = [
    path('hello/', views.say_hello) 
]
