from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shipment.urls')),
    path('stats/', include('stats.urls')),
    path('lists/', include('lists.urls')),
    path('info/', include('info.urls')),
    path('charts/', include('charts.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='shipment/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shipment/logout.html'), name='logout'),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
