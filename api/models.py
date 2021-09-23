from django.db import models


# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre
