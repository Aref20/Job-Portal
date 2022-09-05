from django.shortcuts import render, redirect
from importlib.resources import path
from django.contrib import admin
from application.models import Application ,Qualification
from admin_auto_filters.filters import AutocompleteFilter
from job.models import *
from decouple import config
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from interview.models import *
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter
from django.forms import TextInput, Textarea
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.


class QualificationInline(admin.TabularInline):
    extra = 0
    model = Qualification

class LanguageInline(admin.TabularInline):
    extra = 0
    model = Language

class Computer_SkillInline(admin.TabularInline):
    extra = 0
    model = Computer_Skill

class Previous_CompanyInline(admin.StackedInline):
    extra = 0
    model = Previous_Company

class TrainingInline(admin.TabularInline):
    extra = 0
    model = Training

class Previous_CoworkerInline(admin.TabularInline):
    extra = 0
    model =  Previous_Coworker



class QualificationInlineForm(admin.TabularInline):
    extra = 0
    model = Qualification_Form

class LanguageInlineForm(admin.TabularInline):
    extra = 0
    model = Language_Form

class Computer_SkillInlineForm(admin.TabularInline):
    extra = 0
    model = Computer_Skill_Form

class Previous_CompanyInlineForm(admin.StackedInline):
    extra = 0
    model = Previous_Company_Form

class TrainingInlineForm(admin.TabularInline):
    extra = 0
    model = Training_Form

class Previous_CoworkerInlineForm(admin.TabularInline):
    extra = 0
    model =  Previous_Coworker_Form

   


class JobFilter(AutocompleteFilter):
    title = 'Job' # display title
    field_name = 'Job_App' # name of the foreign key field


#export and import License_Type
class ApplicationResource(resources.ModelResource):

    class Meta:
        model = Application
        fileds = ('id','Name', 'NID','Email','Phone_Num','Job_App' ,'Socility_Status','Experience_Years','Birth_Location','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','First_Approval','Second_Approval','Diseases', 'Create_Date')
        export_order = ('id','Name', 'NID','Email','Phone_Num','Job_App' ,'Socility_Status','Experience_Years','Birth_Location','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','First_Approval','Second_Approval','Diseases', 'Create_Date')



