from django.contrib import admin
from Main.models import Pilot, Airport, Flight, User

# Register your models here.


@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ("anac_code", "name")

    class Meta:
        ordering = "name"


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("icao", "name", "city", "country")

    class Meta:
        ordering = "name"


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "origin_airport",
        "destination_airport",
        "estimated_departure",
        "estimated_arrival",
        "status",
    )

    class Meta:
        ordering = "status"


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

    class Meta:
        ordering = "name"
