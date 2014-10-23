from django.db import models
from escuelas.models import Ciclo
from personal.models import Personal

class Apoyo(models.Model):
    bruto_mensual = models.DecimalField(decimal_places=2, max_digits=8)
    isr_mensual = models.DecimalField(decimal_places=2, max_digits=8)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    ciclo = models.ForeignKey(Ciclo)
    rfc_personal = models.ForeignKey(Personal)

    def __unicode__(self):
        return self.rfc_personal.rfc
