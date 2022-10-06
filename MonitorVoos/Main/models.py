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
        db_table = 'status'

class Pilot(models.Model):
    pass


class User(models.Model):
    name = models.CharField()
    document = models.PositiveIntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'Users'


class Airport(models.Model):
    pass

class Flight(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=SET_NULL, blank=True, null=True, related_name='pilots')
    origin_airport = models.ForeignKey(Airport, on_delete=CASCADE, related_name='origin_airports')
    destination_airport = models.ForeignKey(Airport, on_delete=CASCADE, related_name='destination_airports')
    status = models.ForeignKey(FlightStatus, on_delete=SET_NULL, related_name='status')
    estimated_departure = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    real_departure = models.DateTimeField(blank=True, null=True)
    real_arrival = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'flights'