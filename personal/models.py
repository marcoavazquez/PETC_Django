from django.db import models
from escuelas.models import Ciclo, Escuela

class NivelEstudio(models.Model):
    nivel_estudio = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nivel_estudio


class Especialidad(models.Model):
    especialidad = models.CharField(max_length=255)

    def __unicode__(self):
        return self.especialidad


class Personal(models.Model):
    rfc = models.CharField(max_length=15)
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    doble_plaza = models.BooleanField(default=False)
    fecha_ingreso = models.DateField()
    fecha_nacimiento = models.DateField()
    nivel_estudio = models.ForeignKey(NivelEstudio)
    especialidad = models.ForeignKey(Especialidad)

    def dos_plaza(self):
        if self.doble_plaza:
            p = "Si"
        else:
            p = "No"
        return p

    def __unicode__(self):
        return "%s - %s" % (self.rfc, self.nombre)


class Puesto(models.Model):
    puesto = models.CharField(max_length=255)

    def __unicode__(self):
        return self.puesto


class Estado(models.Model):
    estado = models.CharField(max_length=255)

    def __unicode__(self):
        return self.estado


class PersonalPorCiclo(models.Model):
    personal = models.ForeignKey(Personal)
    ciclo = models.ForeignKey(Ciclo)
    puesto = models.ForeignKey(Puesto)
    escuela = models.ForeignKey(Escuela)
    estado = models.ForeignKey(Estado)

    class Meta:
        unique_together = [("personal", "ciclo", "escuela")]

    def __unicode__(self):
        return "%s - %s - %s" % (self.personal, self.escuela, self.ciclo)
