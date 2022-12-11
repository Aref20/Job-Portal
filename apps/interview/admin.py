from pyexpat import model
from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from django.core.mail.message import EmailMessage
from django.core.mail import get_connection, send_mail, EmailMultiAlternatives
from decouple import config
from apps.application.emailmessages import Emessage
from apps.userprofile.models import *


User = get_user_model()
# Register your models here.


#export and import
class JobResource(resources.ModelResource):
    interview_id = fields.Field(column_name='Interview ID', attribute='id')
    id = fields.Field(column_name='Application Number', attribute='interview_application__UserProfile_App__id')
    department = fields.Field(column_name='Department', attribute='interview_application__department')
    hiring_recommendation = fields.Field(column_name='Hiring Recommendation', attribute='hiring_Recommendation')
    Notes = fields.Field(column_name='Notes', attribute='note')
    HRNotes = fields.Field(column_name='HR_Notes', attribute='HRnote')
    class Meta:
        model = Interview

        fileds = ('interview_application__department',)
        #export_order = ('id','interview_application','interview_application__department','interview_application__Job_App__title','hiring_Recommendation','post_date')
        
        exclude = ('commitment', 'MSG_knowledge','MSG_comp_knowledge','self_exp_skill','eng_lang_skill','body_exp_skill'
        ,'behaviour','listening_skills','asked_q_level','computer_skill',
        'working_experience','management_leading_cap','tech_cap','personality',
        'prev_work_leave','achievements','pros','cons','note','HRcommitment', 'HRMSG_knowledge','HRMSG_comp_knowledge',
        'HRself_exp_skill','HReng_lang_skill','HRbody_exp_skill','HRbehaviour','HRlistening_skills','HRasked_q_level','HRcomputer_skill'
        'HRworking_experience','HRmanagement_leading_cap','HRtech_cap','HRpersonality','HRprev_work_leave','HRachievements','HRpros','HRcons','HRnote',
        'expected_salary','work_time','post_date','HRpost_date','HRworking_experience',
        'HRcomputer_skill','hiring_Recommendation','interview_application','Second_Interview_Time')





