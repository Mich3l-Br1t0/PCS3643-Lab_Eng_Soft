from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from .decorators import user_is_in_group
from django.contrib import messages
from .forms import (
    RegisterForm,
    Newflightform,
    Newairlineform,
    AirportForm,
    ReportForm,
    Editflightform,
    EditStatusForm,
)
from .models import User_data, Flight, Pilot, Airline, Airport
from django.http import FileResponse, HttpResponse
import io
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def createPDF(type, flights, pilot, start_date, end_date):
    buff = io.BytesIO()
    c = canvas.Canvas(buff, pagesize=letter, bottomup=0)

    text_object = c.beginText()
    text_object.setTextOrigin(inch, inch)
    text_object.setFont("Helvetica", 14)

    lines = []

    lines.append("Relatório de voos")
    lines.append("Período: " + start_date + " a " + end_date)
    lines.append("")

    if type == 1:
        for flight in flights:
            lines.append("Companhia: " + flight.airline.name)
            lines.append("Destino: " + flight.destination_airport.name)
            lines.append("Origem: " + flight.origin_airport.name)
            lines.append("Piloto: " + flight.pilot.name)
            lines.append("")

    if type == 2:
        lines.append("Piloto: " + pilot)
        lines.append("Voos no período: " + str(len(flights)))
        lines.append("")
        for flight in flights:
            lines.append(
                "Destino: "
                + flight.destination_airport.name
                + " - "
                + flight.destination_airport.city
                + " - "
                + flight.destination_airport.country
            )
            lines.append(
                "Origem: "
                + flight.origin_airport.name
                + " - "
                + flight.origin_airport.city
                + " - "
                + flight.origin_airport.country
            )
            lines.append("Partida Estimada: " + str(flight.estimated_arrival))
            lines.append("Chegada Estimada: " + str(flight.estimated_departure))
            lines.append("Partida Real: " + str(flight.real_departure))
            lines.append("Chegada Real: " + str(flight.real_arrival))
            lines.append("")

    for line in lines:
        text_object.textLine(line)

    c.drawText(text_object)
    c.showPage()
    c.save()
    buff.seek(0)

    return buff


def signup(request):
    def assign_user_to_group(user, group_name):
        group_object = Group.objects.get_or_create(name=group_name.lower())[0]
        user.groups.add(group_object)

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            user = User_data.objects.create(
                user_id=form.instance.id,
                cpf=form.data["cpf"],
                profession=form.data["profession"],
            )

            if form.data["profession"] == "Pilot":
                Pilot.objects.create(
                    name=form.data["first_name"] + " " + form.data["last_name"],
                    anac_code=form.data["anac_code"],
                    cpf=form.data["cpf"],
                )

            assign_user_to_group(user.user, form.data["profession"])

            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "signup.html", {"form": form})


def index(request):
    if request.user.is_authenticated:
        user_id = request.user.pk
        user_profession = User_data.objects.get(user_id=user_id).profession
        if user_profession == "Manager":
            return redirect("/home/reports")
        elif user_profession == "Operator":
            return redirect("/home/crud")
        elif user_profession in ["Control", "Pilot", "Worker"]:
            return redirect("/home")
        return redirect("/home")
    return redirect("/panel")


@login_required
def home(request):
    form = Newflightform()
    form.data = Flight.objects.all()

    return render(request, "home.html", {"form": form})


@user_is_in_group(["operator"])
@login_required(login_url="home/crud/")
def crud(request):
    return render(request, "crud.html")


def panel(request):
    form = Newflightform()
    form.data = Flight.objects.all()
    return render(request, "panel.html", {"form": form})


@login_required
@user_is_in_group(["manager"])
def reports(request):
    if request.method == "POST":
        data = request.POST
        if not ReportForm(data).is_valid():
            form = ReportForm(data)
            return render(request, "reports.html", {"form": form})
        start_date = (
            data["start_date_year"]
            + "-"
            + data["start_date_month"]
            + "-"
            + data["start_date_day"]
        )
        end_date = (
            data["end_date_year"]
            + "-"
            + data["end_date_month"]
            + "-"
            + data["end_date_day"]
        )
        if data["Pilot"] == "":
            flights = Flight.objects.filter(
                estimated_departure__gte=datetime.date(
                    int(data["start_date_year"]),
                    int(data["start_date_month"]),
                    int(data["start_date_day"]),
                ),
                estimated_departure__lte=datetime.date(
                    int(data["end_date_year"]),
                    int(data["end_date_month"]),
                    int(data["end_date_day"]),
                ),
            )
            if len(flights) == 0:
                return HttpResponse("Não há voos no período selecionado")
            file = createPDF(1, flights, "", start_date, end_date)
            return FileResponse(file, as_attachment=True, filename="MonitorVoos.pdf")
        else:
            flights = Flight.objects.filter(
                estimated_departure__gte=datetime.date(
                    int(data["start_date_year"]),
                    int(data["start_date_month"]),
                    int(data["start_date_day"]),
                ),
                estimated_departure__lte=datetime.date(
                    int(data["end_date_year"]),
                    int(data["end_date_month"]),
                    int(data["end_date_day"]),
                ),
                pilot_id=data["Pilot"],
            )
            if len(flights) == 0:
                return HttpResponse("Não há voos no período selecionado")
            file = createPDF(2, flights, flights[0].airline.name, start_date, end_date)
            return FileResponse(file, as_attachment=True, filename="MonitorVoos.pdf")
    form = ReportForm()
    return render(request, "reports.html", {"form": form})


