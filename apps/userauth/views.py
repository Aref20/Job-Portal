from imaplib import _Authenticator
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from .forms import *
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from .views import *
from django.views.generic.edit import *
from django.core.exceptions import ValidationError



class SignUpView(CreateView):
  template_name = 'register.html'
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"



  def form_valid(self, form):
        
        #save the new user first
        result = super().form_valid(form)
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return result

  def get_success_url(self):
          return reverse_lazy('apps.userprofile:Profile',args=(self.object.id,))
  




class Login(LoginView):
    template_name = 'login.html'
    fields = ['username','password']


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

class Reset_Pass(PasswordResetView):
    from_email = "hr@sukhtian.com.jo"










