from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


class xauth_login(auth_views.LoginView):
    template_name = 'xauth/login.html'
    redirect_authenticated_user = True

class xauth_logut(auth_views.LogoutView):
    template_name = 'xauth/logout.html'

class xauth_password_change(auth_views.PasswordChangeView):
    success_url = reverse_lazy('xauth_password_change_done')
    template_name = 'xauth/password_change_form.html'

class xauth_password_change_done(auth_views.PasswordChangeDoneView):
    template_name = 'xauth/password_change_done.html'