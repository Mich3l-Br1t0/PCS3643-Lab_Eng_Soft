from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

PROFESSION_CHOICES = [
    ("manager", "Gerente de Operações"),
    ("control", "Torre de Controle"),
    ("pilot", "Piloto"),
    ("worker", "Funcionário da Companhia Aérea"),
    ("operator", "Operador de voo"),
]


class NameForm(forms.Form):
    your_name = forms.CharField(label="Nome", max_length=100)
    your_nickname = forms.CharField(label="Sobrenome", max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label="Senha", widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        label="Confirmar Senha", widget=forms.PasswordInput()
    )
    profession = forms.CharField(
        label="Profissão", widget=forms.Select(choices=PROFESSION_CHOICES)
    )
