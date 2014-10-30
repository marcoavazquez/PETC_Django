from django.db import models
from lugares.models import Municipio, Localidad
from caracteristicas.models import Nivel, Modalidad
from petc.settings import CICLO_ACTUAL


class EscuelaQuerySet(models.QuerySet):

    def afiliada(self):
        return self.filter(afiliada=True)


class Escuela(models.Model):
    clave = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio)
    localidad = models.ForeignKey(Localidad)
    zona = models.PositiveIntegerField()
    sector = models.PositiveIntegerField()
    modalidad = models.ForeignKey(Modalidad)
    nivel = models.ForeignKey(Nivel)
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=25)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=30)
    colonia = models.CharField(max_length=255)
    cod_postal = models.PositiveIntegerField()
    afiliada = models.BooleanField(default=False)

    objects = EscuelaQuerySet.as_manager()

    def esta_afiliada(self):
        if self.afiliada:
            return "Si"
        else:
            return "No"

    def __unicode__(self):
        return self.clave


class Ciclo(models.Model):
    #ciclo es el anho de inicio de curso
    ciclo = models.PositiveIntegerField(unique=True)

    def fin_ciclo(self):
        fin = self.ciclo + 1
        return fin

    def __unicode__(self):
        return "%i-%i" % (self.ciclo, self.fin_ciclo())


class EscuelasPorCiclo(models.Model):
    ciclo = models.ForeignKey(Ciclo)
    escuela = models.ForeignKey(Escuela)

    class Meta:
        unique_together = [("ciclo", "escuela")]

    def es_ciclo_actual(self):
        if self.ciclo.ciclo == CICLO_ACTUAL:
            return True
        else:
            return False

    def anho_ciclo(self):
        return self.ciclo.ciclo

    def __unicode__(self):
        return "%s(%s)" % (self.escuela, self.ciclo)
