from tkinter.ttk import LabelFrame
from django import forms
from django.forms import ModelForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Airline, Flight

PROFESSION_CHOICES = [
    ("Manager", "Gerente de Operações"),
    ("Control", "Torre de Controle"),
    ("Pilot", "Piloto"),
    ("Worker", "Funcionário da Companhia Aérea"),
    ("Operator", "Operador de voo"),
]


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="Nome")
    last_name = forms.CharField(max_length=100, label="Sobrenome")
    cpf = forms.CharField(max_length=11, label="CPF")
    email = forms.EmailField()
    profession = forms.CharField(
        label="Profissão", widget=forms.Select(choices=PROFESSION_CHOICES)
    )
    anac_code = forms.CharField(
        max_length=6, label="Código Anac (caso seja piloto)", required=False
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
            "anac_code",
            "password1",
            "password2",
        ]


class Newflightform(ModelForm):
    estimated_departure = forms.DateField(label="Partida Estimada")
    estimated_arrival = forms.DateField(label="Chegada Estimada")
    pilot_id = forms.IntegerField(label="Piloto")
    departure_airport = forms.IntegerField(label="Aeroporto de partida")
    arrival_airport = forms.IntegerField(label="Aeroporto de chegada")
    airline_id = forms.IntegerField(label="Companhia aérea")
    status = forms.CharField(label="Status")

    class Meta:
        model = Flight
        fields = (
            "estimated_departure",
            "estimated_arrival",
            "pilot_id",
            "departure_airport",
            "arrival_airport",
            "airline_id",
            "status",
        )


class Newairlineform(ModelForm):
    name = forms.CharField(max_length=100, label="Nome da Companhia aérea")
    flight_identifier = forms.CharField(
        max_length=3, label="Identificador da Companhia aérea"
    )

    class Meta:
        model = Airline
        fields = ("name", "flight_identifier")
