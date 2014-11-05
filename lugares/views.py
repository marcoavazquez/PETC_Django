from rest_framework import viewsets
from .models import Localidad, Municipio
from serializers import LocalidadSerializer, MunicipioSerializer


class LocalidadViewSet(viewsets.ModelViewSet):
    model = Localidad
    serializer_class = LocalidadSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    model = Municipio
    serializer_class = MunicipioSerializer
