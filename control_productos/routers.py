
from rest_framework import routers
 
from .views import ProductoViewApi, CategoriaViewApi, ProductoCategoriaViewApi

router = routers.SimpleRouter()

app_name = "control_productos"

router.register("productos", ProductoViewApi)
router.register("categorias", CategoriaViewApi)
router.register("productos_categoria", ProductoCategoriaViewApi, basename="productos_categoria")

urlpatterns = router.urls
