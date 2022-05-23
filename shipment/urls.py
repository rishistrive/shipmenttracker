from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="home"),
    path("config/", views.config_widget, name="config"),
    path("widget/<widget_id>/", views.redirect_to_widget, name="redirect_widget"),
    path("about/", views.about, name="about"),
]
