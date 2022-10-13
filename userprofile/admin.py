from django.contrib import admin
from .models import *
from job.models import *
from decouple import config
from interview.models import *
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter
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




#export and import License_Type
class ProfileResource(resources.ModelResource):

    class Meta:
        model = UserProfile
        fileds = ('id','Name', 'NID','Email','Phone_Num', 'Socility_Status','Experience_Years','Birth_Location','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','First_Approval','Second_Approval','Diseases', 'Create_Date')
        export_order = ('id','Name', 'NID','Email','Phone_Num', 'Socility_Status','Experience_Years','Birth_Location','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date','Diseases', 'Create_Date')



class ProfileAdmin(ImportExportModelAdmin,NumericFilterModelAdmin):
    resource_class = ProfileResource
    readonly_fields = ('id','user')
    inlines = [QualificationInline,Computer_SkillInline,Previous_CompanyInline,TrainingInline,Previous_CoworkerInline]#,LanguageInline]
    list_display = ('id','Name','Email','Phone_Num' ,'Socility_Status','Experience_Years','Nationality','Car_License','Have_Car','Current_Salary','Expected_Salary','Available_Date', 'Create_Date')
    list_filter = ['Experience_Years','Name','Have_Car','Car_License','Car_License_Type','Name','Qualification__Major' ,'Qualification__Degree', 'Create_Date']
    search_fields = ['Name', 'NID','Email','Current_Salary' , 'Create_Date']
    

    formfield_overrides = {
    #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #models.DateField: {'widget': TextInput(attrs={'size':'100'})},
    #models.IntegerField: {'widget': TextInput(attrs={'size':'20'})},

    }


    fieldsets = (
      (' معلومات المتقدم', {
          'fields': ('id','user',('Name','NID','Phone_Num',),('Email','Birth_Date','Birth_Location',),('City','Location','Nationality',)
          ,('Have_Car','Car_License'),('Current_Salary','Expected_Salary','Available_Date',)
          ,('Relative_Frinds','Relative_Frinds_Job','Diseases'),('Socility_Status','Coworker_Ask','Car_License_Type',),('Experience_Years','Warranty','resume'))
      }),


      
    )



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
admin.site.register(UserProfile,ProfileAdmin)