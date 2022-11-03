from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("home/crud/", views.crud, name="crud"),
    path("home/airport_crud", views.airport_crud, name="airport_crud"),
]
