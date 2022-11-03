# Generated by Django 4.1.1 on 2022-11-03 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Airline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("flight_identifier", models.CharField(max_length=3)),
            ],
            options={
                "db_table": "airlines",
            },
        ),
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("icao", models.CharField(max_length=4)),
                ("name", models.CharField(max_length=256)),
                ("city", models.CharField(max_length=256)),
                ("state", models.CharField(max_length=256)),
                ("country", models.CharField(max_length=256)),
            ],
            options={
                "db_table": "airports",
            },
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(default="Cadastrado", max_length=256)),
                ("estimated_departure", models.DateTimeField()),
                ("estimated_arrival", models.DateTimeField()),
                ("real_departure", models.DateTimeField(blank=True, null=True)),
                ("real_arrival", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "flights",
            },
        ),
        migrations.CreateModel(
            name="Pilot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("anac_code", models.CharField(max_length=6)),
                ("cpf", models.CharField(max_length=11)),
            ],
            options={
                "db_table": "pilots",
            },
        ),
        migrations.CreateModel(
            name="User_data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cpf", models.CharField(max_length=11)),
                ("profession", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "users_data",
            },
        ),
        migrations.AddConstraint(
            model_name="pilot",
            constraint=models.UniqueConstraint(
                fields=("anac_code", "cpf"), name="unique anac code"
            ),
        ),
        migrations.AddField(
            model_name="flight",
            name="airline",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="airline",
                to="Main.airline",
            ),
        ),
        migrations.AddField(
            model_name="flight",
            name="destination_airport",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="destination_airports",
                to="Main.airport",
            ),
        ),
        migrations.AddField(
            model_name="flight",
            name="origin_airport",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="origin_airports",
                to="Main.airport",
            ),
        ),
        migrations.AddField(
            model_name="flight",
            name="pilot",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pilot",
                to="Main.pilot",
            ),
        ),
        migrations.AddConstraint(
            model_name="airport",
            constraint=models.UniqueConstraint(fields=("icao",), name="unique icao"),
        ),
        migrations.AddConstraint(
            model_name="user_data",
            constraint=models.UniqueConstraint(fields=("cpf",), name="unique document"),
        ),
    ]
