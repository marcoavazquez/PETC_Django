from django.contrib import admin
from .models import Escuela, Ciclo, EscuelasPorCiclo

admin.site.register(Escuela)
admin.site.register(Ciclo)
admin.site.register(EscuelasPorCiclo)
