from django.contrib import admin
from application.models import Application ,Qualification
from admin_auto_filters.filters import AutocompleteFilter
from job.models import *
from decouple import config
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from interview.models import *
# Register your models here.


class QualificationInline(admin.TabularInline):
    model = Qualification
    #fields = ['Degree']  


class JobFilter(AutocompleteFilter):
    title = 'Job' # display title
    field_name = 'Job_App' # name of the foreign key field





class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    inlines = [QualificationInline,]
    list_display = ('Name', 'NID','Email','Phone_Num','Job_App' , 'Create_Date')
    list_filter = (JobFilter,'Name', 'NID','Email','Job_App' , 'Create_Date')
    change_list_template = "admin/change_list_filter_confirm.html"
    change_list_filter_template = "admin/filter_listing.html"
    
    
    
    def get_form(self, request, obj, **kwargs):
        loguserlist = []
        appid = request.resolver_match.kwargs['object_id'] # get current application id
        loguser = (request.user.id)
        loguserlist.append(loguser)
        job = Job.objects.filter(JA__id=appid)[0] # get current job
        users = list(User.objects.filter(usertitle__name=job).values_list('id',flat=True)) # get all users for this job
        
        form = super(ApplicationAdmin, self).get_form(request, obj, **kwargs)
        if loguserlist in  users: # if current user defind for this job
            form.base_fields["First_Approval"].disabled = True
            form.base_fields["First_Approval_Note"].disabled = True

        else:
            form.base_fields["Second_Approval"].disabled = True
            form.base_fields["Second_Approval_Note"].disabled = True
            form.base_fields["HR_Interview_Approval"].disabled = True


            
        return form


    def save_form(self, request, form, change):
        appid = request.resolver_match.kwargs['object_id']
        first_app = form.cleaned_data.get('First_Approval')
        secound_app = form.cleaned_data.get('Second_Approval')
        HR_App = form.cleaned_data.get('HR_Interview_Approval')
        applicant_name = form.cleaned_data.get('Name')
        interview_date_hour = form.cleaned_data.get('Interview_Date').strftime("%H:%M:%S")
        interview_date = form.cleaned_data.get('Interview_Date').strftime("%m/%d/%Y")

        loguserlist = []
        appid = request.resolver_match.kwargs['object_id'] # get current application id
        job = Job.objects.filter(JA__id=appid)[0] # get current job
        users = list(User.objects.filter(usertitle__name=job).values_list('email',flat=True))
        if first_app and secound_app and HR_App :
                    # send email for users and HR
                    subject = 'مقابلة'
                    message = 'رابط المقابلة الساعة '+interview_date_hour+' '+interview_date+' في تاريخ  '+applicant_name+' تم تحدديد مقابلة للسيد '
                    recipient_list = users
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


                    # send email for applicanet
                    subject2 = 'welcome to GFG world'
                    message2 = 'Hبيليلي.'
                    recipient_list2 = [form.cleaned_data.get('Email')]
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







    #search_fields = ['Name', 'NID','Email','Phone_Num' , 'Create_Date']







admin.site.register(Application,ApplicationAdmin)
admin.site.register(Qualification)