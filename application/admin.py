from django.contrib import admin
from application.models import Application ,Qualification
from admin_auto_filters.filters import AutocompleteFilter
from job.models import *
# Register your models here.


class QualificationInline(admin.TabularInline):
    model = Qualification
    #fields = ['Degree']  


class JobFilter(AutocompleteFilter):
    title = 'Job' # display title
    field_name = 'Job_App' # name of the foreign key field





class ApplicationAdmin(admin.ModelAdmin):
    inlines = [QualificationInline,]
    list_display = ('Name', 'NID','Email','Phone_Num','Job_App' , 'Create_Date')
    list_filter = (JobFilter,'Name', 'NID','Email','Job_App' , 'Create_Date')
    change_list_template = "admin/change_list_filter_confirm.html"
    change_list_filter_template = "admin/filter_listing.html"
    


    
    def get_form(self, request, obj, **kwargs):
       # print(request.user.groups.values_list('name', flat=True).first())
        #self.exclude = ("title", )
        #if request.user.groups.values_list('name', flat=True).first() == "HR":
            #readonly_fields = ('headline', )
            #self.exclude = ("title", )
            
        form = super(ApplicationAdmin, self).get_form(request, obj, **kwargs)
        if request.user.groups.values_list('name', flat=True).first() == "HR":
            form.base_fields["Second_Approval"].disabled = True
            form.base_fields["Second_Approval_Note"].disabled = True
        else:
            #form.base_fields['Job_App'].queryset =
            #q =  Title.objects.values('department_person')
            s=User.objects.filter(usertitle__name='Data Analysis')
           # print(s)
            print(form.fields)
            form.base_fields["First_Approval"].disabled = True
            form.base_fields["First_Approval_Note"].disabled = True
        return form




    #search_fields = ['Name', 'NID','Email','Phone_Num' , 'Create_Date']







admin.site.register(Application,ApplicationAdmin)
admin.site.register(Qualification)