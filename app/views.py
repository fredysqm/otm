from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import MarcaComercial


#Root
class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'

#Mantenimiento
class app_proveedor(LoginRequiredMixin, ListView):
    model = MarcaComercial
    template_name = 'app/proveedor/main.html'