class ApplicationAdmin(ImportExportModelAdmin,NumericFilterModelAdmin):
    resource_class = ApplicationResource
    readonly_fields = ('id',)
    inlines = [QualificationInline,LanguageInline,Computer_SkillInline,Previous_CompanyInline,TrainingInline,Previous_CoworkerInline]
    list_display = ('id','Name','Email','Phone_Num','Job_App' ,'Socility_Status','Experience_Years','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','First_Approval','Second_Approval', 'Create_Date','Visit')
    list_filter = ['Job_App','Experience_Years','Name','Have_Car','Car_License','Car_License_Type','Name','Qualification__Major' ,'Qualification__Degree','Visit', 'Create_Date']
    search_fields = ['Job_App','Name', 'NID','Email','Job_App','Current_Salary' , 'Create_Date']
    
    #change_list_template = "admin/change_list_filter_confirm.html"
    #change_list_filter_template = "admin/filter_listing.html"

    formfield_overrides = {
    #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #models.DateField: {'widget': TextInput(attrs={'size':'100'})},
    #models.IntegerField: {'widget': TextInput(attrs={'size':'20'})},

    }


    fieldsets = (
      (' معلومات المتقدم', {
          'fields': ('id',('Name','NID','Phone_Num',),('Email','Birth_Date','Birth_Location',),('City','Location','Nationality',)
          ,('Have_Car','Car_License','Job_App'),('Current_Salary','Expected_Salary','Available_Date',)
          ,('Relative_Frinds','Relative_Frinds_Job','Diseases'),('Socility_Status','Coworker_Ask','Car_License_Type',),('Experience_Years','Warranty','resume'))
      }),


      

      (' ملاحظات الموارد البشرية ', {
          'fields': ('First_Approval','First_Approval_Note')
      }),

      (' ملاحظات  رئيس القسم ', {
          'fields': ('Second_Approval','Second_Approval_Note','Interview_Date')
      }),


      ('موافقة الموارد البشرية ', {
          'fields': ('HR_Interview_Approval','Black_List','Waiting_List')
      }),
    )




    
    def get_queryset(self, request):
        
        qs = super(ApplicationAdmin, self).get_queryset(request)
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        depid = request.user.groups.values_list('id',flat = True).first()
        bl = list(map(int,Application.objects.filter(Black_List = True).values_list('NID',flat=True)))# get all black list national id
        record = list(map(int,qs.values_list('NID',flat=True)))
   
        #return first approval records only for the department
        if dep == 'HR':
            return qs
        else:
            qs2 = qs.filter(First_Approval = True) # show only first approvel and related department
            return qs2.filter(department = depid)

        



    def get_form(self, request, obj, **kwargs):
     #if self.pk is None:
        loguserlist = []
        appid = request.resolver_match.kwargs['object_id'] # get current application id
        loguser = (request.user.id)
        loguserlist.append(loguser)
        job = Job.objects.filter(JA__id=appid).first() # get current job
        users = list(User.objects.filter(usertitle__name=job).values_list('id',flat=True)) # get all users related to thid job for this job
        dep = request.user.groups.values_list('name',flat = True).first()
        
        form = super(ApplicationAdmin, self).get_form(request, obj, **kwargs)
        # if current user defind for this job
        if dep == "HR": 

        #    form.base_fields["Second_Approval"].disabled = True
        #    form.base_fields["Second_Approval_Note"].disabled = True
             Application.objects.filter(pk=appid).update(Visit = True)
            

        #else:

        #    form.base_fields["First_Approval"].disabled = True
        #    form.base_fields["First_Approval_Note"].disabled = True
        #    form.base_fields["HR_Interview_Approval"].disabled = True
        #    form.base_fields["Black_List"].disabled = True 
        #    form.base_fields["Waiting_List"].disabled = True 

        return form


    def save_form(self, request, form, change):
        appid = request.resolver_match.kwargs['object_id']
        first_app = form.cleaned_data.get('First_Approval')
        secound_app = form.cleaned_data.get('Second_Approval')
        HR_App = form.cleaned_data.get('HR_Interview_Approval')
        applicant_name = form.cleaned_data.get('Name')
        interview_date_hour = form.cleaned_data.get('Interview_Date').strftime("%H:%M:%S")
        interview_date = form.cleaned_data.get('Interview_Date').strftime("%m/%d/%Y")
        

        loguserlist = []
        appid = request.resolver_match.kwargs['object_id'] # get current application id
        job = Job.objects.filter(JA__id=appid).first() # get current job
        users = list(User.objects.filter(usertitle__name=job).values_list('email',flat=True))
        if first_app and secound_app and HR_App :
                    # send email for users and HR
                    subject = 'مقابلة'
                    message = 'رابط المقابلة الساعة '+interview_date_hour+' '+interview_date+' في تاريخ  '+applicant_name+' تم تحدديد مقابلة للسيد '
                    recipient_list = users
                    #recipient_list.append('hr@sukhtian.com.jo')
                    my_host = 'mail.sukhtian.com.jo'
                    my_port = 587
                    my_username = 'jobs@sukhtian.com.jo'
                    my_password = config('EMAILJOBSPASS')
                    my_use_tls = True
                    connection = get_connection(host=my_host, 
                                                    port=my_port, 
                                                    username=my_username, 
                                                    password=my_password, 
                                                    use_tls=my_use_tls) 
                    EmailMessage( subject, message, my_username, recipient_list, connection=connection ).send(fail_silently=False)


                    # send email for applicanet
                    subject2 = 'welcome to GFG world'
                    message2 = 'Hبيليلي.'
                    recipient_list2 = [form.cleaned_data.get('Email')]
                    my_host2 = 'mail.sukhtian.com.jo'
                    my_port2 = 587
                    my_username2 = 'hr@sukhtian.com.jo'
                    my_password2 = config('EMAILPASS')
                    my_use_tls2 = True
                    connection2 = get_connection(host=my_host2, 
                                                    port=my_port2, 
                                                    username=my_username2, 
                                                    password=my_password2, 
                                                    use_tls=my_use_tls2) 
                    EmailMessage( subject2, message2, my_username2, recipient_list2, connection=connection2 ).send(fail_silently=False)



                    i = Interview(interview_application=Application.objects.get(id=appid))
                    i.save()
        return super().save_form(request, form, change)





#export and import License_Type
class ApplicationFormResource(resources.ModelResource):

    class Meta:
        model = Application_Form
        fileds = ('id','Name', 'NID','Email','Phone_Num' ,'Socility_Status','Experience_Years','Birth_Location','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','First_Approval','Second_Approval','Diseases', 'Create_Date')
        export_order = ('id','Name', 'NID','Email','Phone_Num' ,'Socility_Status','Experience_Years','Birth_Location','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','First_Approval','Second_Approval','Diseases', 'Create_Date')



