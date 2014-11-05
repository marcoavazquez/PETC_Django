from django.views import generic
from .models import Personal, PersonalPorCiclo, NivelEstudio, Especialidad, Puesto, Estado
from petc.mixins import LoginRequiredMixin


class PersonalView(LoginRequiredMixin, generic.ListView):
    model = Personal
    template_name = "personal/personal.html"

    def get_queryset(self):
        if self.kwargs.get("rfc"):
            queryset = self.model.objects.filter(rfc=self.kwargs['rfc'])
            self.detalle = True
            try:
                rfc = self.model.objects.get(rfc=self.kwargs['rfc'])
                self.q_esc = PersonalPorCiclo.objects.filter(personal=rfc.id)[:1]
            except Personal.DoesNotExist:
                self.q_esc = None

        else:
            queryset = super(PersonalView, self).get_queryset()
            self.detalle = False
            self.q_esc = None
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PersonalView, self).get_context_data(**kwargs)
        detalle = {'detalle': self.detalle, 'schooll': self.q_esc}
        context.update(detalle)

        return context


#API
from rest_framework import viewsets
from serializers import PersonalSerializer, PersonalPorCicloSerializer, NivelEstudioSerializer, EspecialidadSerializer, PuestoSerializer, EstadoSerializer


class PersonalViewSet(viewsets.ModelViewSet):
    model = Personal
    serializer_class = PersonalSerializer


class PersonalPorCicloViewSet(viewsets.ModelViewSet):
    model = PersonalPorCiclo
    serializer_class = PersonalPorCicloSerializer


class NivelEstudioViewSet(viewsets.ModelViewSet):
    model = NivelEstudio
    serializer_class = NivelEstudioSerializer


class EspecialidadViewSet(viewsets.ModelViewSet):
    model = Especialidad
    serializer_class = EspecialidadSerializer


class PuestoViewSet(viewsets.ModelViewSet):
    model = Puesto
    serializer_class = PuestoSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    model = Estado
    serializer_class = EstadoSerializer
