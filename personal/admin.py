from django.contrib import admin
from .models import Personal, Especialidad, NivelEstudio, Puesto, Estado, PersonalPorCiclo

admin.site.register(Personal)
admin.site.register(Especialidad)
admin.site.register(NivelEstudio)
admin.site.register(Puesto)
admin.site.register(Estado)
admin.site.register(PersonalPorCiclo)