class ApplicationFormAdmin(ImportExportModelAdmin,NumericFilterModelAdmin):
    resource_class = ApplicationFormResource
    readonly_fields = ('id',)
    inlines = [QualificationInlineForm,LanguageInlineForm,Computer_SkillInlineForm,Previous_CompanyInlineForm,TrainingInlineForm,Previous_CoworkerInlineForm]
    list_display = ('id','Name','Email','Phone_Num' ,'Socility_Status','Experience_Years','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','First_Approval','Second_Approval', 'Create_Date','Visit')
    list_filter = ['Experience_Years','Name','Have_Car','Car_License','Car_License_Type','Name','Qualification__Major' ,'Qualification__Degree','Visit', 'Create_Date']
    search_fields = ['Name', 'NID','Email','Current_Salary' , 'Create_Date']
    #change_list_template = "admin/change_list_filter_confirm.html"
    #change_list_filter_template = "admin/filter_listing.html"

    formfield_overrides = {
    #models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    #models.DateField: {'widget': TextInput(attrs={'size':'100'})},
    #models.IntegerField: {'widget': TextInput(attrs={'size':'100'})},

    }


    fieldsets = (
      (' معلومات المتقدم', {
          'fields': ('id',('Name','NID','Phone_Num','Email'),('Birth_Date','Birth_Location','City','Location',)
          ,('Nationality','Have_Car','Car_License','Experience_Years'),('Current_Salary','Expected_Salary','Available_Date','Socility_Status')
          ,('Relative_Frinds','Relative_Frinds_Job','Diseases',),('Coworker_Ask','Car_License_Type','resume',))
      }),


      

      (' ملاحظات الموارد البشرية ', {
          'fields': ('First_Approval','First_Approval_Note')
      }),

      (' ملاحظات  رئيس القسم ', {
          'fields': ('Second_Approval','Second_Approval_Note','Interview_Date','HR_Interview_Approval','Black_List','Waiting_List')
      }),
    )




    
    def get_queryset(self, request):

        qs = super(ApplicationFormAdmin, self).get_queryset(request)
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        #bl = list(map(int,ApplicationFormAdmin.objects.filter(Black_List = True).values_list('NID',flat=True)))# get all black list national id
        #record = list(map(int,qs.values_list('NID',flat=True) ))

        #return first approval records only for the department
        if dep == 'HR':
            return qs   
        else:
            return qs.filter(First_Approval = True)


        

    def get_form(self, request, obj, **kwargs):

        dep = request.user.groups.values_list('name',flat = True).first()
        
        form = super(ApplicationFormAdmin, self).get_form(request, obj, **kwargs)
        # if current user defind for this job
        if dep == "HR": 

            form.base_fields["Second_Approval"].disabled = True
            form.base_fields["Second_Approval_Note"].disabled = True
        else:
            form.base_fields["First_Approval"].disabled = True
            form.base_fields["First_Approval_Note"].disabled = True
            form.base_fields["HR_Interview_Approval"].disabled = True
            form.base_fields["Black_List"].disabled = True 
            form.base_fields["Waiting_List"].disabled = True 

        return form



    def save_form(self, request, form, change):
        appid = request.resolver_match.kwargs['object_id']
        first_app = form.cleaned_data.get('First_Approval')
        secound_app = form.cleaned_data.get('Second_Approval')
        HR_App = form.cleaned_data.get('HR_Interview_Approval')
        applicant_name = form.cleaned_data.get('Name')
        interview_date_hour = form.cleaned_data.get('Interview_Date').strftime("%H:%M:%S")
        interview_date = form.cleaned_data.get('Interview_Date').strftime("%m/%d/%Y")

        loguserlist = []
        appid = request.resolver_match.kwargs['object_id'] # get current application id
       # job = Job.objects.filter(JA__id=appid).first() # get current job
       # users = list(User.objects.filter(usertitle__name=job).values_list('email',flat=True))
        if first_app and secound_app and HR_App :
                    # send email for users and HR
                    subject = 'مقابلة'
                    message = 'رابط المقابلة الساعة '+interview_date_hour+' '+interview_date+' في تاريخ  '+applicant_name+' تم تحدديد مقابلة للسيد '
                    recipient_list = 'd@t.com'
                    #recipient_list.append('hr@sukhtian.com.jo')
                    my_host = 'mail.sukhtian.com.jo'
                    my_port = 587
                    my_username = 'jobs@sukhtian.com.jo'
                    my_password = config('EMAILJOBSPASS')
                    my_use_tls = True
                    connection = get_connection(host=my_host, 
                                                    port=my_port, 
                                                    username=my_username, 
                                                    password=my_password, 
                                                    use_tls=my_use_tls) 
                    EmailMessage( subject, message, my_username, recipient_list, connection=connection ).send(fail_silently=False)


                    # send email for applicanet
                    subject2 = 'welcome to GFG world'
                    message2 = 'Hبيليلي.'
                    recipient_list2 = [form.cleaned_data.get('Email')]
                    my_host2 = 'mail.sukhtian.com.jo'
                    my_port2 = 587
                    my_username2 = 'hr@sukhtian.com.jo'
                    my_password2 = config('EMAILPASS')
                    my_use_tls2 = True
                    connection2 = get_connection(host=my_host2, 
                                                    port=my_port2, 
                                                    username=my_username2, 
                                                    password=my_password2, 
                                                    use_tls=my_use_tls2) 
                    EmailMessage( subject2, message2, my_username2, recipient_list2, connection=connection2 ).send(fail_silently=False)



                  #  i = Interview(interview_application=Application.objects.get(id=appid))
                  #  i.save()
        return super().save_form(request, form, change)






#export and import License_Type
class License_TypeResource(resources.ModelResource):

    class Meta:
        model = License_Type
        fileds = ('id','Name')
        export_order = ('id','Name')

class License_Typeadmin(ImportExportModelAdmin, admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = License_TypeResource
    readonly_fields = ('id',)
    list_display = ('id','Name')
    list_filter = ('id','Name')
    search_fields = ['id','Name']




admin.site.register(License_Type,License_Typeadmin)
admin.site.register(Application_Form,ApplicationFormAdmin)
admin.site.register(Application,ApplicationAdmin)
#admin.site.register(Qualification)