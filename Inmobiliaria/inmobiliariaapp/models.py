from django.db import models

# Create your models here.
class Inmueble(models.Model):
    Nombre=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="inmobiliariaapp", null=True, blank=True)
    precio=models.FloatField()
    metros_cuadrados=models.IntegerField()
    habitaciones=models.IntegerField()
    banos=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Inmueble'
        verbose_name_plural='Inmuebles'

    def __str__(self):
        return self.Nombre    