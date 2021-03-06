from datetime import datetime
from django.db import models

# Create your models here.
from chPropios.choices import BANCOS
from proveedor.models import Proveedor
from Empresa.models import Empresa


class chPropio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True,)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    banco = models.CharField(max_length=50, choices=BANCOS, default='HSBC')
    numCh = models.CharField(max_length=8,)
    fechaCarga = models.DateField(default=datetime.now) # (auto_now_add=True) para que no se muestre el campo
    fechaVto = models.DateField(auto_now=False)
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    pagado = models.BooleanField(default=False, )  # help_text="Fue pagado ya el cheque?"

    class Meta:
        ordering = ["monto"]
        verbose_name = "Cheque Propio"
        verbose_name_plural = "Cheques Propios"
        #unique_together = (('banco', 'numCh',),) # par de campos unicos en tupla
        constraints = [
            models.UniqueConstraint(fields=['banco', 'numCh',], name='Cheque unico')
        ] # tambien para campos unicos en pares

    def __str__(self):
        return f"Persona {self.id}: Proveedor: {self.proveedor}, Cheque: {self.banco}-{self.numCh}, Vencimiento: {self.fechaVto}, Monto: ${self.monto}"

    # def estado(self):
    #     if self.fechaVto >= datetime.now():
    #         self.situacion = "Vencido"
    #     else:
    #         self.situacion = "No vencido"
