
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

# Create your views here.


#@login_required
class Profile(UpdateView):
    template_name = 'profile.html'
    model = UserProfile
    context_object_name = 'form'
    form_class = ProfileForm
    success_url = '/'




    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        if self.request.POST:
            context['Qualification_form'] = ProfileQualificationFormSet(self.request.POST, instance=self.object)
            context['Language_Form'] = ProfileLanguageFormSet(self.request.POST, instance=self.object)
            context['Computer_Skill_Form'] = ProfileComputer_SkillFormSet(self.request.POST, instance=self.object)
            context['Profile_Previous_Company_Form'] = ProfilePrevious_CompanyFormSet(self.request.POST, instance=self.object)
            context['Profile_Training_Form'] = ProfileTrainingFormSet(self.request.POST, instance=self.object)
            context['Profile_Previous_Coworker_Form'] = ProfilePrevious_CoworkerFormSet(self.request.POST, instance=self.object)
        else:
            context['Qualification_form'] = ProfileQualificationFormSet(instance=self.object)
            context['Language_Form'] = ProfileLanguageFormSet( instance=self.object)
            context['Computer_Skill_Form'] = ProfileComputer_SkillFormSet( instance=self.object)
            context['Profile_Previous_Company_Form'] = ProfilePrevious_CompanyFormSet(instance=self.object)
            context['Profile_Training_Form'] = ProfileTrainingFormSet( instance=self.object)
            context['Profile_Previous_Coworker_Form'] = ProfilePrevious_CoworkerFormSet( instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        Qualification_form = context['Qualification_form']
        Language_Form = context['Language_Form']
        Computer_Skill_Form = context['Computer_Skill_Form']
        Profile_Previous_Company_Form = context['Profile_Previous_Company_Form']
        Profile_Training_Form = context['Profile_Training_Form']
        Profile_Previous_Coworker_Form = context['Profile_Previous_Coworker_Form']
        if (Qualification_form.is_valid() and Language_Form.is_valid() and Computer_Skill_Form.is_valid() and \
        Profile_Previous_Company_Form.is_valid() and Profile_Training_Form.is_valid() and Profile_Previous_Coworker_Form.is_valid()):

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
        return self.render_to_response(self.get_context_data(form=form))

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

    ## profile = form.save()
    # user = profile.user
    # user.first_name = form.cleaned_data['first_name']
     #user.username = form.cleaned_data['username']
    # user.email = form.cleaned_data['email']
    # user.save()

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
