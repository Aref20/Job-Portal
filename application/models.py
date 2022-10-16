#from asyncio.windows_events import NULL
from django.db import models
from job.models import Job
from userprofile.models import *
from django.utils.translation import gettext_lazy as _
from job.models import Language as Lang
from django.utils.html import format_html
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class Application(models.Model):
    UserProfile_App = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True,blank =True,verbose_name=' الملف الشخصي')
    Job_App = models.ForeignKey(Job, on_delete=models.CASCADE,null=True,blank =True,related_name="JA",verbose_name=' الوظيفة')
    Visit = models.BooleanField(default=False,verbose_name=' تمت رؤيته ')
    Waiting_List = models.BooleanField(default=False,verbose_name='قائمة ألإنتظار ')
    department =  models.CharField(max_length=100,verbose_name='القسم',null=True,blank=True)
    Interview_Date = models.DateField(blank=True,default=now ,verbose_name=' تحديد تاريخ المقابلة')
    HR_Interview_Approval = models.BooleanField(default=False,verbose_name=' موافقة الموارد البشرية لتاريخ المقابلة ')
    Black_List = models.BooleanField(default=False,verbose_name=' القائمة السوداء ')
    First_Approval = models.BooleanField(default=False,verbose_name=' موافقة الموارد البشرية ')
    First_Approval_Note = models.TextField(blank=True,max_length=5000,verbose_name=' ملاحظات الموارد البشرية ')
    Second_Approval = models.BooleanField(default=False,verbose_name='موافقة رئيس القسم ')
    Second_Approval_Note = models.TextField(blank=True,max_length=5000,verbose_name=' ملاحظات رئيس القسم')
    Create_Date = models.DateField(auto_now_add=True,verbose_name=' تاريخ التقديم')


    class Meta:
        verbose_name = _('  طلبات التوظيف')
        verbose_name_plural = _('  طلبات التوظيف')


    def __str__(self):
        return self.UserProfile_App.Name