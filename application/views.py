
from faulthandler import disable
import re
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView , FormView
from application.models import Application
from userprofile.models import Profile
from .forms import *
from job.models import *
from django.shortcuts import get_object_or_404
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from decouple import config
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.db import transaction
from django.template import RequestContext
from django.template.response import TemplateResponse

# Create your views here.



def testdex(request, template_name="jazzmin/templates/admin/index.html"):
    args = {}
    text = "hello world"
    args['mytext'] = text
    return TemplateResponse(request, template_name, args)


class ApplicationCreateView(CreateView):#CreateWithInlinesView):
    model = Application
    template_name = 'job_detail.html'
    success_url = '../'


# set job for application by id
    def dispatch(self, request, *args, **kwargs):
     current_user = request.user.id
     self.Job_App = Job.objects.values_list('id').filter(pk=kwargs['job_id'])
     self.department = Job.objects.values_list('department').filter(pk=kwargs['job_id'])
     self.UserProfile_App = Profile.objects.values_list(id).filter(pk=current_user)
     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
     form.instance.Job_App_id =self.Job_App 
     form.instance.department =self.department 
     form.instance.UserProfile_App = self.UserProfile_App
     messages.add_message(self.request, messages.SUCCESS,'لقد تم تقديم الطلب بنجاح')

     # get email from the form
     email = form.cleaned_data['Email'] 

     # send success email for applicatent
     subject = 'welcome to GFG world'
     message = 'Hi aref thank you for registering in geeksforgeeks.'
     #email_from = settings.EMAIL_HOST_USER
     recipient_list = [email, ]
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
     send_mail( subject, message, my_username, recipient_list, connection=connection )
     

     return super().form_valid(form)
        


    def form_invalid(self, form, Qualification_form, Language_Form , Computer_Skill_Form , Application_Previous_Company_Form , Application_Training_Form , Application_Previous_Coworker_Form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        pass











    



