from pyexpat import model
from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
# Register your models here.


class InterviewAdmin(admin.ModelAdmin):

    #readonly_fields = ('interview_application.id',)
    readonly_fields = ('id',)
    list_display = ('id','get_ID','get_Name','get_NID','get_Email','hiring_Recommendation','expected_salary','work_time','post_date')
    list_filter = ('id','interview_application','hiring_Recommendation','post_date')
    change_list_template = "admin/change_list_filter_confirm.html"
    change_list_filter_template = "admin/filter_listing.html"

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
    models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':30})},
    models.DateField: {'widget': TextInput(attrs={'size':'100'})},
    models.IntegerField: {'widget': TextInput(attrs={'size':'100'})},

    }

admin.site.register(Interview,InterviewAdmin)

