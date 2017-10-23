from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'
