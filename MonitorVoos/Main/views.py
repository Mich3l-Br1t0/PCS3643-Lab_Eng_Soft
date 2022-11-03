from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import RegisterForm, Newflightform
from Main.models import User_data, Flight


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


def crud(request):
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
    return render(request, "crud.html", {"form": form})
