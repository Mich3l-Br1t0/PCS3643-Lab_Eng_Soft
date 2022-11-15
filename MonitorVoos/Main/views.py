from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import RegisterForm, Newflightform, AirportForm
from .models import User_data, Airport


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
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = Newflightform()
    return render(request, "crud.html", {"form": form})


def airport_crud(request):
    if not (request.user.is_superuser):
        user_id = request.user.pk
        user_profession = User_data.objects.get(user_id=user_id).profession
    else:
        user_profession = "superuser"

    if not (user_profession in ["manager", "superuser"]):
        return redirect("/")

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
def airport_update(request, airport_id):
    airport = Airport.objects.get(pk=airport_id)
    form = AirportForm(request.POST or None, instance=airport)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect("/home/airport_crud")
    return render(request, "airports/airport_update.html", {"form": form})


def airport_delete(request, airport_id):
    Airport.objects.get(pk=airport_id).delete()
    return redirect("/home/airport_crud")
