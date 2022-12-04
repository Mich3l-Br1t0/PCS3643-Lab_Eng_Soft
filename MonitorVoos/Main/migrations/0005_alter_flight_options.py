# Generated by Django 4.0.3 on 2022-11-30 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0004_flight_is_origin"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="flight",
            options={
                "permissions": [
                    (
                        "status_registered_to_boarding_or_cancelled",
                        "Change status from registered to boarding or cancelled",
                    ),
                    (
                        "status_boarding_to_scheduled",
                        "Change status from boarding to scheduled",
                    ),
                    (
                        "status_scheduled_to_taxiing",
                        "Change status from scheduled to taxiing",
                    ),
                    (
                        "status_ready_to_authorized",
                        "Change status from ready to authorized",
                    ),
                    (
                        "status_authorized_to_flying",
                        "Change status from authorized to flying",
                    ),
                    ("status_flying_to_landed", "Change status from flying to landed"),
                ]
            },
        ),
    ]
