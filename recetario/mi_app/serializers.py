from rest_framework import serializers
from .models import Receta, Ingrediente, RecetaIngrediente, Categoria

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'name', 'description']


class RecetaIngredienteSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer()

    class Meta:
        model = RecetaIngrediente
        fields = ['id', 'receta', 'ingrediente', 'quantity', 'unit']


class RecetaSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    ingredients = RecetaIngredienteSerializer(many=True)

    class Meta:
        model = Receta
        fields = ['id', 'title', 'description', 'time_required', 'difficulty', 'categoria', 'ingredients']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'name', 'description']
