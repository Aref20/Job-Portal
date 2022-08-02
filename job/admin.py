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
class BookResource(resources.ModelResource):

    class Meta:
        model = Job
        fileds = ('id','title','department','nature','salary','experience_min','experience_max','location','vacancy','Education__name','status', 'expiration_date','post_date')
        export_order = ('id','title','department','nature','salary','experience_min','experience_max','location','vacancy','Education','status', 'expiration_date','post_date')


class jobadmin(ImportExportModelAdmin,SummernoteModelAdmin , admin.ModelAdmin):
    # displaying posts with title slug and created time
    
    resource_class = BookResource
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
          'fields': (('department','Education'), ('salary', 'vacancy','nature'),('experience_min','experience_max','location'),('status','expiration_date','langs'))
      }),

        ('المهارات المطلوبة ', {
          'fields': ((),('required_competencies','other'))
      }),
   )

    formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    models.DateField: {'widget': TextInput(attrs={'size':'100'})},
    models.IntegerField: {'widget': TextInput(attrs={'size':'100'})},

    }

    
    def get_form(self, request, obj, **kwargs):
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        


        form = super(jobadmin, self).get_form(request, obj, **kwargs)

        #Each user apply for his group and disable fields if not HR
        if not(dep=='IT'):
            form.base_fields["department"].queryset =  request.user.groups
            form.base_fields["status"].disabled = True
            form.base_fields["expiration_date"].disabled = True


        return form



    def save_form(self, request, form, change):
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True)).first()
        dep = request.user.groups.values_list('name',flat = True).first()
        
        #id = request.resolver_match.kwargs['object_id']
        #print(""+user+ " from "+dep+" department has request new job "+str(dep)+" ")

        # send email for HR
        if not(dep=='HR'):
            subject = 'New Job'
            message = ""+user+" from "+dep+" department  add new job"
            recipient_list = ['citaga9237@galotv.com']
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


        return super().save_form(request, form, change)








    

    


  
admin.site.register(Job, jobadmin)
admin.site.register(Location)
admin.site.register(Nature)
admin.site.register(Title)
admin.site.register(Language)
admin.site.register(Degree)
admin.site.register(Career_Level)


#admin.site.register(Department,DepartmentPersonadmin)


