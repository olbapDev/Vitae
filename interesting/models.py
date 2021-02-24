from django.db import models

# Create your models here.
class Interes(models.Model):
    tittle = models.CharField(max_length=100)
    nota = models.TextField()

    def __str__(self):
        return self.tittle+ ' | '