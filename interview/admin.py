from pyexpat import model
from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from import_export import resources
User = get_user_model()
# Register your models here.







class InterviewAdmin(admin.ModelAdmin):

    readonly_fields = ('id','interview_application',)
    list_display = ('id','get_ID','get_Name','get_NID','get_Email','hiring_Recommendation','expected_salary','work_time','get_Dep','post_date')
    list_filter = ('id','interview_application','interview_application__department','hiring_Recommendation','post_date')
    #change_list_template = "admin/change_list_filter_confirm.html"
    #change_list_filter_template = "admin/filter_listing.html"

    # to get relation data
    @admin.display( ordering='interview_application__UserProfile_App__NID',description='الرقم الوطني')
    def get_NID(self, obj):
        return obj.interview_application.UserProfile_App.NID


    @admin.display( ordering='interview_application__UserProfile_App__id',description='رقم الطلب')
    def get_ID(self, obj):
        return obj.interview_application.UserProfile_App.id


    @admin.display( ordering='interview_application__UserProfile_App__Name',description='إسم المرشح')
    def get_Name(self, obj):
        return obj.interview_application.UserProfile_App.Name

    @admin.display( ordering='interview_application__UserProfile_App__Email',description='البريد ألإلكتروني')
    def get_Email(self, obj):
        return obj.interview_application.UserProfile_App.Email

    @admin.display( ordering='interview_application__department',description=' القسم')
    def get_Dep(self, obj):
        return Group.objects.get(id = obj.interview_application.department).name
        
        



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
          'fields': ((),('expected_salary','work_time','hiring_Recommendation'))
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
    #models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':50})},
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
            return qs.filter(interview_application__department = depid)


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

        return form


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

