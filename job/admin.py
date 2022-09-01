from django.contrib import admin
from job.models import *
from decouple import config
from django.core.mail import get_connection, send_mail
from django_summernote.admin import SummernoteModelAdmin
from django.core.mail.message import EmailMessage
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.forms import TextInput, Textarea
# Register your models here.

#class Department_Personline(admin.TabularInline):
   # model = Department_Person

#export and import
class JobResource(resources.ModelResource):

    class Meta:
        model = Job
        fileds = ('id','title','department','nature','salary','experience_min','experience_max','location','vacancy','Education__name','status', 'expiration_date','post_date')
        export_order = ('id','title','department','nature','salary','experience_min','experience_max','location','vacancy','Education','status', 'expiration_date','post_date')


class jobadmin(ImportExportModelAdmin,SummernoteModelAdmin , admin.ModelAdmin):
    # displaying posts with title slug and created time
    
    resource_class = JobResource
    #change_list_template = "admin/change_list_filter_confirm.html"
    readonly_fields = ('id',)
    list_display = ('id','title','department','nature','salary','experience_min','experience_max','location','vacancy','Education','status', 'expiration_date','post_date')
    list_filter = ('id','title','department','nature','salary','experience_min','experience_max','location','vacancy','Education','status', 'expiration_date','post_date')
    search_fields = ['title']
    summernote_fields = ('description', 'required_competencies','other')

    fieldsets = (
      ('ألإسم والوصف', {
          'fields': ('id',('title'))
      }),
      ('معلومات الوظيفة ', {
          'fields': (('department','Education'), ('salary', 'vacancy','nature'),('experience_min','experience_max','location'),('status','expiration_date','Career_Level','langs'))
      }),

        ('المهارات المطلوبة ', {
          'fields': ((),('required_competencies','other'))
      }),
   )

    formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size':'50'})},
 
    models.IntegerField: {'widget': TextInput(attrs={'size':'50'})},

    }

    
    def get_form(self, request, obj, **kwargs):
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        

        form = super(jobadmin, self).get_form(request, obj, **kwargs)

        #Each user apply for his group and disable fields if not HR
        if not(dep=='HR'):
            form.base_fields["department"].queryset =  request.user.groups
            form.base_fields["title"].queryset = Title.objects.filter(department__name = dep)
            form.base_fields["status"].disabled = True
            form.base_fields["expiration_date"].disabled = True
        return form



    def save_form(self, request, form, change):
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        
        # send email for HR if not HR and on insert
        if (not (dep=='HR') and not(change)):
            subject = 'New Job'
            message = ""+user+" from "+dep+" department request new job"
            recipient_list = ['paypal31877@yahoo.com']
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
            EmailMessage( subject, message, my_username, recipient_list, connection=connection ).send(fail_silently=False)


        return super().save_form(request, form, change)



#export and import Career_Level
class Career_LevelResource(resources.ModelResource):

    class Meta:
        model = Career_Level
        fileds = ('id','level',)
        export_order = ('id','level',)

class Career_Leveladmin(ImportExportModelAdmin, admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = Career_LevelResource
    readonly_fields = ('id',)
    list_display = ('id','level',)
    list_filter = ('id','level',)
    search_fields = ['id','level',]



#export and import TitleResource
class TitleResource(resources.ModelResource):

    class Meta:
        model = Title
        fileds = ('id','name','department')
        export_order = ('id','name','department')

class Titleadmin(ImportExportModelAdmin, admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = TitleResource
    readonly_fields = ('id',)
    list_display = ('id','name','department')
    list_filter = ('id','name','department')
    search_fields = ['id','name','department']


    def get_queryset(self, request):
        
        qs = super(Titleadmin, self).get_queryset(request)
        dep = request.user.groups.values_list('name',flat = True).first()
        depid = request.user.groups.values_list('id',flat = True).first()
   
        #return first approval records only for the department
        if dep == 'HR':
            return qs
        else:
            return qs.filter(department = depid)



#export and import Nature
class NatureResource(resources.ModelResource):

    class Meta:
        model = Nature
        fileds = ('id','Nature_name')
        export_order = ('id','Nature_name')

class Natureadmin(ImportExportModelAdmin, admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = NatureResource
    readonly_fields = ('id',)
    list_display = ('id','Nature_name')
    list_filter = ('id','Nature_name')
    search_fields = ['id','Nature_name']




#export and import Location
class NatureResource(resources.ModelResource):

    class Meta:
        model = Location
        fileds = ('id','location_name')
        export_order = ('id','location_name')

class Locationadmin(ImportExportModelAdmin, admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = NatureResource
    readonly_fields = ('id',)
    list_display = ('id','location_name')
    list_filter = ('id','location_name')
    search_fields = ['id','location_name']



#export and import Language
class LanguageResource(resources.ModelResource):

    class Meta:
        model = Language
        fileds = ('id','name')
        export_order = ('id','name')

class Languageadmin(ImportExportModelAdmin, admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = NatureResource
    readonly_fields = ('id',)
    list_display = ('id','name')
    list_filter = ('id','name')
    search_fields = ['id','name']





#export and import Degree
class DegreeResource(resources.ModelResource):

    class Meta:
        model = Degree
        fileds = ('id','name')
        export_order = ('id','name')

class Degreeadmin(ImportExportModelAdmin, admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = DegreeResource
    readonly_fields = ('id',)
    list_display = ('id','name')
    list_filter = ('id','name')
    search_fields = ['id','name']



    

    


  
admin.site.register(Job, jobadmin)
admin.site.register(Location,Locationadmin)
admin.site.register(Nature,Natureadmin)
admin.site.register(Title,Titleadmin)
admin.site.register(Language,Languageadmin)
admin.site.register(Degree,Degreeadmin)
admin.site.register(Career_Level,Career_Leveladmin)


#admin.site.register(Department,DepartmentPersonadmin)


