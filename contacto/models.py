from django.db import models
from django.urls import reverse
# Create your models here.
class Contacto(models.Model):
    name= models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return "nuevo mensaje de: " + self.name
    
    def get_absolute_url(self):
        return reverse('home')