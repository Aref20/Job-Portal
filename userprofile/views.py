from django.shortcuts import render
from imaplib import _Authenticator
from .forms import *
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from .forms import *
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from .views import *
from django.views.generic.edit import *
from .models import *
from django.contrib import messages
from django.core.mail import get_connection, send_mail
from decouple import config
# Create your views here.

class Profile(UpdateView):
    template_name = 'profile.html'
    model = Profile
    form_class = ProfileForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        Qualification_form = ProfileQualificationFormSet()
        Language_Form = ProfileLanguageFormSet()
        Computer_Skill_Form = ProfileComputer_SkillFormSet()
        Profile_Previous_Company_Form =ProfilePrevious_CompanyFormSet()
        Profile_Training_Form = ProfileTrainingFormSet()
        Profile_Previous_Coworker_Form = ProfilePrevious_CoworkerFormSet()
        #instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  Qualification_form=Qualification_form
                                  ,Language_Form=Language_Form
                                  ,Computer_Skill_Form=Computer_Skill_Form
                                  ,Profile_Previous_Company_Form=Profile_Previous_Company_Form
                                  ,Profile_Training_Form=Profile_Training_Form
                                  ,Profile_Previous_Coworker_Form=Profile_Previous_Coworker_Form
                                  ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        Qualification_form = ProfileQualificationFormSet(self.request.POST)
        Language_Form = ProfileLanguageFormSet(self.request.POST)
        Computer_Skill_Form = ProfileComputer_SkillFormSet(self.request.POST)
        Profile_Previous_Company_Form =ProfilePrevious_CompanyFormSet(self.request.POST)
        Profile_Training_Form = ProfileTrainingFormSet(self.request.POST)
        Profile_Previous_Coworker_Form = ProfilePrevious_CoworkerFormSet(self.request.POST)

        if (form.is_valid() and Qualification_form.is_valid() 
         and Language_Form.is_valid() and Computer_Skill_Form.is_valid() and Profile_Previous_Company_Form.is_valid()
         and Profile_Training_Form.is_valid() and Profile_Previous_Coworker_Form.is_valid()):

          #  bl = list(Profile.objects.filter(Black_List = True).values_list('NID',flat=True))# get all black list national id
          #  nd = form.cleaned_data['NID']
           # if nd in bl: #prevent black list from apply
             #   messages.add_message(self.request, messages.SUCCESS,'لقد تم تقديم الطلب بنجاح')
            #    return HttpResponseRedirect('../')
           # else:
                return self.form_valid(form, Qualification_form , Language_Form , Computer_Skill_Form , Profile_Previous_Company_Form , Profile_Training_Form , Profile_Previous_Coworker_Form)
        else:

            return self.form_invalid(form, Qualification_form , Language_Form , Computer_Skill_Form , Profile_Previous_Company_Form , Profile_Training_Form , Profile_Previous_Coworker_Form)



    def form_valid(self, form,Qualification_form, Language_Form , Computer_Skill_Form , Profile_Previous_Company_Form , Profile_Training_Form , Profile_Previous_Coworker_Form):
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
     
     
     # add formset
     self.object = form.save()
     Qualification_form.instance = self.object
     Qualification_form.save()
     Language_Form.instance = self.object
     Language_Form.save()
     Computer_Skill_Form.instance = self.object
     Computer_Skill_Form.save()
     Profile_Previous_Company_Form.instance = self.object
     Profile_Previous_Company_Form.save()
     Profile_Training_Form.instance = self.object
     Profile_Training_Form.save()
     Profile_Previous_Coworker_Form.instance = self.object
     Profile_Previous_Coworker_Form.save()

     return super().form_valid(form)
        


    def form_invalid(self, form, Qualification_form, Language_Form , Computer_Skill_Form , Profile_Previous_Company_Form , Profile_Training_Form , Profile_Previous_Coworker_Form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form
            ,Qualification_form=Qualification_form
            ,Language_Form=Language_Form
            ,Computer_Skill_Form=Computer_Skill_Form
            ,Profile_Previous_Company_Form=Profile_Previous_Company_Form
            ,Profile_Training_Form=Profile_Training_Form
            ,Profile_Previous_Coworker_Form=Profile_Previous_Coworker_Form

            ))
