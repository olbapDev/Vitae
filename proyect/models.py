from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=100)
    lenguaje = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='projects', null=True, blank=True)

    def __str__(self):
        return self.titulo + ' | '