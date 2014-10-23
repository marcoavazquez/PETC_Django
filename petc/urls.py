from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import LoginView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', "petc.views.salir", name="salir"),
    url(r'^', include("escuelas.urls")),
    url(r'^', include("personal.urls")),
)
