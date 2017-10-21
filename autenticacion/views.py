from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


class autenticacion_login(auth_views.LoginView):
    template_name = 'autenticacion/login.html'
    redirect_authenticated_user = True

class autenticacion_logut(auth_views.LogoutView):
    template_name = 'autenticacion/logout.html'

class autenticacion_password_change(auth_views.PasswordChangeView):
    success_url = reverse_lazy('autenticacion_password_change_done')
    template_name = 'autenticacion/password_change_form.html'

class autenticacion_password_change_done(auth_views.PasswordChangeDoneView):
    template_name = 'autenticacion/password_change_done.html'