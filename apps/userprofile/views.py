
from .forms import *
from django.contrib.auth.views import *
from .views import *
from .models import *
from django.contrib import messages
from django.core.mail import get_connection, send_mail
from decouple import config
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.


#@login_required
class Profile(UpdateView):
    template_name = 'profile.html'
    model = UserProfile
    context_object_name = 'form'
    form_class = ProfileForm
    

  #  def get_context_data(self, **kwargs) :
        # context =  super().get_context_data(**kwargs)
        # context['User'] = UserForm(instance=self.request.user)
         
        # return context

         


    def get_success_url(self):
        return reverse_lazy('apps.job:jobs')

    def get_object(self):
        return get_object_or_404(UserProfile, pk=self.request.user.id)#self.kwargs.get('pk'))


    

    
    def form_invalid(self, form,Qualification_form,Language_Form,Computer_Skill_Form,Profile_Previous_Company_Form,Profile_Training_Form,Profile_Previous_Coworker_Form,User):
        return self.render_to_response(self.get_context_data(form=form, Qualification_form=Qualification_form
        ,Language_Form=Language_Form,Computer_Skill_Form=Computer_Skill_Form,Profile_Previous_Company_Form=Profile_Previous_Company_Form,
        Profile_Training_Form=Profile_Training_Form,Profile_Previous_Coworker_Form=Profile_Previous_Coworker_Form,User=User))


    def form_valid(self, form,Qualification_form,Language_Form,Computer_Skill_Form,Profile_Previous_Company_Form,Profile_Training_Form,Profile_Previous_Coworker_Form,User):
        messages.add_message(self.request, messages.SUCCESS,' تم تعديل الملف شخصي بنجاح')
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
        User.instance = self.request.user
        User.save()
        return HttpResponseRedirect(self.get_success_url())



    
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        Qualification_form = ProfileQualificationFormSet(self.request.POST, instance=self.object)
        Language_Form = ProfileLanguageFormSet(self.request.POST, instance=self.object)
        Computer_Skill_Form = ProfileComputer_SkillFormSet(self.request.POST, instance=self.object)
        Profile_Previous_Company_Form =ProfilePrevious_CompanyFormSet(self.request.POST, instance=self.object)
        Profile_Training_Form = ProfileTrainingFormSet(self.request.POST, instance=self.object)
        Profile_Previous_Coworker_Form = ProfilePrevious_CoworkerFormSet(self.request.POST, instance=self.object)
        User = UserForm(self.request.POST,instance=self.request.user)

        if (form.is_valid() and Qualification_form.is_valid() 
         and Language_Form.is_valid() and Computer_Skill_Form.is_valid() and Profile_Previous_Company_Form.is_valid()
         and Profile_Training_Form.is_valid() and Profile_Previous_Coworker_Form.is_valid() and User.is_valid()):

          #  bl = list(Profile.objects.filter(Black_List = True).values_list('NID',flat=True))# get all black list national id
          #  nd = form.cleaned_data['NID']
           # if nd in bl: #prevent black list from apply
             #   messages.add_message(self.request, messages.SUCCESS,'لقد تم تقديم الطلب بنجاح')
            #    return HttpResponseRedirect('../')
           # else:
                return self.form_valid(form,Qualification_form,Language_Form,Computer_Skill_Form,Profile_Previous_Company_Form,Profile_Training_Form,Profile_Previous_Coworker_Form,User)
        else:

                return self.form_invalid(form,Qualification_form,Language_Form,Computer_Skill_Form,Profile_Previous_Company_Form,Profile_Training_Form,Profile_Previous_Coworker_Form,User)


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        Qualification_form = ProfileQualificationFormSet(instance=self.object)
        Language_Form = ProfileLanguageFormSet(instance=self.object)
        Computer_Skill_Form = ProfileComputer_SkillFormSet(instance=self.object)
        Profile_Previous_Company_Form =ProfilePrevious_CompanyFormSet( instance=self.object)
        Profile_Training_Form = ProfileTrainingFormSet( instance=self.object)
        Profile_Previous_Coworker_Form = ProfilePrevious_CoworkerFormSet( instance=self.object)
        User = UserForm(instance=self.request.user)
        
        return self.render_to_response(self.get_context_data(form = form,Qualification_form=Qualification_form
        ,Language_Form=Language_Form,Computer_Skill_Form=Computer_Skill_Form,Profile_Previous_Company_Form=Profile_Previous_Company_Form,
        Profile_Training_Form=Profile_Training_Form,Profile_Previous_Coworker_Form=Profile_Previous_Coworker_Form,User = User))