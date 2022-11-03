from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import RegisterForm, Newflightform, Newairlineform
from Main.models import User_data, Airline


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


def crud(request):
    if request.method == "POST":
        form = Newflightform(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = Newflightform()
    return render(request, "crud.html", {"form": form})
