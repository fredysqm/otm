from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


#Root
class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'

#Mantenimiento
class app_proveedor(LoginRequiredMixin, TemplateView):
    template_name = 'app/proveedor/main.html'