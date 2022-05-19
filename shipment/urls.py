from django.urls import path

from . import views

urlpatterns = [
    path("", views.check_widget, name="home"),
    path("config/", views.config_widget, name="config"),
    path("widget/<widget_id>", views.redirecttowidget, name="redirect_widget"),
    path("about/", views.about, name="about"),
]
