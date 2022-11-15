from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("home/crud/", views.crud, name="crud"),
    path("home/airport_crud", views.airport_crud, name="airport_crud"),
    path("home/airport_crud/<airport_id>", views.airport_update, name="airport_update"),
    path(
        "home/airport_crud/delete/<airport_id>",
        views.airport_delete,
        name="airport_delete",
    ),
]
