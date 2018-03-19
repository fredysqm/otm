from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


#Root
class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'

#Mantenimiento
class app_mantenimiento_pais(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/pais.html'