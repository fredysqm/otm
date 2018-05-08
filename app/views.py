from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from core.models import MarcaComercial


#Root
class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'

#Mantenimiento
class app_proveedor(LoginRequiredMixin, ListView):
    model = MarcaComercial
    template_name = 'app/proveedor/view.html'

class app_proveedor_update(LoginRequiredMixin, UpdateView):
    model = MarcaComercial
    fields = ('nombre', 'proveedor', 'categoria_servicio', 'localidad', 'modalidad_pago', 'direccion', 'telefono_fijo', 'telefono_movil', 'email', 'sitio_web', 'observaciones')
    template_name = 'app/proveedor/update.html'
    success_url = reverse_lazy('app_proveedor')