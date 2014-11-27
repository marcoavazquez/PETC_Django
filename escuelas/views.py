from django.views import generic
from .models import Escuela, EscuelasPorCiclo, Ciclo
from personal.models import PersonalPorCiclo
from petc.mixins import LoginRequiredMixin


class HomeView(generic.TemplateView):
    template_name = "escuelas/home.html"


class EscuelasView(LoginRequiredMixin, generic.ListView):
    model = Escuela
    template_name = "escuelas/escuela_list.html"

    def get_queryset(self):
        if self.kwargs.get("clave"):
            queryset = self.model.objects.filter(clave=self.kwargs['clave'])
        else:
            queryset = super(EscuelasView, self).get_queryset()

        return queryset


class ConsultaView(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self):
        tipo = self.request.GET.get("tipo-busqueda", None)
        consulta = self.request.GET.get("consulta", None)
        if tipo == "escuela":
            url = "/escuelas/%s" % consulta
        elif tipo == "personal":
            url = "/personal/%s" % consulta
        else:
            url = "/"
        return url


class EscuelaCicloView(LoginRequiredMixin, generic.ListView):
    model = EscuelasPorCiclo
    template_name = "escuelas/escuela_ciclo.html"


class EscuelaPersonalView(LoginRequiredMixin, generic.ListView):
    model = PersonalPorCiclo
    template_name = "escuelas/detalle_escuela.html"

    def get_queryset(self):
        id_escuela = self.kwargs.get("escuela")
        queryset = self.model.objects.filter(escuela=id_escuela)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(EscuelaPersonalView, self).get_context_data(**kwargs)
        datos = self.model.objects.filter(escuela=self.kwargs.get("escuela"))[:1]

        datos_escuela = {
            'schooll': datos
        }

        context.update(datos_escuela)

        return context


class FiltroEscuela(generic.TemplateView):
    template_name = "escuelas/filtro_escuela.html"


#API
from rest_framework import viewsets
from serializers import EscuelaSerializer, CicloSerializer


class EscuelasViewSet(viewsets.ModelViewSet):
    model = Escuela
    serializer_class = EscuelaSerializer


class CicloViewSet(viewsets.ModelViewSet):
    model = Ciclo
    serializer_class = CicloSerializer
