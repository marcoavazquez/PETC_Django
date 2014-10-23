from django.shortcuts import render
from django.views import generic
from .models import Escuela


class HomeView(generic.TemplateView):
    template_name = "escuelas/home.html"


class EscuelasView(generic.ListView):
    model = Escuela
    template_name = "escuelas/escuela_list.html"

    def get_queryset(self):
        if self.kwargs.get('clave'):  #variable donde estan lo que se envia por url
            queryset = self.model.objects.filter(clave=self.kwargs['clave'])
        else:
            queryset = super(EscuelasView, self).get_queryset()

        return queryset


class ConsultaView(generic.RedirectView):


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
