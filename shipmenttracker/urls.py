from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shipment.urls")),
    path("stats/", include("stats.urls")),
    path("lists/", include("lists.urls")),
    path("info/", include("info.urls")),
    path("charts/", include("charts.urls")),
    path("register/", include("registrations.urls")),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registrations/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="registrations/logout.html"),
        name="logout",
    ),
]

urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
