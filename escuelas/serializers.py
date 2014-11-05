from rest_framework import serializers
from .models import Escuela, Ciclo


class EscuelaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Escuela


class CicloSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ciclo
