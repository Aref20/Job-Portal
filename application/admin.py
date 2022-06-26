from django.contrib import admin
from application.models import Application ,Qualification
from admin_auto_filters.filters import AutocompleteFilter
# Register your models here.



class JobFilter(AutocompleteFilter):
    title = 'Job' # display title
    field_name = 'Job_App' # name of the foreign key field



class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'NID','Email','Phone_Num','Job_App' , 'Create_Date')
    list_filter = (JobFilter,'Name', 'NID','Email','Job_App' , 'Create_Date')
    change_list_template = "admin/change_list_filter_confirm.html"
    change_list_filter_template = "admin/filter_listing.html"

    #search_fields = ['Name', 'NID','Email','Phone_Num' , 'Create_Date']







admin.site.register(Application,ApplicationAdmin)
admin.site.register(Qualification)