from django.shortcuts import render


def bookview(request):
    return render(request, "FIRST.html")
