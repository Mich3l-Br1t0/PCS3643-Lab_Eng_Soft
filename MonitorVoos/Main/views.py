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
                    name=form.data["first_name"]
                    + " " + form.data["last_name"],
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


@login_required
def reports(request):
    return render(request, "reports.html")


@login_required
def monitoring(request):
    return render(request, "monitoring.html")


@login_required
def flights_crud(request):
    if not (request.user.is_superuser):
        user_id = request.user.pk
        user_profession = User_data.objects.get(user_id=user_id).profession
    else:
        user_profession = 'superuser'

    if not (user_profession in ['manager', 'superuser']):
        return redirect("/")
    if request.method == "POST":
        form = Newflightform(request.POST)
        Flight.objects.create(
            pilot_id=form.data["pilot"],
            origin_airport_id=form.data["departure_airport"],
            destination_airport_id=form.data["arrival_airport"],
            airline_id=form.data["airline"],
            status=form.data["status"],
            estimated_departure=form.data["estimated_departure"],
            estimated_arrival=form.data["estimated_arrival"],
        )
    else:
        form = Newflightform()
    return render(request, "flights_crud.html", {"form": form})


@login_required
def airline_crud(request):
    if not (request.user.is_superuser):
        user_id = request.user.pk
        user_profession = User_data.objects.get(user_id=user_id).profession
    else:
        user_profession = 'superuser'

    if not (user_profession in ['manager', 'superuser']):
        return redirect("/")
    if request.method == "POST":
        form = Newairlineform(request.POST)
        Airline.objects.create(
            name=form.data["name"],
            flight_identifier=form.data["flight_identifier"],
        )
    else:
        form = Newairlineform()
    return render(request, "airline_crud.html", {"form": form})
