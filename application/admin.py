from cProfile import Profile
from django.shortcuts import render, redirect
from importlib.resources import path
from django.contrib import admin
from application.models import Application 
from admin_auto_filters.filters import AutocompleteFilter
from job.models import *
from decouple import config
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from interview.models import *
from admin_numeric_filter.admin import NumericFilterModelAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .emailmessages import Emessage
import arabic_reshaper

# Register your models here.

class JobFilter(AutocompleteFilter):
    title = 'Job' # display title
    field_name = 'Job_App' # name of the foreign key field



#export and import License_Type
class ApplicationResource(resources.ModelResource):

    class Meta:
        model = Application
        fileds = ('id','Job_App','First_Approval','Second_Approval','Create_Date')
        export_order = ('id''Job_App','First_Approval','Second_Approval','Diseases', 'Create_Date')



class ApplicationAdmin(ImportExportModelAdmin,NumericFilterModelAdmin):
    resource_class = ApplicationResource
    readonly_fields = ('id',)
    list_display = ('id','Job_App' ,'get_Name','get_EXP','get_NID','get_Email','First_Approval','Second_Approval', 'Create_Date','Visit')
    list_filter = ['Job_App','UserProfile_App__NID','UserProfile_App__Qualification__Major','UserProfile_App__Training__Name',
    'Waiting_List','UserProfile_App__Experience_Years','UserProfile_App__Qualification__Degree','UserProfile_App__Qualification__Graduation_Date',
    'First_Approval','Second_Approval', 'Create_Date','Visit']
    search_fields = ['Job_App','Email','Job_App', 'Create_Date','get_NID']
    
    # to get relation data
    @admin.display( ordering='UserProfile_App__NID',description='الرقم الوطني')
    def get_NID(self, obj):
            return obj.UserProfile_App.NID


    @admin.display( ordering='UserProfile_App__Experience_Years',description='سنوات الخبرة ')
    def get_EXP(self, obj):
            return obj.UserProfile_App.Experience_Years


    @admin.display( ordering='UserProfile_App__Name',description='إسم المرشح')
    def get_Name(self, obj):
            return obj.UserProfile_App.Name

    @admin.display( ordering='UserProfile_App__Email',description='البريد ألإلكتروني')
    def get_Email(self, obj):
            return obj.UserProfile_App.Email

    @admin.display( ordering='UserProfile_App__department',description=' القسم')
    def get_Dep(self, obj):
            return Group.objects.get(id = obj.UserProfile_App.department).name
    fieldsets = (
      (' معلومات المتقدم', {
          'fields': ('id',('Job_App','UserProfile_App',))
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
        #bl = list(map(int,Application.objects.filter(Black_List = True).values_list('UserProfile_App__NID',flat=True)))# get all black list national id
        #print(qs.filter(First_Approval = True))
        #record = list(map(int,qs.values_list('UserProfile_App__NID',flat=True)))
   
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
        users = list(User.objects.filter(usertitle__name=job).values_list('id',flat=True)) # get all users related to this job for this job
        dep = request.user.groups.values_list('name',flat = True).first()
        message = Emessage('aref','alhamad','ss','2022','4:5')
        m2 = message.firstinterview()
        
        form = super(ApplicationAdmin, self).get_form(request, obj, **kwargs)
        
        # if current user defined for this job
        form.base_fields["UserProfile_App"].disabled = True
        form.base_fields["Job_App"].disabled = True
        if dep == "HR": 

            form.base_fields["Second_Approval"].disabled = True
            form.base_fields["Second_Approval_Note"].disabled = True
            Application.objects.filter(pk=appid).update(Visit = True)
            

        else:

            form.base_fields["First_Approval"].disabled = True
            form.base_fields["First_Approval_Note"].disabled = True
            form.base_fields["HR_Interview_Approval"].disabled = True
            form.base_fields["Black_List"].disabled = True 
            form.base_fields["Waiting_List"].disabled = True
            

        return form


    def save_form(self, request, form, change):

        profile = form.cleaned_data.get('UserProfile_App')
        job = form.cleaned_data.get('Job_App')
        appid = request.resolver_match.kwargs['object_id']
        applicanetemail = User.objects.filter(userprofile = profile).values_list('email',flat=True)[0] #get email for user
        first_app = form.cleaned_data.get('First_Approval')
        secound_app = form.cleaned_data.get('Second_Approval')
        HR_App = form.cleaned_data.get('HR_Interview_Approval')
        applicant_name = User.objects.filter(userprofile = profile).values_list('username',flat=True)[0] #get email for user
        interview_date_hour = form.cleaned_data.get('Interview_Date').strftime("%H:%M:%S")
        interview_date = form.cleaned_data.get('Interview_Date').strftime("%m/%d/%Y")
        

        loguserlist = []
        appid = request.resolver_match.kwargs['object_id'] # get current application id
        job = Job.objects.filter(JA__id=appid).first() # get current job
        users = list(User.objects.filter(usertitle__name=job).values_list('email',flat=True))# get all users email related to this job for this job
        message = Emessage(str(applicant_name),'',str(job),interview_date,interview_date_hour)
        m2 = message.firstinterview()
        if first_app and secound_app and HR_App :
                    # send email for users and HR
                    subject = 'مقابلة'
                    message = 'رابط المقابلة الساعة '+interview_date_hour+' '+interview_date+' في تاريخ  '+applicant_name+' تم تحدديد مقابلة للسيد '
                    recipient_list = users
                    recipient_list.append('adsa19836@gmail.com')
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
                    subject2 = 'مقابلة'
                    message2 = m2
                    recipient_list2 = [applicanetemail,] #[form.cleaned_data.get('Email')]
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






admin.site.register(Application,ApplicationAdmin)
