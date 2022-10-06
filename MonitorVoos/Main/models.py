from email.policy import default
from django.db import models
from django.db.models import SET_NULL, CASCADE


class Pilot(models.Model):
    name = models.CharField(max_length=256)
    anac_code = models.CharField(max_length=6)
    cpf = models.CharField(max_length=11)

    class Meta:
        db_table = "pilots"


class User(models.Model):
    name = models.CharField(max_length=256)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    password = models.CharField(max_length=256)

    class Meta:
        db_table = "users"


class Airport(models.Model):
    icao = models.CharField(max_length=4)
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)

    class Meta:
        db_table = "airports"


class Flight(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=SET_NULL, blank=True, null=True, related_name='pilots')
    origin_airport = models.ForeignKey(Airport, on_delete=CASCADE, related_name='origin_airports')
    destination_airport = models.ForeignKey(Airport, on_delete=CASCADE, related_name='destination_airports')
    status = models.CharField(default='Cadastrado', max_length=256)
    estimated_departure = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    real_departure = models.DateTimeField(blank=True, null=True)
    real_arrival = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'flights'
