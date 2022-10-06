from django.db import models
from django.db.models import SET_NULL, CASCADE


class FlightStatus(models.IntegerChoices):
    REGISTERED = 1, "Cadastrado"
    BOARDING = 2, "Embarcando"
    PROGRAMMED = 3, "Programado"
    TAXIING = 4, "Taxiando"
    READY = 5, "Pronto"
    AUTHORIZED = 6, "Autorizado"
    ON_AIR = 7, "Em voo"
    LANDED = 8, "Aterrissado"
    CANCELLED = 9, "Cancelado"

    class Meta:
        db_table = "status"


class Pilot(models.Model):
    name = models.CharField(max_lenght=256)
    anac_code = models.PositiveIntegerField(max_length=6)
    cpf = models.PositiveIntegerField(max_length=11)

    class Meta:
        db_table = "pilots"


class User(models.Model):
    name = models.CharField(max_lenght=256)
    cpf = models.PositiveIntegerField(max_lenght=11)
    email = models.EmailField()
    password = models.CharField()

    class Meta:
        db_table = "users"


class Airport(models.Model):
    icao = models.CharField(max_lenght=4)
    name = models.CharField(max_lenght=256)
    city = models.CharField(max_lenght=256)
    state = models.CharField(max_lenght=256)
    country = models.CharField(max_lenght=256)

    class Meta:
        db_table = "airports"
