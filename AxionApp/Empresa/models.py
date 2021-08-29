from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empresa(models.Model):
    razonSocial = models.CharField(max_length=50, unique=True)
    cuit = models.CharField(max_length=11, blank=True)
    user = models.ManyToManyField(User,)

    class Meta:
        ordering = ["razonSocial"]
        verbose_name_plural = "Empresas"
                
    def __str__(self):
        return f"{self.razonSocial}"