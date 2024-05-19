"""
URL configuration for tiendafaty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib.auth import views as auth_views

admin.site.site_header = "Tienda Faty"


urlpatterns = [
    path("admin/", admin.site.urls),




    # reset password
    path(
        "reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"
    ),
    # reset password send
    path(
        "reset_password_send/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    # reset password <uidb64>/<token>
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # reset password complete con un boton para redirigir a login
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("api/", include("control_ventas.routers")),
    path("api/", include("control_productos.routers")),

    path("api/", include("control_ventas.urls")),
    path("api/", include("control_inventario.urls")),
    
    path("api/", include("registration.urls")),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)