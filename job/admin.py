from django.contrib import admin
from job.models import *
from decouple import config
from django.core.mail import get_connection, send_mail
from django_summernote.admin import SummernoteModelAdmin
from django.core.mail.message import EmailMessage
# Register your models here.

#class Department_Personline(admin.TabularInline):
   # model = Department_Person


class jobadmin(SummernoteModelAdmin , admin.ModelAdmin):
    # displaying posts with title slug and created time

    list_display = ('title','nature','status', 'post_date')
    list_filter = ("title", 'post_date','status','nature','location','salary','experience_min','experience_max')
    search_fields = ['title', 'description']
    summernote_fields = ('description', )


#class DepartmentPersonadmin( admin.ModelAdmin):
   #     inlines = [Department_Personline,]



class requestjobadmin(SummernoteModelAdmin , admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('location', 'department','title','experience_min','experience_max','Education')
    list_filter = ('location', 'department','title','experience_min','experience_max','Education')
    search_fields = ['location', 'department','title','experience_min','experience_max','Education']
    summernote_fields = ('required_competencies','other' )


    def get_form(self, request, obj, **kwargs):

        
        form = super(requestjobadmin, self).get_form(request, obj, **kwargs)
        form.base_fields["department"].queryset =  request.user.groups
        #form.base_fields["First_Approval"].disabled = True
        #form.base_fields["First_Approval_Note"].disabled = True
        print()

        return form

    
    def save_form(self, request, form, change):
        user = (User.objects.filter(id=request.user.id).values_list('username',flat=True))[0]
        dep = request.user.groups.values_list('name',flat = True)[0]
        #id = request.resolver_match.kwargs['object_id']
        print(""+user+ " from "+dep+" department has request new job "+str(dep)+" ")
        # send email for HR
        subject = 'New Job'
        message = ""+user+" from "+dep+" department has request new job"
        recipient_list = ['arefalhamad@yahoo.com']
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
        return super().save_form(request, form, change)

  
admin.site.register(Job, jobadmin)
admin.site.register(Location)
admin.site.register(Nature)
admin.site.register(Title)
admin.site.register(Language)
admin.site.register(Degree)
admin.site.register(Career_Level)
admin.site.register(Request_Job,requestjobadmin)
#admin.site.register(Department,DepartmentPersonadmin)


