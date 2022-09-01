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
    list_filter = ('id','interview_application','hiring_Recommendation','post_date')
    #change_list_template = "admin/change_list_filter_confirm.html"
    #change_list_filter_template = "admin/filter_listing.html"

    # to get relation data
    @admin.display( ordering='interview_application__NID',description='الرقم الوطني')
    def get_NID(self, obj):
        return obj.interview_application.NID


    @admin.display( ordering='interview_application__id',description='رقم الطلب')
    def get_ID(self, obj):
        return obj.interview_application.id


    @admin.display( ordering='interview_application__Name',description='إسم المرشح')
    def get_Name(self, obj):
        return obj.interview_application.Name

    @admin.display( ordering='interview_application__Email',description='البريد ألإلكتروني')
    def get_Email(self, obj):
        return obj.interview_application.Email

    @admin.display( ordering='interview_application__department',description=' القسم')
    def get_Dep(self, obj):
        return Group.objects.get(id = obj.interview_application.department).name
        
        



    fieldsets = (
      (' معلومات المتقدم', {
          'fields': ('interview_application',)
      }),
      (' مجال التقييم ', {
          'fields': ( ('commitment', 'MSG_knowledge','MSG_comp_knowledge','self_exp_skill','eng_lang_skill'),('body_exp_skill','behaviour','listening_skills','asked_q_level','computer_skill'))
      }),
      (' التعليق', {
          'fields': (('working_experience','management_leading_cap'),('tech_cap','personality'),('prev_work_leave','achievements'),('pros','cons'),('note'),('expected_salary','work_time','hiring_Recommendation'))
      }),
   )


   

    formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':50})},
    models.DateField: {'widget': TextInput(attrs={'size':'100'})},
    models.IntegerField: {'widget': TextInput(attrs={'size':'50'})},

    }

    def get_queryset(self, request):
        
        qs = super(InterviewAdmin, self).get_queryset(request)
        dep = request.user.groups.values_list('name',flat = True).first()
        depid = request.user.groups.values_list('id',flat = True).first()
   
        #return first approval records only for the department
        if dep == 'HR':
            return qs
        else:
            return qs.filter(interview_application__department = depid)




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

