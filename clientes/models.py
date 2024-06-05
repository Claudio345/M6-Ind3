from django.db import models

# Create your models here.
class Cliente(models.Model):
    image = models.URLField(verbose_name="Url de la imagen")
    nombre = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    