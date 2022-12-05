# Generated by Django 4.0.3 on 2022-12-01 18:43

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0007_group_and_permissions_creation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="status",
            field=django_fsm.FSMField(
                choices=[
                    ("Cadastrado", "Cadastrado"),
                    ("Embarcando", "Embarcando"),
                    ("Cancelado", "Cancelado"),
                    ("Programado", "Programado"),
                    ("Taxiando", "Taxiando"),
                    ("Pronto", "Pronto"),
                    ("Em voo", "Em voo"),
                    ("Aterrisado", "Aterrisado"),
                ],
                default="registered",
                max_length=50,
            ),
        ),
    ]