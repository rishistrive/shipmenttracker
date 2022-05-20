from django.urls import path

from . import views

urlpatterns = [
    path("", views.check_widget, name="home"),
    path("config/", views.config_widget, name="config"),
<<<<<<< HEAD
    path("widget/<widget_id>/", views.redirect_to_widget, name="redirect_widget"),
=======
    path("widget/<widget_id>", views.redirecttowidget, name="redirect_widget"),
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
    path("about/", views.about, name="about"),
]
