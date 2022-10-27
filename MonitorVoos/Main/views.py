from django.shortcuts import render


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
