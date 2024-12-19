from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext, gettext_lazy
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    success_message = gettext_lazy("You are logged in")
    extra_context = {
        "title": gettext("Entrance"),
        "button_text": gettext("Enter"),
    }

    def get_success_url(self):
        return reverse_lazy("home")


class LogoutUser(LogoutView):
    next_page = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)
