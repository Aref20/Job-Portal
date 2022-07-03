from django.contrib import admin
from job.models import *


from django_summernote.admin import SummernoteModelAdmin

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





  
admin.site.register(Job, jobadmin)
#admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Nature)
admin.site.register(Title)
#admin.site.register(Department,DepartmentPersonadmin)


