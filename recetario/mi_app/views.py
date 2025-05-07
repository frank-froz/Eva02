from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Receta, Ingrediente, Categoria
from .serializers import RecetaSerializer, IngredienteSerializer, CategoriaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['categoria', 'difficulty']
    ordering_fields = ['time_required', 'difficulty']

    @action(detail=False, methods=['get'])
    def search_by_ingredients(self, request):
        ingredientes = request.query_params.get('ingredientes', None)
        if ingredientes:
            ingredientes_list = ingredientes.split(',')
            recetas = Receta.objects.filter(ingredients__name__in=ingredientes_list).distinct()
            serializer = self.get_serializer(recetas, many=True)
            return Response(serializer.data)
        return Response({'detail': 'No ingredients provided'}, status=400)


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