class InterviewAdmin(ImportExportActionModelAdmin):
    resource_class = JobResource
    readonly_fields = ('id','interview_application')
    list_display = ('id','get_ID','get_Name','get_NID','get_Email','hiring_Recommendation','expected_salary','work_time','get_Dep','post_date')
    list_filter = ('id','interview_application__UserProfile_App__user__username','interview_application__department__name','Second_Interview_Time','interview_application__Job_App__title','hiring_Recommendation','post_date')
 
    
    # to get relation data
    @admin.display( ordering='interview_application__UserProfile_App__NID',description='الرقم الوطني')
    def get_NID(self, obj):
        return obj.interview_application.UserProfile_App.NID


    @admin.display( ordering='interview_application__UserProfile_App__id',description='رقم الطلب')
    def get_ID(self, obj):
        return obj.interview_application.UserProfile_App.id


    @admin.display( ordering='interview_application__UserProfile_App__user__username',description='إسم المرشح')
    def get_Name(self, obj):
        return obj.interview_application.UserProfile_App.user.username

    @admin.display( ordering='interview_application__UserProfile_App__user__email',description='البريد ألإلكتروني')
    def get_Email(self, obj):
        return obj.interview_application.UserProfile_App.user.email

    @admin.display( ordering='interview_application__department__id',description=' القسم')
    def get_Dep(self, obj):
        return Group.objects.get(id = obj.interview_application.department.id).name




        



    fieldsets = (
  
      (' معلومات المتقدم', {
          'fields': ('interview_application',)
      }),

      (' تقييم رئيس القسم  ', {
          'fields': ( ('commitment', 'MSG_knowledge','MSG_comp_knowledge',),('self_exp_skill','eng_lang_skill','body_exp_skill'),('behaviour','listening_skills','asked_q_level','computer_skill'))
      }),
      (' تعليق رئيس القسم', {
          'fields': (('working_experience','management_leading_cap','tech_cap'),('personality','prev_work_leave','achievements'),('pros','cons','note'))
      }),


      ('التوصية بالتعيين', {
          'fields': ((),('expected_salary','work_time','hiring_Recommendation','Second_Interview_Time'))
      }),

      (' تقييم الموارد البشرية  ', {
          'fields': ( ('HRcommitment', 'HRMSG_knowledge','HRMSG_comp_knowledge',),('HRself_exp_skill','HReng_lang_skill','HRbody_exp_skill'),('HRbehaviour','HRlistening_skills','HRasked_q_level','HRcomputer_skill'))
      }),
      
      (' تعليق الموارد البشرية', {
          'fields': (('HRworking_experience','HRmanagement_leading_cap','HRtech_cap'),('HRpersonality','HRprev_work_leave','HRachievements'),('HRpros','HRcons','HRnote'))
      }),



        
    )


   

    formfield_overrides = {
    #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':30})},
   # models.DateField: {'widget': TextInput(attrs={'size':'100'})},
    #models.IntegerField: {'widget': TextInput(attrs={'size':'50'})},

    }



    def get_queryset(self, request):
        
        qs = super(InterviewAdmin, self).get_queryset(request)
        dep = request.user.groups.values_list('name',flat = True).first()
        depid = request.user.groups.values_list('id',flat = True).first()
   
        #return first approval records only for the department
        if dep == 'HR':
            return qs
        elif dep == 'MANAGEMENT':
            return qs.filter(hiring_Recommendation =  'Second_Interview')
        else:
            return qs.filter(interview_application__department__id = depid)


    def get_form(self, request, obj, **kwargs):
        loguserlist = []
        appid = request.resolver_match.kwargs['object_id'] # get current application id
        loguser = (request.user.id)
        loguserlist.append(loguser)
        job = Job.objects.filter(JA__id=appid).first() # get current job
        users = list(User.objects.filter(usertitle__name=job).values_list('id',flat=True)) # get all users related to thid job for this job
        dep = request.user.groups.values_list('name',flat = True).first()
        
        form = super(InterviewAdmin, self).get_form(request, obj, **kwargs)
        # if current user defind for this job
        if dep == "HR": 

            form.base_fields["working_experience"].disabled = True
            form.base_fields["management_leading_cap"].disabled = True
            form.base_fields["tech_cap"].disabled = True
            form.base_fields["personality"].disabled = True
            form.base_fields["prev_work_leave"].disabled = True
            form.base_fields["achievements"].disabled = True
            form.base_fields["pros"].disabled = True
            form.base_fields["cons"].disabled = True
            form.base_fields["note"].disabled = True
            form.base_fields["commitment"].disabled = True
            form.base_fields["MSG_knowledge"].disabled = True
            form.base_fields["MSG_comp_knowledge"].disabled = True
            form.base_fields["self_exp_skill"].disabled = True
            form.base_fields["eng_lang_skill"].disabled = True
            form.base_fields["body_exp_skill"].disabled = True
            form.base_fields["behaviour"].disabled = True
            form.base_fields["listening_skills"].disabled = True
            form.base_fields["asked_q_level"].disabled = True
            form.base_fields["computer_skill"].disabled = True
 

        else:
            form.base_fields["HRworking_experience"].disabled = True
            form.base_fields["HRmanagement_leading_cap"].disabled = True
            form.base_fields["HRtech_cap"].disabled = True
            form.base_fields["HRpersonality"].disabled = True
            form.base_fields["HRprev_work_leave"].disabled = True
            form.base_fields["HRachievements"].disabled = True
            form.base_fields["HRpros"].disabled = True
            form.base_fields["HRcons"].disabled = True
            form.base_fields["HRnote"].disabled = True
            form.base_fields["HRcommitment"].disabled = True
            form.base_fields["HRMSG_knowledge"].disabled = True
            form.base_fields["HRMSG_comp_knowledge"].disabled = True
            form.base_fields["HRself_exp_skill"].disabled = True
            form.base_fields["HReng_lang_skill"].disabled = True
            form.base_fields["HRbody_exp_skill"].disabled = True
            form.base_fields["HRbehaviour"].disabled = True
            form.base_fields["HRlistening_skills"].disabled = True
            form.base_fields["HRasked_q_level"].disabled = True
            form.base_fields["HRcomputer_skill"].disabled = True

            form.base_fields["expected_salary"].disabled = True
            form.base_fields["work_time"].disabled = True
            form.base_fields["hiring_Recommendation"].disabled = True
            form.base_fields["Second_Interview_Time"].disabled = True

        return form


    def save_model(self, request, obj, form, change):
        applicant = Application.objects.filter(id=obj.interview_application.id).values_list('UserProfile_App',flat=True).first()
        applicantJob = Application.objects.filter(id=obj.interview_application.id).values_list('Job_App',flat=True).first()
        job = Job.objects.filter(id=applicantJob).values_list('title__name',flat=True).first()
        profile = UserProfile.objects.filter(id = applicant).first()
        email = profile.user.email
        name = profile.user.username
        interview_date_hour = form.cleaned_data.get('Second_Interview_Time').strftime("%H:%M:%S")
        interview_date = form.cleaned_data.get('Second_Interview_Time').strftime("%m/%d/%Y")

        message = Emessage(str(name), '', '', '', '')
        message2 = Emessage(str(name), '', job, interview_date, interview_date_hour)
        
        if ( obj.hiring_Recommendation=='Black_List'):
            UserProfile.objects.filter(id = applicant).update(Black_List=True)
 

        # send email for user if rejected
        if ( obj.hiring_Recommendation=='No'):
            subject = 'مقابلة'
            m2 = message.rejectinterview()
            recipient_list = [email] 
            my_host = 'mail.sukhtian.com.jo'
            my_port = 587
            my_username = 'jobs@sukhtian.com.jo'
            my_password =config('EMAILJOBSPASS')
            my_use_tls = True
            connection = get_connection(host=my_host,
                                                        port=my_port, 
                                                        username=my_username, 
                                                        password=my_password, 
                                                        use_tls=my_use_tls) 
            msg = EmailMultiAlternatives(
            subject, m2, my_username, recipient_list, connection=connection)
            msg.attach_alternative(m2, "text/html")
            msg.send()


        # send email for user in second interview
        if ( obj.hiring_Recommendation=='Second_Interview'):
            subject = 'مقابلة'
            m2 = message2.secoundInterview()
            recipient_list = [email] 
            my_host = 'mail.sukhtian.com.jo'
            my_port = 587
            my_username = 'jobs@sukhtian.com.jo'
            my_password =config('EMAILJOBSPASS')
            my_use_tls = True
            connection = get_connection(host=my_host,
                                                        port=my_port, 
                                                        username=my_username, 
                                                        password=my_password, 
                                                        use_tls=my_use_tls) 
            msg = EmailMultiAlternatives(
            subject, m2, my_username, recipient_list, connection=connection)
            msg.attach_alternative(m2, "text/html")
            msg.send()



        if not change:
            obj.created_by = request.user
        obj.save()

#export and import
class GroupResource(resources.ModelResource):

    class Meta:
        model = Group
        fileds = ('id','name',)
        export_order = ('id','name',)
        #exclude = ('id','password','user_permissions', 'date_joined','groups','is_staff','is_active','is_superuser','last_login')

class GroupAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    #change_list_template = "admin/change_list_filter_confirm_sidebar.html"
    resource_class = GroupResource
    readonly_fields = ('id',)
    list_display = ('id','name',)
    list_filter = ('id','name',)
    search_fields = ['id','username',]
    





admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)

admin.site.register(Interview,InterviewAdmin)

