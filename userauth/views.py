from imaplib import _Authenticator
from application.forms import *
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from .forms import *
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from .views import *
from django.views.generic.edit import *



class SignUpView(CreateView):
  template_name = 'register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


class Login(LoginView):
    template_name = 'login.html'
    fields = ['username','password']


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

class Reset_Pass(PasswordResetView):
    from_email = "hr@sukhtian.com.jo"










