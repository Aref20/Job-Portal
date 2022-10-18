
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import *
from application.models import Application
from userprofile.models import UserProfile
from job.models import *
from decouple import config
from job.views import *
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.db import transaction
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from .emailmessages import Emessage
# Create your views here.

# send success email for applicatent
subject = 'welcome to GFG world'
message = 'Hi aref thank you for registering in geeksforgeeks.'
#recipient_list = [email ]
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



class ApplicationCreateView(CreateView):#CreateWithInlinesView):
    model = Application
    #template_name = 'job_detail.html'
    success_url = '../'
    fields = ['UserProfile_App','Job_App']


    
# set job for application by id
    def dispatch(self, request, *args, **kwargs):
     current_user = self.request.user.id
     self.Job_App = Job.objects.values_list('id').filter(pk=kwargs['pk'])
     self.department = Job.objects.values_list('department').filter(pk=kwargs['pk'])
     self.UserProfile_App = UserProfile.objects.get(pk=current_user)
     return super().dispatch(request, *args, **kwargs)

    

    def form_valid(self, form):
     
     form.instance.Job_App_id =self.Job_App 
     form.instance.department =self.department 
     form.instance.UserProfile_App = self.UserProfile_App
     messages.add_message(self.request, messages.SUCCESS,'لقد تم تقديم الطلب بنجاح')
     message = Emessage('aref','alhamad',"","","")
     m2 = message.welcomemessage()
     # get email from the form
     email = [self.UserProfile_App.user.email]

     send_mail( subject,m2, my_username, email, connection=connection )
     

     return super().form_valid(form)
     



class PostCommentView(View):
    def get(self, request, *args, **kwargs):
         
         view = JobDetailView.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs) :
         view = ApplicationCreateView.as_view()

         return view(request, *args, **kwargs) 










    



