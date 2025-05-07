from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categorías'


class Ingrediente(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ingredientes'


class Receta(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    time_required = models.PositiveIntegerField(help_text="Tiempo de preparación en minutos")
    difficulty = models.CharField(max_length=50, choices=[('Fácil', 'Fácil'), ('Medio', 'Medio'), ('Difícil', 'Difícil')])
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="recetas")
    ingredients = models.ManyToManyField(Ingrediente, through='RecetaIngrediente')

    def __str__(self):
        return self.title


class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.quantity} {self.unit} de {self.ingrediente.name} para {self.receta.title}'
