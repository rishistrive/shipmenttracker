from django.urls import path

from . import views

urlpatterns = [
    path("", views.check_widget, name="home"),
    path("config/", views.config_widget, name="config"),
    path("about/", views.about, name="about"),
]
