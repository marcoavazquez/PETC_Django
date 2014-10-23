from django.db import models


class Municipio(models.Model):
    municipio = models.CharField(max_length=255)

    def __unicode__(self):
        return self.municipio


class Localidad(models.Model):
    localidad = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return "%s (%s)" % (self.localidad, self.municipio.municipio)
