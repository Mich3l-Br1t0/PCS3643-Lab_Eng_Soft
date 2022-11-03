from tkinter.ttk import LabelFrame
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Flight

PROFESSION_CHOICES = [
    ("manager", "Gerente de Operações"),
    ("control", "Torre de Controle"),
    ("pilot", "Piloto"),
    ("worker", "Funcionário da Companhia Aérea"),
    ("operator", "Operador de voo"),
]


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="Nome")
    last_name = forms.CharField(max_length=100, label="Sobrenome")
    cpf = forms.CharField(max_length=11, label="CPF")
    email = forms.EmailField()
    profession = forms.CharField(
        label="Profissão", widget=forms.Select(choices=PROFESSION_CHOICES)
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "cpf",
            "email",
            "profession",
            "password1",
            "password2",
        ]


class Newflightform(forms.Form):
    estimated_departure = forms.DateField(label="Partida Estimada")
    estimated_arrival = forms.CharField(max_length=100, label="Chegada Estimada")
    pilot = forms.IntegerField(label="Piloto")
    departure_airport = forms.IntegerField(label="Aeroporto de partida")
    arrival_airport = forms.IntegerField(label="Aeroporto de chegada")
    airline = forms.IntegerField(label="Companhia aérea")
    status = forms.CharField(label="Status")

    class Meta:
        model = Flight
        fields = [
            "estimated_departure",
            "estimated_arrival",
            "pilot",
            "departure_airport",
            "arrival_airport",
            "airline",
            "status",
        ]
