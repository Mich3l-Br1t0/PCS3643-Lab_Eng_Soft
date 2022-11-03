from tkinter.ttk import LabelFrame
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    anac_code = forms.CharField(max_length=6, label="Código Anac (caso seja piloto)", required=False)

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


class Newflightform(forms.Form):
    estimated_departure = forms.CharField(max_length=100, label="Partida Estimada")
    estimated_arrival = forms.CharField(max_length=100, label="Chegada Estimada")
    pilot = forms.CharField(max_length=100, label="Piloto")
    departure_airport = forms.CharField(max_length=100, label="Aeroporto de partida")
    arrival_airport = forms.CharField(max_length=100, label="Aeroporto de chegada")
