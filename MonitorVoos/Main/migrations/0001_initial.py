# Generated by Django 4.1.1 on 2022-10-13 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
            name="User",
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
                ("cpf", models.CharField(max_length=11)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=256)),
            ],
            options={
                "db_table": "users",
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
                (
                    "airline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="airline",
                        to="Main.airline",
                    ),
                ),
                (
                    "destination_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destination_airports",
                        to="Main.airport",
                    ),
                ),
                (
                    "origin_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="origin_airports",
                        to="Main.airport",
                    ),
                ),
                (
                    "pilot",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="pilot",
                        to="Main.pilot",
                    ),
                ),
            ],
            options={
                "db_table": "flights",
            },
        ),
    ]
