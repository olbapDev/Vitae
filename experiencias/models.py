from django.db import models

# Create your models here.
class Experiencia(models.Model):
    nameEmpresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descripcion= models.TextField()

    def __str__(self):
        return self.nameEmpresa + ' | ' + self.cargo