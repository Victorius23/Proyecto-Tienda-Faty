# * mapear las rutas de la aplicación de ventas api

from django.urls import path
from rest_framework import routers

from .views import VentaViewApi
 
router = routers.SimpleRouter()
router.register("ventas", VentaViewApi)
 
urlpatterns = router.urls