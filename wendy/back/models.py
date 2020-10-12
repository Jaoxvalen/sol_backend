from django.db import models

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)
    peso = models.IntegerField()
    talla = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre


