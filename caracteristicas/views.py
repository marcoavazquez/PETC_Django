from rest_framework import viewsets
from serializers import ModalidadSerializer, NivelSerializer
from .models import Modalidad, Nivel


class ModalidadViewSet(viewsets.ModelViewSet):
    model = Modalidad
    serializers_class = ModalidadSerializer


class NivelViewSet(viewsets.ModelViewSet):
    model = Nivel
    serializers_class = NivelSerializer
