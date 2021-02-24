from django.db import models

# Create your models here.
class Conocimiento(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100, default='basico')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre + ' | ' + self.nivel