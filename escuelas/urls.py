from django.conf.urls import patterns, url
from .views import HomeView, EscuelasView, ConsultaView
urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^escuelas/$', EscuelasView.as_view(), name="escuelas"),
    url(r'^escuelas/(?P<clave>[\W\w]+)/$', EscuelasView.as_view(), name="escuelas"),
    url(r'^consulta/$', ConsultaView.as_view(), name="consulta"),
)
