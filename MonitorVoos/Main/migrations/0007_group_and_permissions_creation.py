from django.db import migrations
from django.contrib.auth.models import Group, User
from ..commons import PROFESSION_CHOICES
from ..models import User_data
from django.contrib.auth.models import Permission


def create_groups_with_permissions(apps, schema_editor):
    pilot_permissions = [
        Permission.objects.get(codename="status_scheduled_to_taxiing"),
        Permission.objects.get(codename="status_taxiing_to_ready"),
        Permission.objects.get(codename="status_authorized_to_flying"),
        Permission.objects.get(codename="status_flying_to_landed"),
    ]

    control_permissions = [
        Permission.objects.get(codename="status_ready_to_authorized")
    ]

    worker_permissions = [
        Permission.objects.get(codename="status_registered_to_boarding_or_cancelled"),
        Permission.objects.get(codename="status_boarding_to_scheduled"),
    ]

    for group, dummy in PROFESSION_CHOICES:
        gp = Group.objects.get_or_create(name=group.lower())[0]

        if group == "Pilot":
            gp.permissions.add(*pilot_permissions)
        elif group == "Worker":
            gp.permissions.add(*worker_permissions)
        elif group == "Control":
            gp.permissions.add(*control_permissions)


def attribute_groups_to_users(apps, schema_editor):
    for user_data in User_data.objects.all():
        user = user_data.user
        group = Group.objects.get(name=user_data.profession.lower())
        user.groups.add(group)


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0006_alter_flight_options_alter_flight_status"),
    ]

    operations = [
        migrations.RunPython(create_groups_with_permissions),
        migrations.RunPython(attribute_groups_to_users),
    ]