@login_required
@user_is_in_group(["pilot", "control", "worker"])
def monitoring_update(request, flight_id):
    # def which_transition(flight):
    #     if flight.status == "Cadastrado":
    #         flight.to_boarding_or_cancelled()
    #     elif flight.status == "Embarcando":
    #         flight.to_scheduled()

    # def _check_real_departure_and_arrival(flight, form):
    #     if flight.estimated_departure < form["real_departure"]:
    #         return False
    #     elif flight.estimated_arrival < form["real_arrival"]:
    #         return False
    #     elif form["real_departure"] > form["real_arrival"]:
    #         return False

    #     return True

    flight = Flight.objects.get(pk=flight_id)
    form = EditStatusForm(request.POST or None, instance=flight)
    if request.method == "POST":
        flight.status = form.data["status"]
        if form.data["real_departure"] and not flight.real_departure:
            # if _check_real_departure_and_arrival(flight, form):
            flight.real_departure = form.data["real_departure"]
        if form.data["real_arrival"] and not flight.real_arrival:
            flight.real_arrival = form.data["real_arrival"]
        flight.save()
        return redirect("/home")
    return render(request, "monitoring/monitoring_update.html", {"form": form})


@login_required
@user_is_in_group(["operator"])
def flights_crud(request):
    if request.method == "POST":
        form = Newflightform(request.POST)
        if form.is_valid():
            form.save()
            if form.data["origin_airport"] == "1":
                flight = Flight.objects.get(pk=form.instance.pk)
                flight.is_origin = True
                flight.save()
            messages.success(request, "Voo Adicionado")
            return redirect("/home/flights_crud")
        form.flights = Flight.objects.all()
        return render(request, "flights_crud.html", {"form": form})
    else:
        form = Newflightform()
        form.flights = Flight.objects.all()
    return render(request, "flights_crud.html", {"form": form})


@login_required
@user_is_in_group(["operator", "worker", "pilot", "control"])
def flights_update(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    form = Editflightform(request.POST or None, instance=flight)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/home/flights_crud")
        else:
            return render(request, "flights/flights_update.html", {"form": form})
    return render(request, "flights/flights_update.html", {"form": form})


@login_required
@user_is_in_group(["operator"])
def flights_delete(request, flight_id):
    Flight.objects.get(pk=flight_id).delete()
    return redirect("/home/flights_crud")


@login_required
@user_is_in_group(["operator"])
def airline_crud(request):
    if request.method == "POST":
        form = Newairlineform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home/airline_crud")
    else:
        form = Newairlineform()
        form.data = Airline.objects.all()
    return render(request, "airline_crud.html", {"form": form})


@login_required
@user_is_in_group(["operator"])
def airline_update(request, airline_id):
    airline = Airline.objects.get(pk=airline_id)
    form = Newairlineform(request.POST or None, instance=airline)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("/home/airline_crud")
    return render(request, "airlines/airline_update.html", {"form": form})


@login_required
@user_is_in_group(["operator"])
def airline_delete(request, airline_id):
    Airline.objects.get(pk=airline_id).delete()
    return redirect("/home/airline_crud")


@login_required
@user_is_in_group(["operator"])
def airport_crud(request):
    if request.method == "POST":
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/airport_crud")
        form.airports = Airport.objects.all()
        return render(request, "airport_crud.html", {"form": form})
    else:
        form = AirportForm()
        form.airports = Airport.objects.all()
    return render(request, "airport_crud.html", {"form": form})


@login_required
@user_is_in_group(["operator"])
def airport_update(request, airport_id):
    if Group.objects.get(name="operator") in request.user.groups.all():
        airport = Airport.objects.get(pk=airport_id)
        form = AirportForm(request.POST or None, instance=airport)
        if request.method == "POST":
            if form.is_valid():
                form.save()
            return redirect("/home/airport_crud")
        return render(request, "airports/airport_update.html", {"form": form})
    else:
        return HttpResponse("User is not authorized to access this page", status=403)


@user_is_in_group(["operator"])
def airport_delete(request, airport_id):
    Airport.objects.get(pk=airport_id).delete()
    return redirect("/home/airport_crud")
