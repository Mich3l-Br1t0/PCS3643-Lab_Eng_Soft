# Generated by Django 4.0.3 on 2022-11-23 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0002_airline_unique flight identifier"),
    ]

    operations = [
        migrations.AddField(
            model_name="flight",
            name="is_departure_flight",
            field=models.BooleanField(default=True),
        ),
    ]