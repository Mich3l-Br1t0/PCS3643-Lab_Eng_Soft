from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    #path("", index),
    #path("home/", home),
    #path("signup/", signup),
    #path("home/reports/", reports),
    #path("home/monitoring/", monitoring),
    #path("home/crud/", crud),
]
