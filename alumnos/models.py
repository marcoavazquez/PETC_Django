from django.db import models
from escuelas.models import Escuela, Ciclo


class Alumnos(models.Model):
    cantidad = models.PositiveIntegerField()
    numero_grupos = models.PositiveIntegerField()
    grado = models.PositiveIntegerField()
    escuela = models.ForeignKey(Escuela)
    ciclo = models.ForeignKey(Ciclo)


    def __unicode__(self):
        return "%s - %s (%s)" % (self.escuela.clave, self.escuela.nombre, self.ciclo)
