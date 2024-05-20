from rest_framework import routers

from .views import CantidadProductos, CantidadStock

router = routers.SimpleRouter()

router.register("cantidad-stock", CantidadStock)
router.register("cantidad_productos", CantidadProductos, basename="cantidad_productos")


urlpatterns = router.urls