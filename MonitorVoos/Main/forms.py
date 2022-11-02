from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registerform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class Newflightform(forms.Form):
    estimated_departure = forms.CharField(max_length=100, label="Partida Estimada")
    estimated_arrival = forms.CharField(max_length=100, label="Chegada Estimada")
    pilot = forms.CharField(max_length=100, label="Piloto")
    departure_airport = forms.CharField(max_length=100, label="Aeroporto de partida")
    arrival_airport = forms.CharField(max_length=100, label="Aeroporto de chegada")
