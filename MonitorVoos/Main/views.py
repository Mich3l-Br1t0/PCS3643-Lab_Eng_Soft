from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NameForm, RegisterForm
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    if request.method == "POST":
        # form = NameForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        # form = NameForm()
        form = RegisterForm()
    return render(request, "signup2.html", {"form": form})


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
