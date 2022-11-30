from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django_fsm import FSMField, transition
from .commons import STATUS_CHOICES


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
        return self.name


class User_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    profession = models.CharField(max_length=100)

    class Meta:
        db_table = "users_data"
        constraints = [models.UniqueConstraint(fields=["cpf"], name="unique document")]


class Airport(models.Model):
    icao = models.CharField(max_length=4)
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)

    class Meta:
        db_table = "airports"
        constraints = [models.UniqueConstraint(fields=["icao"], name="unique icao")]

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
        Airport, on_delete=models.CASCADE, related_name="origin_airports", default=1
    )
    destination_airport = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="destination_airports"
    )
    airline = models.ForeignKey(
        Airline, on_delete=models.CASCADE, related_name="airline"
    )
    status = FSMField(choices=STATUS_CHOICES, default="registered")
    estimated_departure = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    real_departure = models.DateTimeField(blank=True, null=True)
    real_arrival = models.DateTimeField(blank=True, null=True)
    is_origin = models.BooleanField(default=False)

    @transition(
        field=status,
        source="registered",
        target=["boarding", "cancelled"],
        permission="Main.status_registered_to_boarding_or_cancelled",
    )
    def to_boarding_or_cancelled(self):
        return "People are getting into the plane... or not"

    @transition(
        field=status,
        source="boarding",
        target="scheduled",
        permission="Main.status_boarding_to_scheduled",
    )
    def to_scheduled(self):
        return "Flight is scheduled"

    @transition(
        field=status,
        source="scheduled",
        target="taxiing",
        permission="Main.status_scheduled_to_taxiing",
    )
    def to_taxiing(self):
        return "Plane is taxiing"

    @transition(
        field=status,
        source="taxiing",
        target="ready",
        permission="Main.status_taxiing_to_ready",
    )
    def to_ready(self):
        return "Plane is ready to fly"

    @transition(
        field=status,
        source="ready",
        target="authorized",
        permission="Main.status_ready_to_authorized",
    )
    def to_authorized(self):
        return "Plane is authorized to departure"

    @transition(
        field=status,
        source="authorized",
        target="flying",
        permission="Main.status_authorized_to_flying",
    )
    def to_flying(self):
        return "Plane has departured"

    @transition(
        field=status,
        source="flying",
        target="landed",
        permission="Main.status_flying_to_landed",
    )
    def to_landed(self):
        return "Plane has landed"

    class Meta:
        db_table = "flights"
        permissions = [
            (
                "status_registered_to_boarding_or_cancelled",
                "Change status from registered to boarding or cancelled",
            ),
            (
                "status_boarding_to_scheduled",
                "Change status from boarding to scheduled",
            ),
            ("status_scheduled_to_taxiing", "Change status from scheduled to taxiing"),
            ("status_taxiing_to_ready", "Change status from taxiing to ready"),
            ("status_ready_to_authorized", "Change status from ready to authorized"),
            ("status_authorized_to_flying", "Change status from authorized to flying"),
            ("status_flying_to_landed", "Change status from flying to landed"),
        ]
