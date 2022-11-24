from tkinter.ttk import LabelFrame
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Airline, Flight, Airport

PROFESSION_CHOICES = [
    ("Manager", "Gerente de Operações"),
    ("Control", "Torre de Controle"),
    ("Pilot", "Piloto"),
    ("Worker", "Funcionário da Companhia Aérea"),
    ("Operator", "Operador de voo"),
]

STATUS_CHOICES = [
    ("Cadastrado", "Cadastrado"),
    ("Em voo", "Em voo"),
    ("Aguardando Embarque", "Aguardado Embarque"),
    ("Aguardando Desembarque", "Aguardando Desembarque"),
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
            "destination_airport",
            "airline",
            "status",
        ]
        labels = {
            "estimated_departure": "Partida Estimada (AAAA-MM-DD hh:mm)",
            "estimated_arrival": "Chegada Estimada (AAAA-MM-DD hh:mm)",
            "pilot": "Piloto",
            "origin_airport": "Aeroporto de partida",
            "destination_airport": "Aeroporto de chegada",
            "airline": "Companhia Aérea",
        }


class Editflightform(ModelForm):

    status = forms.CharField(
        label="Status", widget=forms.Select(choices=STATUS_CHOICES)
    )

    class Meta:
        model = Flight
        fields = [
            "estimated_departure",
            "estimated_arrival",
            "pilot",
            "destination_airport",
            "airline",
            "status",
            "real_departure",
            "real_arrival",
        ]
        labels = {
            "estimated_departure": "Partida Estimada (AAAA-MM-DD hh:mm)",
            "estimated_arrival": "Chegada Estimada (AAAA-MM-DD hh:mm)",
            "pilot": "Piloto",
            "origin_airport": "Aeroporto de partida",
            "destination_airport": "Aeroporto de chegada",
            "airline": "Companhia Aérea",
            "real_departure": "Partida real",
            "real_arrival": "Chegada real",
        }

    def clean(self):
        cleaned_data = super().clean()
        origin_airport = cleaned_data.get("origin_airport")
        destination_airport = cleaned_data.get("destination_airport")
        if origin_airport == destination_airport:
            raise ValidationError(
                "Aeroporto de destino não pode ser igual o de partida"
            )
        estimated_departure = cleaned_data.get("estimated_departure")
        estimated_arrival = cleaned_data.get("estimated_arrival")
        if not estimated_arrival:
            return cleaned_data
        if not estimated_departure:
            return cleaned_data
        if estimated_departure > estimated_arrival:
            raise ValidationError("Partida estimada não pode ser maior que chegada")
        return cleaned_data


class Newairlineform(ModelForm):
    name = forms.CharField(max_length=100, label="Nome da Companhia aérea")
    flight_identifier = forms.CharField(
        max_length=3, label="Identificador da Companhia aérea"
    )

    class Meta:
        model = Airline
        fields = ("name", "flight_identifier")


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = "__all__"
        labels = {
            "icao": "Código ICAO",
            "name": "Nome",
            "city": "Cidade",
            "state": "Estado",
            "country": "País",
        }


class ReportForm(forms.Form):
    start_date = forms.DateField(label="Data início", widget=forms.SelectDateWidget())
    end_date = forms.DateField(label="Data fim", widget=forms.SelectDateWidget())
    Airline = forms.ModelChoiceField(
        queryset=Airline.objects.all(), required=False, label="Companhia Aérea"
    )
    # Todos os voos do sistema num período
    # Todos os voos de uma companhia aérea num período + detalhes

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date >= end_date:
            raise ValidationError(
                "Data de início não pode ser maior ou igual data de fim"
            )
        return cleaned_data
