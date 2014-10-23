from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.http import HttpResponseRedirect


class LoginView(generic.FormView):

    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/home/"
    form_class.error_messages = {
        'invalid_login': ("Datos incorrectos, intente de nuevo"),
        'inactive': ("This account is inactive."),
    }

    def form_valid(self, form):
        login(self.request, form.user_cache)

        return super(LoginView, self).form_valid(form)


def salir(request):
    logout(request)
    return HttpResponseRedirect("/login/")
