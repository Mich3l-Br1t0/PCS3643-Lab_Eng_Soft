from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Pilot(models.Model):
    name = models.CharField(max_length=256)
    anac_code = models.CharField(
        max_length=6,
    )
    cpf = models.CharField(max_length=11)

    class Meta:
        db_table = "pilots"
        constraints = [
            models.UniqueConstraint(
                fields=["anac_code", "cpf"], name="unique anac code"
            )
        ]

    def __str__(self):
        return self.name + " - " + self.anac_code


class User_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    profession = models.CharField(max_length=100)

    class Meta:
        db_table = "users_data"
        constraints = [models.UniqueConstraint(
            fields=["cpf"], name="unique document")]


class Airport(models.Model):
    icao = models.CharField(max_length=4)
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)

    class Meta:
        db_table = "airports"
        constraints = [models.UniqueConstraint(
            fields=["icao"], name="unique icao")]

    def __str__(self):
        return self.name


class Airline(models.Model):
    name = models.CharField(max_length=256)
    flight_identifier = models.CharField(max_length=3)

    class Meta:
        db_table = "airlines"
        constraints = [
            models.UniqueConstraint(
                fields=["flight_identifier"], name="unique flight identifier"
            )
        ]

    def __str__(self):
        return self.name


class Flight(models.Model):
    pilot = models.ForeignKey(
        Pilot, on_delete=models.SET_NULL, blank=True, null=True, related_name="pilot"
    )
    origin_airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="origin_airports"
    )
    destination_airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="destination_airports"
    )
    airline = models.ForeignKey(
        Airline, on_delete=models.CASCADE, related_name="airline"
    )
    status = models.CharField(default="Cadastrado", max_length=256)
    estimated_departure = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    real_departure = models.DateTimeField(blank=True, null=True)
    real_arrival = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "flights"
