import django_filters
from .models import Receta

class RecetaFilter(django_filters.FilterSet):
    categoria = django_filters.NumberFilter(field_name='categoria__id', lookup_expr='exact')  # Filtra por ID de categoría
    difficulty = django_filters.CharFilter(field_name='difficulty', lookup_expr='exact')  # Filtra por dificultad
    time_required = django_filters.NumberFilter(field_name='time_required', lookup_expr='lte')  # Filtra por tiempo de preparación

    class Meta:
        model = Receta
        fields = ['categoria', 'difficulty', 'time_required']