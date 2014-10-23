from django.db import models

class Nivel(models.Model):
    nivel = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nivel

class Modalidad(models.Model):
    modalidad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.modalidad
