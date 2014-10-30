from django.conf.urls import patterns, url
from .views import HomeView, EscuelasView, ConsultaView, EscuelaCicloView, EscuelaPersonalView
from petc.settings import CICLO_ACTUAL

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^escuelas/$', EscuelasView.as_view(), name="escuelas"),
    url(r'^escuelas/(?P<clave>[\w]+)/$', EscuelasView.as_view(), name="escuelas"),
    url(r'^escuelas/ciclo/%i/$' % CICLO_ACTUAL, EscuelaCicloView.as_view(), name="escuela_ciclo"),
    url(r'^consulta/$', ConsultaView.as_view(), name="consulta"),
    url(r'^escuelas/(?P<clave>[\w]+)/detalle-escuela/(?P<escuela>\d+)/$',
        EscuelaPersonalView.as_view(), name="detalle-escuela"),
)
