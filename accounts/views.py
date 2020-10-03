from django.contrib.auth.mixins import LoginRequiredMixin

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
