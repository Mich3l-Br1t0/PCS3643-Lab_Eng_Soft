from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import Registerform, Newflightform
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = Registerform()
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
    if request.method == "POST":
        form = Newflightform(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = Newflightform()
    return render(request, "crud.html", {"form": form})
