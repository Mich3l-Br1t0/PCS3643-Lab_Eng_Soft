from tkinter.ttk import LabelFrame
from django import forms
from django.forms import ModelForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Airline, Flight

PROFESSION_CHOICES = [
    ("Manager", "Gerente de Operações"),
    ("Control", "Torre de Controle"),
    ("Pilot", "Piloto"),
    ("Worker", "Funcionário da Companhia Aérea"),
    ("Operator", "Operador de voo"),
]

STATUS_CHOICES = [
    ("Cadastrado", "Cadastrado"),
    ("Em_voo", "Em voo"),
    ("Aguardando_Embarque", "Aguardado Embarque"),
    ("Aguardando_Desembarque", "Aguardando Desembarque"),
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

    status = forms.CharField(
        label="Status", widget=forms.Select(choices=STATUS_CHOICES)
    )

    class Meta:
        model = Flight
        fields = [
            "estimated_departure",
            "estimated_arrival",
            "pilot",
            "origin_airport",
            "destination_airport",
            "airline",
            "status",
        ]
        labels = {
            "estimated_departure": "Partida Estimada",
            "estimated_arrival": "Chegada Estimada",
            "pilot": "Piloto",
            "origin_airport": "Aeroporto de partida",
            "destination_airport": "Aeroporto de chegada",
            "airline": "Companhia Aérea",
        }


class Newairlineform(ModelForm):
    name = forms.CharField(max_length=100, label="Nome da Companhia aérea")
    flight_identifier = forms.CharField(
        max_length=3, label="Identificador da Companhia aérea"
    )

    class Meta:
        model = Airline
        fields = ("name", "flight_identifier")
