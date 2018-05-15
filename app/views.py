from django.views.generic import TemplateView, CreateView
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

class app_proveedor_create(LoginRequiredMixin, CreateView):
    #model = MarcaComercial
    form_class = ProveedorCrearForm
    #fields = ('nombre', 'proveedor', 'categoria_servicio', 'localidad', 'modalidad_pago', 'direccion', 'telefono_fijo', 'telefono_movil', 'email', 'sitio_web', 'observaciones')
    template_name = 'app/proveedor/create.html'
    success_url = reverse_lazy('app_proveedor')