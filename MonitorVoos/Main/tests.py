from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from Main.models import Pilot, Flight, Airport, User_data, Airline
from django.contrib.auth.models import User
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

        airline = Airline.objects.create(name="GOL Airlines", flight_identifier="GOL")

        estimated_departure = timezone.now()
        estimated_arrival = timezone.now() + timedelta(hours=3)

        Flight.objects.create(
            origin_airport=origin_airport,
            destination_airport=destination_airport,
            estimated_departure=estimated_departure,
            estimated_arrival=estimated_arrival,
            airline=airline,
        )

    def test_flight_id_creation(self):
        flight_one = Flight.objects.get(origin_airport__name__contains="Congonhas")
        self.assertEqual(flight_one.id, 1)


class UserTestCase(TestCase):
    def setUp(self):

        user_josenildo = User.objects.create(
            first_name="Josenildo",
            last_name="das Cruzes",
            username="josenildo123",
            email="josenildo@email.com",
        )

        user_jerivaldo = User.objects.create(
            first_name="Jerivaldo",
            last_name="Amoedo",
            username="jerivaldo123",
            email="jerivaldo@email.com",
        )

        User_data.objects.create(
            user=user_josenildo,
            cpf="62771054864",
            profession="manager",
        )

        User_data.objects.create(
            user=user_jerivaldo,
            cpf="12345678991",
            profession="worker",
        )

    def test_user_id_creation(self):
        user_one = User_data.objects.get(user__username__icontains="josenildo")
        self.assertEqual(user_one.id, 1)

    def test_user_update(self):
        user_one = User_data.objects.get(id=1)
        user_one.profession = "control"

        user_one.save()

        updated_user_one = User_data.objects.get(id=1)

        self.assertEqual(updated_user_one.profession, "control")

    def test_user_delete(self):
        original_length = len(User_data.objects.all())
        User_data.objects.first().delete()

        final_length = len(User_data.objects.all())
        self.assertEqual(final_length, original_length - 1)


class AirlineTestCase(TestCase):
    def setUp(self):
        Airline.objects.create(name="LATAM Airlines", flight_identifier="LAT")
        Airline.objects.create(name="Azul Airlines", flight_identifier="AZL")

    def test_airline_id_creation(self):
        airline_one = Airline.objects.get(name__icontains="LATAM")
        self.assertEqual(airline_one.id, 1)

    def test_airline_update(self):
        airline_two = Airline.objects.get(id=2)
        airline_two.flight_identifier = "AZU"

        airline_two.save()

        updated_airline_two = Airline.objects.get(id=2)

        self.assertEqual(updated_airline_two.flight_identifier, "AZU")

    def test_airline_delete(self):
        original_length = len(Airline.objects.all())
        Airline.objects.first().delete()

        final_length = len(Airline.objects.all())
        self.assertEqual(final_length, original_length - 1)

    def test_airline_view_get(self):
        response = self.client.get(reverse("airline_crud"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Azul")

    def test_airline_view_post(self):
        airline_data = {"name": "Laranja Airlines", "flight_identifier": "LRJ"}

        response = self.client.post(reverse("airline_crud"), data=airline_data)
        self.assertEqual(response.status_code, 201)
        self.assertContains(response, "Laranja")
