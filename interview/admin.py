from pyexpat import model
from django.contrib import admin
from .models import *
# Register your models here.


class InterviewAdmin(admin.ModelAdmin):
    #readonly_fields = ('interview_application.id',)
    list_display = ('interview_application','hiring_Recommendation')
    list_filter = ('interview_application','hiring_Recommendation',)
    change_list_template = "admin/change_list_filter_confirm.html"
    change_list_filter_template = "admin/filter_listing.html"

admin.site.register(Interview,InterviewAdmin)

