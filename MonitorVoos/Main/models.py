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
