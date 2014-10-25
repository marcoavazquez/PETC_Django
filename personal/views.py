from django.views import generic
from .models import Personal


class PersonalView(generic.ListView):
    model = Personal
    template_name = "personal/personal.html"

    def get_queryset(self):
        if self.kwargs.get("rfc"):
            queryset = self.model.objects.filter(rfc=self.kwargs['rfc'])
        else:
            queryset = super(PersonalView, self).get_queryset()

        return queryset
