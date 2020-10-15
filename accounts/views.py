from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from django.urls import reverse_lazy
from django.views.generic import(
    TemplateView,
)


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    # なんかデータ必要だったら
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "password_change"
        return context


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'password_change_done.html'
