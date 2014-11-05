from rest_framework import serializers
from .models import PersonalPorCiclo, Personal, NivelEstudio, Especialidad, Puesto, Estado


class PersonalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personal


class PersonalPorCicloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalPorCiclo


class NivelEstudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NivelEstudio


class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especialidad


class PuestoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Puesto


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
