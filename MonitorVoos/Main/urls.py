from django.urls import path

from ..MyProj import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("home", views.home, name="home"),
    path("signup", views.signup, name="signup"),
]
