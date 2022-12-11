
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import *
from apps.application.models import Application
from apps.userprofile.models import UserProfile
from apps.job.models import *
from decouple import config
from apps.job.views import *
from django.core.mail import get_connection, send_mail,EmailMultiAlternatives
from django.core.mail.message import EmailMessage
from django.db import transaction
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from .emailmessages import Emessage
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# send success email for applicatent
subject = 'MSG'
my_host = 'mail.sukhtian.com.jo'
my_port = 587
my_username = 'hr@sukhtian.com.jo'
my_password = config('EMAILPASS')
my_use_tls = True

connection = get_connection(host=my_host, 
                                    port=my_port, 
                                    username=my_username, 
                                    password=my_password, 
                                    use_tls=my_use_tls) 



class ApplicationCreateView(LoginRequiredMixin,CreateView):
    model = Application
    login_url = '/'
    #redirect_field_name = 'redirect_to'
    success_url = '../'
    fields = ['UserProfile_App','Job_App']


    
# set job for application by id
    def dispatch(self, request, *args, **kwargs):
     current_user = self.request.user.id
     self.Job_App = Job.objects.get(pk=kwargs['pk'])
     #self.department = Group.objects.get(id=self.Job_App.department.id)
     if request.user.is_authenticated:
        self.UserProfile_App = UserProfile.objects.get(pk=current_user)
     return super().dispatch(request, *args, **kwargs)

    

    def form_valid(self, form):
     
     form.instance.Job_App_id =self.Job_App.id
     form.instance.department =Group.objects.get(id=self.Job_App.department.id)
     form.instance.UserProfile_App = self.UserProfile_App
     messages.add_message(self.request, messages.SUCCESS,'لقد تم تقديم الطلب بنجاح')
     username = self.UserProfile_App.user.username
     message = Emessage(username,'',"","","")
     m2 = message.welcomemessage()
     # get email from the form
     email = [self.UserProfile_App.user.email]

     msg = EmailMultiAlternatives( subject,m2, my_username, email, connection=connection )
     msg.attach_alternative(m2, "text/html")
     msg.send()
     

     return super().form_valid(form)
     



class CreateViewApplication(View):
    def get(self, request, *args, **kwargs):
         
         view = JobDetailView.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs) :
         view = ApplicationCreateView.as_view()

         return view(request, *args, **kwargs) 










    



