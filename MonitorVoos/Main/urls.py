from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("home/flights_crud/", views.flights_crud, name="flights_crud"),
    path("home/airline_crud/", views.airline_crud, name="airline_crud"),
    path("home/flights_crud/<flight_id>", views.flights_update, name="flights_update"),
    path(
        "home/flights_crud/delete/<flight_id>",
        views.flights_delete,
        name="flights_delete",
    ),
    path("home/airline_crud/<airline_id>", views.airline_update, name="airline_update"),
    path(
        "home/airline_crud/delete/<airline_id>",
        views.airline_delete,
        name="airline_delete",
    ),
    path("home/reports/", views.reports, name="reports"),
]
