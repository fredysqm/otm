from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
#from core.models import Proveedor


#ROOT
class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'

#Mantenimiento
# class app_mantenimiento_proveedores(LoginRequiredMixin, ListView):
#     template_name = 'app/proveedores/main.html'
#     model = Proveedor
#     queryset = Proveedor.objects.select_related().order_by('-id')
#     paginate_by = 50