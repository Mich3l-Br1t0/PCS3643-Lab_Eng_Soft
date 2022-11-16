from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    form = Newflightform()
    form.data = Flight.objects.all()

    return render(request, "home.html", {"form": form})


@login_required
def reports(request):
    return render(request, "reports.html")


@login_required
def monitoring_update(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    form = Newflightform(request.POST or None, instance=flight)
    if request.method == "POST":
        if request.method == "POST":
            if form.is_valid():
                form.save()
            return redirect("/home")
    return render(request, "monitoring/monitoring_update.html", {"form": form})


@login_required
def flights_crud(request):
    if not (request.user.is_superuser):
        user_id = request.user.pk
        user_profession = User_data.objects.get(user_id=user_id).profession
    else:
        user_profession = "superuser"

    if not (user_profession in ["manager", "superuser"]):
        return redirect("/")

    if request.method == "POST":
        form = Newflightform(request.POST)
        if form.is_valid():
            form.save()
            # Ta dando erro essa parada comentada aqui
            # messages.success(request, "student with name  {}  added.".format(form.name))
            return redirect("/home/flights_crud")
        form.flights = Flight.objects.all()
        return render(request, "flights_crud.html", {"form": form})
    else:
        form = Newflightform()
        form.flights = Flight.objects.all()
    return render(request, "flights_crud.html", {"form": form})


@login_required
def flights_update(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    form = Newflightform(request.POST or None, instance=flight)
    if request.method == "POST":
        if request.method == "POST":
            if form.is_valid():
                form.save()
            return redirect("/home/flights_crud")
    return render(request, "flights/flights_update.html", {"form": form})


def flights_delete(flight_id):
    Flight.objects.get(pk=flight_id).delete()
    return redirect("/home/flights_crud")


@login_required
def airline_crud(request):
    if not (request.user.is_superuser):
        user_id = request.user.pk
        user_profession = User_data.objects.get(user_id=user_id).profession
    else:
        user_profession = "superuser"

    if not (user_profession in ["manager", "superuser"]):
        return redirect("/")

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
def airline_update(request, airline_id):
    airline = Airline.objects.get(pk=airline_id)
    form = Newairlineform(request.POST or None, instance=airline)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("/home/airline_crud")
    return render(request, "airlines/airline_update.html", {"form": form})


def airline_delete(airline_id):
    Airline.objects.get(pk=airline_id).delete()
    return redirect("/home/airline_crud")
