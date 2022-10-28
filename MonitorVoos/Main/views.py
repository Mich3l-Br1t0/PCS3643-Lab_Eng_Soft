from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import Registerform
from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("")
    else:
        form = Registerform()
    return render(request, "register.html", {"form": form})


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def signup(request):
    return render(request, "signup.html")


def reports(request):
    return render(request, "reports.html")


def monitoring(request):
    return render(request, "monitoring.html")


def crud(request):
    return render(request, "crud.html")
