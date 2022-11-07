from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import RegisterForm, Newflightform, Newairlineform
from Main.models import User_data, Flight, Pilot, Airline


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            User_data.objects.create(
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
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "signup.html", {"form": form})


def index(request):
    if request.user.is_authenticated:
        return redirect("/home")
    return redirect("/login")


@login_required
def home(request):
    return render(request, "home.html")


def reports(request):
    return render(request, "reports.html")


def monitoring(request):
    return render(request, "monitoring.html")


def flights_crud(request):
    if request.method == "POST":
        form = Newflightform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home/flights_crud")
    else:
        form = Newflightform()
        form.data = Flight.objects.all()
    return render(request, "flights_crud.html", {"form": form})


def flights_update(request, flight_id):
    allFlights = Flight.objects.get(pk=flight_id)
    if request.method == "POST":
        form = Newflightform(request.POST or None, instance=allFlights)
        if request.method == "POST":
            if form.is_valid():
                form.save()
            return redirect("/home/flights_crud")
    return render(request, "flights/flights_crud.html", {"form": form})


def flights_delete(request, flight_id):
    Flight.objects.get(pk=flight_id).delete()
    return redirect("/home/flights_crud")


def airline_crud(request):
    if request.method == "POST":
        form = Newairlineform(request.POST)
        Airline.objects.create(
            name=form.data["name"],
            flight_identifier=form.data["flight_identifier"],
        )
    else:
        form = Newairlineform()
    return render(request, "airline_crud.html", {"form": form})
