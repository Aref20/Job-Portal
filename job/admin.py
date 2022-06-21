from django.contrib import admin
from job.models import Job, Department , Location , Nature
from application.models import Application

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class jobadmin(SummernoteModelAdmin):
    # displaying posts with title slug and created time
    list_display = ('title', 'department','nature','status', 'post_date')
    list_filter = ("title",'department', 'post_date','status','nature','location','salary','experience_min','experience_max')
    search_fields = ['title', 'description']
    # prepopulating slug from title
    #prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('description', )
  
admin.site.register(Job, jobadmin)
admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Nature)
admin.site.register(Application)
