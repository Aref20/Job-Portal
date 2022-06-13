from django.contrib import admin
from job.models import Job, Department
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class jobadmin(SummernoteModelAdmin):
    # displaying posts with title slug and created time
    list_display = ('job_title', 'job_description', 'job_department', 'job_post_date')
    list_filter = ("job_title",'job_department', 'job_post_date' )
    search_fields = ['job_title', 'job_description']
    # prepopulating slug from title
    #prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('job_description', )
  
admin.site.register(Job, jobadmin)
admin.site.register(Department)
