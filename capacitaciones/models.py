from django.db import models
from escuelas.models import Escuela

class Capacitacion(models.Model):
    capacitacion = models.CharField(max_length=255)

    def __unicode__(self):
        return self.capacitacion


class CapacitacionesPorEscuela(models.Model):
    clave_escuela = models.ForeignKey(Escuela)
    capacitacion = models.ForeignKey(Capacitacion)
    fecha = models.DateField()

    def __unicode__(self):
        return self.clave_escuela.clave
