from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import LoginView

from rest_framework import routers
from escuelas.views import EscuelasViewSet, CicloViewSet
from lugares.views import LocalidadViewSet, MunicipioViewSet
from caracteristicas.views import ModalidadViewSet, NivelViewSet
from personal.views import PersonalViewSet, PersonalPorCicloViewSet, NivelEstudioViewSet, EspecialidadViewSet, PuestoViewSet, EstadoViewSet

router = routers.DefaultRouter()
router.register(r'escuelas', EscuelasViewSet)
router.register(r'ciclos', CicloViewSet)
router.register(r'localidades', LocalidadViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'modalidades', ModalidadViewSet)
router.register(r'niveles', NivelViewSet)
router.register(r'personal', PersonalViewSet)
router.register(r'personalxciclo', PersonalPorCicloViewSet)
router.register(r'niveles-estudio', NivelEstudioViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'puestos', PuestoViewSet)
router.register(r'estados', EstadoViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', "petc.views.salir", name="salir"),
    url(r'^', include("escuelas.urls")),
    url(r'^', include("personal.urls")),
    url(r'api/', include(router.urls)),
    url(r'api-auth', include('rest_framework.urls', namespace='rest_framework')),
)
