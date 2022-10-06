from django.db import models


# Create your models here.
class Flight(models.Model):
    pass


# TODO: confirmar necessidade de classes de relatorio
class SpecificFlightReport(models.Model):
    pass


# TODO: confirmar necessidade de classes de relatorio
class StatusReport(models.Model):
    pass


class Pilot(models.Model):
    pass


class Plane(models.Model):
    pass


class User(models.Model):
    name = models.CharField()
    document = models.PositiveIntegerField()
    email = models.EmailField()


class Airport(models.Model):
    pass


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
