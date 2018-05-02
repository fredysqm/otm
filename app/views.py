from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


#Root
class app_main(LoginRequiredMixin, TemplateView):
    template_name = 'app/main.html'

#Mantenimiento
class app_mantenimiento_pais(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/pais.html'

class app_mantenimiento_ciudad(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/ciudad.html'

class app_mantenimiento_idioma(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/idioma.html'

class app_mantenimiento_moneda(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/moneda.html'

class app_mantenimiento_banco(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/banco.html'

class app_mantenimiento_operador(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/operador.html'

class app_mantenimiento_proveedor(LoginRequiredMixin, TemplateView):
    template_name = 'app/mantenimiento/proveedor.html'