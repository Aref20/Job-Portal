from tokenize import group
from django.contrib import admin
from apps.job.models import *
from decouple import config
from django.core.mail import get_connection, send_mail
from django_summernote.admin import SummernoteModelAdmin
from django.core.mail.message import EmailMessage
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.forms import TextInput, Textarea
from dateutil import parser
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Register your models here.




#export and import
class JobResource(resources.ModelResource):

    class Meta:
        model = Job
        fileds = ('id','title','department','created_by','nature','salary','experience_min','experience_max','location','vacancy','Education__name','status', 'expiration_date','post_date')
        export_order = ('id','title','department','created_by','nature','salary','experience_min','experience_max','location','vacancy','Education','status', 'expiration_date','post_date')


class JobHistoryInline(admin.TabularInline):
    extra = 0
    model =  JobHistory
    readonly_fields = ('id','open_date','close_date','vacancy','reason','days')

class jobadmin(ImportExportModelAdmin,SummernoteModelAdmin , admin.ModelAdmin):
    # displaying posts with title slug and created time
    
    resource_class = JobResource
    #change_list_template = "admin/change_list_filter_confirm.html"
    readonly_fields = ('id','job_actions',)
    inlines = [JobHistoryInline]
    list_display = ('id','title','department','created_by','nature','salary','experience_min','experience_max','location','vacancy','Education','status', 'expiration_date','post_date','job_actions',)
    list_filter = ('id','title','department','created_by','nature','salary','experience_min','experience_max','location','vacancy','Education','status', 'expiration_date','post_date')
    search_fields = ['title']
    summernote_fields = ('description', 'required_competencies','other')

    fieldsets = (
      ('ألإسم والوصف', {
          'fields': ('id',('title'))
      }),
      
      ('معلومات الوظيفة ', {
          'fields': (('department','Education'), ('salary', 'vacancy','nature')
          ,('experience_min','experience_max','location')
          ,('status','expiration_date','reason','Career_Level','langs'))
      }),


      ('المهارات المطلوبة ', {
          'fields': ((),('required_competencies'),('other',))
      }),




   )



    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('send/<int:pk>/', self.send_email),
        ]
        return my_urls + urls

    def send_email(self,request,pk):
        obj = get_object_or_404(Job, pk=pk)
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        HRUsers = list(User.objects.filter(groups__name = 'HR').values_list('email',flat=True))

<<<<<<< HEAD:apps/job/admin.py
=======

        form = super(jobadmin, self).get_form(request, obj, **kwargs)

        #Each user apply for his group and disable fields if not HR
        if not(dep=='HR'):
            form.base_fields["department"].queryset =  request.user.groups
            form.base_fields["title"].queryset = Title.objects.filter(department__name = dep)
            form.base_fields["status"].disabled = True
            form.base_fields["expiration_date"].disabled = True
        return form

    def get_queryset(self, request):

        qs = super(jobadmin, self).get_queryset(request)
        dep = request.user.groups.values_list('name',flat = True).first()
        depid = request.user.groups.values_list('id',flat = True).first()

        if dep == 'HR':
            return qs
        else:
            return qs.filter(department = depid)




    def save_form(self, request, form, change):
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        HRUsers = list(User.objects.filter(groups__name = 'HR').values_list('email',flat=True))
>>>>>>> 6d1e5612c55e23af9fe877b39e477031198ffd69:job/admin.py
        # send email for HR if not HR and on insert
        if (not (dep=='HR') ):
            subject = 'New Job'
            message = ""+user+" from "+dep+" department request new job"
            recipient_list = HRUsers # send to all HR group
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
            messages.add_message(request, messages.SUCCESS, '.The request has been sent successfully')
        return HttpResponseRedirect('../../')
      





    
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

    def get_queryset(self, request):

        qs = super(jobadmin, self).get_queryset(request)
        dep = request.user.groups.values_list('name',flat = True).first()
        depid = request.user.groups.values_list('id',flat = True).first()

        if dep == 'HR':
            return qs
        else:
            return qs.filter(department = depid)





    
    def save_model(self, request, obj, form, change):
        
        if not change:
            obj.created_by = request.user



        
        jobHistory = JobHistory(job=obj,vacancy = obj.vacancy,reason=obj.reason)
        if obj.status =='ACTIVE' and 'status' in form.changed_data :
             jobHistory.open_date = datetime.now()
             jobHistory.save()
             
             
        if obj.status =='INACTIVE' and 'status' in form.changed_data:
             jobhistoryid = JobHistory.objects.latest('id').id
             opendate = parser.parse(str(JobHistory.objects.filter(id=jobhistoryid).values_list('open_date',flat = True).first()))
             closedate = parser.parse(str(datetime.now()))
             
             jhobj = JobHistory.objects.filter(id=jobhistoryid)
             jhobj.update(close_date = datetime.now(),vacancy = obj.vacancy,reason=obj.reason,days= abs((closedate - opendate).days))
        
        obj.save()



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

class Titleadmin(ImportExportModelAdmin,SummernoteModelAdmin , admin.ModelAdmin):
    # displaying posts with title slug and created time
    resource_class = TitleResource
    readonly_fields = ('id',)
    list_display = ('id','name','department')
    list_filter = ('id','name','department')
    search_fields = ['id','name','department']
    summernote_fields = ('description',)


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


