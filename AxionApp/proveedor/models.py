from django.db import models


# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    cuit = models.CharField(max_length=11, blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return f"{self.nombre}"
