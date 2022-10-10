from django.test import TestCase
from django.utils import timezone
from Main.models import Pilot, Flight, Airport, User
from datetime import timedelta

# Create your tests here.


class AiportTestCase(TestCase):
    def setUp(self):
        Airport.objects.create(
            icao="SBSP",
            name="Aeroporto de Congonhas",
            city="São Paulo",
            state="São Paulo",
            country="Brasil",
        )

        Airport.objects.create(
            icao="SBSS",
            name="Aeroporto de É NOIS",
            city="São Paulo",
            state="RJ",
            country="Zambabue",
        )

        Airport.objects.create(
            icao="SBRS",
            name="Aeroporto de Sulito",
            city="Curitiba",
            state="RS",
            country="Sulito",
        )

    def test_airport_create(self):
        airport_one = Airport.objects.get(icao="SBSP")
        self.assertEqual(airport_one.id, 1)

    def test_airport_update(self):
        airport_two = Airport.objects.get(id=2)
        airport_two.icao = "SBBB"

        airport_two.save()

        updated_airport_two = Airport.objects.get(id=2)

        self.assertEqual(updated_airport_two.icao, "SBBB")

    def test_airport_delete(self):
        original_length = len(Airport.objects.all())
        Airport.objects.first().delete()

        final_length = len(Airport.objects.all())
        self.assertEqual(final_length, original_length - 1)


class PilotTestCase(TestCase):
    def setUp(self):
        Pilot.objects.create(
            name="Paulinho Renan", anac_code="ANAC22", cpf="12345678990"
        )

        Pilot.objects.create(
            name="Carlinhos Bala", anac_code="ANAC17", cpf="45319371023"
        )

        Pilot.objects.create(name="Josevaldo", anac_code="ANAC13", cpf="1653919371292")

    def test_pilot_id_creation(self):
        pilot_one = Pilot.objects.get(name__icontains="Paulinho")
        self.assertEqual(pilot_one.id, 1)

    def test_pilot_update(self):
        pilot_two = Pilot.objects.get(id=2)
        pilot_two.anac_code = "ANAC12"

        pilot_two.save()

        updated_pilot_two = Pilot.objects.get(id=2)

        self.assertEqual(updated_pilot_two.anac_code, "ANAC12")

    def test_pilot_delete(self):
        original_length = len(Pilot.objects.all())
        Pilot.objects.first().delete()

        final_length = len(Pilot.objects.all())
        self.assertEqual(final_length, original_length - 1)


class FlightTestCase(TestCase):
    def setUp(self):
        origin_airport = Airport.objects.create(
            icao="SBSP",
            name="Aeroporto de Congonhas",
            city="São Paulo",
            state="SP",
            country="Brasil",
        )
        destination_airport = Airport.objects.create(
            icao="SBRJ",
            name="Aeroporto de Santos Dumont",
            city="Rio de Janeiro",
            state="RJ",
            country="Brasil",
        )

        estimated_departure = timezone.now()
        estimated_arrival = timezone.now() + timedelta(hours=3)

        Flight.objects.create(
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            estimated_departure=estimated_departure,
            estimated_arrival=estimated_arrival,
        )

    def test_flight_id_creation(self):
        flight_one = Flight.objects.get(origin_airport__name__contains="Congonhas")
        self.assertEqual(flight_one.id, 1)

class UserTestCase(TestCase):
    def setUp(self):
       user = User.objects.create(
        name = "Josenildo das Cruzes",
        cpf = "62771054864",
        email = "josenildo@email.com",
        password="josenildo10",
       )

    def test_user_id_creation(self):
        user_one = User.objects.get(name__icontains="Josenildo")
        self.assertEqual(user_one.id, 1)
    
