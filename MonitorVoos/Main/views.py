from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NameForm
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        print(request.POST)
        return redirect("/")
    else:
        form = NameForm()
    return render(request, "signup.html", {"form": form})


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def reports(request):
    return render(request, "reports.html")


def monitoring(request):
    return render(request, "monitoring.html")


def crud(request):
    return render(request, "crud.html")
