from rest_framework import serializers
from .models import Modalidad, Nivel


class ModalidadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Modalidad


class NivelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Nivel
