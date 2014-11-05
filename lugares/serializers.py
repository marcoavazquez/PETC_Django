from rest_framework import serializers
from .models import Localidad, Municipio


class LocalidadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Localidad


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Municipio
