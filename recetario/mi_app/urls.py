from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet, IngredienteViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'recetas', RecetaViewSet)
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
