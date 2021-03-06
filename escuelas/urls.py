from django.conf.urls import patterns, url
from .views import HomeView, EscuelasView, ConsultaView, EscuelaCicloView, EscuelaPersonalView, FiltroEscuela
from petc.settings import CICLO_ACTUAL
from rest_framework import routers

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^escuelas/$', EscuelasView.as_view(), name="escuelas"),
    url(r'^escuelas/(?P<clave>[\w]+)/$', EscuelasView.as_view(), name="escuelas"),
    url(r'^escuelas/ciclo/%i/$' % CICLO_ACTUAL, EscuelaCicloView.as_view(), name="escuela_ciclo"),
    url(r'^consulta/$', ConsultaView.as_view(), name="consulta"),
    url(r'^escuelas/(?P<clave>[\w]+)/detalle-escuela/(?P<escuela>\d+)/$',
        EscuelaPersonalView.as_view(), name="detalle-escuela"),
    url(r'^filtrar/', FiltroEscuela.as_view(), name="filtro_escuela"),
)
