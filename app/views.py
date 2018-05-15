from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from core.models import MarcaComercial
from app.forms import ProveedorCrearForm


#Root
class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'

#Mantenimiento
class app_proveedor(LoginRequiredMixin, TemplateView):
    template_name = 'app/proveedor/main.html'