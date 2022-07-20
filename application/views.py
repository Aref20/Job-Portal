
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView , FormView
from application.models import Application,Qualification
from .forms import *
from job.models import Job
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



# Create your views here.


#class QualificationInline(InlineFormSetFactory):
 #   model = Qualification
 #   fields = '__all__'

class ApplicationCreateView(CreateView):#CreateWithInlinesView):
    model = Application
    #inlines = [QualificationInline,]
    #fields = '__all__'
    template_name = 'apply.html'
    success_url = '../'
    form_class = ApplicationForm



    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        Qualification_form = ApplicationQualificationFormSet(prefix='Qualification_form')
        Language_Form = ApplicationLanguageFormSet()
        Computer_Skill_Form = ApplicationComputer_SkillFormSet()
        Application_Previous_Company_Form =ApplicationPrevious_CompanyFormSet()
        Application_Training_Form = ApplicationTrainingFormSet()
        Application_Previous_Coworker_Form = ApplicationPrevious_CoworkerFormSet()
        #instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  Qualification_form=Qualification_form
                                  ,Language_Form=Language_Form
                                  ,Computer_Skill_Form=Computer_Skill_Form
                                  ,Application_Previous_Company_Form=Application_Previous_Company_Form
                                  ,Application_Training_Form=Application_Training_Form
                                  ,Application_Previous_Coworker_Form=Application_Previous_Coworker_Form
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
        Qualification_form = ApplicationQualificationFormSet(self.request.POST,prefix='Qualification_form')
        Language_Form = ApplicationLanguageFormSet(self.request.POST)
        Computer_Skill_Form = ApplicationComputer_SkillFormSet(self.request.POST)
        Application_Previous_Company_Form =ApplicationPrevious_CompanyFormSet(self.request.POST)
        Application_Training_Form = ApplicationTrainingFormSet(self.request.POST)
        Application_Previous_Coworker_Form = ApplicationPrevious_CoworkerFormSet(self.request.POST)
        if (form.is_valid() and Qualification_form.is_valid() 
         and Language_Form.is_valid() and Computer_Skill_Form.is_valid() and Application_Previous_Company_Form.is_valid()
         and Application_Training_Form.is_valid() and Application_Previous_Coworker_Form.is_valid()
        ):
            return self.form_valid(form, Qualification_form , Language_Form , Computer_Skill_Form , Application_Previous_Company_Form , Application_Training_Form , Application_Previous_Coworker_Form)
        else:
            print(Language_Form.get_form_error() )
            return self.form_invalid(form, Qualification_form , Language_Form , Computer_Skill_Form , Application_Previous_Company_Form , Application_Training_Form , Application_Previous_Coworker_Form)

   # def get_context_data(self, **kwargs):
    #    data = super(ApplicationCreateView, self).get_context_data(**kwargs)
   ##        data['titles'] = ApplicationQualificationFormSet(self.request.POST)
     #   else:
    #        data['titles'] = ApplicationQualificationFormSet()
    #    return data


# set job for application by id
    def dispatch(self, request, *args, **kwargs):
     self.Job_App = Job.objects.values_list('id').filter(pk=kwargs['job_id'])
     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form,Qualification_form, Language_Form , Computer_Skill_Form , Application_Previous_Company_Form , Application_Training_Form , Application_Previous_Coworker_Form):
     form.instance.Job_App_id =self.Job_App 
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
     Application_Previous_Company_Form.instance = self.object
     Application_Previous_Company_Form.save()
     Application_Training_Form.instance = self.object
     Application_Training_Form.save()
     Application_Previous_Coworker_Form.instance = self.object
     Application_Previous_Coworker_Form.save()

     #return HttpResponseRedirect(self.get_success_url())
     return super().form_valid(form)

     #return super().form_valid(form)

    def form_invalid(self, form, Qualification_form, Language_Form , Computer_Skill_Form , Application_Previous_Company_Form , Application_Training_Form , Application_Previous_Coworker_Form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form
            ,Qualification_form=Qualification_form
            ,Language_Form=Language_Form
            ,Computer_Skill_Form=Computer_Skill_Form
            ,Application_Previous_Company_Form=Application_Previous_Company_Form
            ,Application_Training_Form=Application_Training_Form
            ,Application_Previous_Coworker_Form=Application_Previous_Coworker_Form

            ))







    



