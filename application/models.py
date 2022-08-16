#from asyncio.windows_events import NULL
from django.db import models
from job.models import Job
from datetime import date, datetime    
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from job.models import Language as Lang
from django.utils.html import format_html
# Create your models here.

class License_Type(models.Model):
    Name = models.CharField(max_length=100,verbose_name=' فئة الرخصة')


    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('فئة الرخصة ')
        verbose_name_plural = _('فئة الرخصة ')

class Application(models.Model):
    NID = models.CharField(max_length=10,verbose_name='الرقم الوطني',error_messages={'required': 'Please let us know what to call you!'})
    department =  models.CharField(max_length=100,verbose_name='القسم',null=True,blank=True)
    Email = models.EmailField(max_length=100,verbose_name='البريد الإلكتروني ')
    Birth_Date = models.DateField(default=datetime.now,verbose_name='  تاريخ الميلاد')
    Name = models.CharField(max_length=100,verbose_name=' الاسم')
    Create_Date = models.DateField(auto_now_add=True,verbose_name=' تاريخ التقديم')
    Socility_Status = models.CharField(choices=[('Married', 'متزوج'),('Single', 'أعزب')],default='Single',max_length=10,verbose_name='الحالة الاجتماعية ')
    Birth_Location = models.CharField(max_length=100,verbose_name=' مكان الولادة')
    City = models.CharField(max_length=100,verbose_name=' المدينة')
    Location = models.CharField(max_length=100,verbose_name='الموقع ')
    Phone_Num = models.IntegerField(verbose_name='الخلوي ')
    Nationality = models.CharField(max_length=100,verbose_name='الجنسية ')
    Car_License = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل لديك رخصة سواقة')
    Have_Car = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل تملك سيارة')
    Job_App = models.ForeignKey(Job,blank=True, on_delete=models.SET_NULL, null=True , related_name="JA",verbose_name=' الوظيفة')
    Last_Job_Desc = models.TextField(max_length=5000,verbose_name=' شرح أخر وظيفة')
    Current_Salary = models.IntegerField( null=True,verbose_name=' الراتب الحالي')
    Expected_Salary = models.IntegerField( null=True,verbose_name='الراتب المطلوب ')
    Available_Date = models.DateField(default=datetime.now,verbose_name=' التاريخ الذي تستطيع الالتحاق فيه بالعمل')
    Relative_Frinds = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name='هل لديك اصدقاء او معارف يعملون او كانوا يعملون في شركة مجموعة منير سختيان   ')
    Relative_Frinds_Job = models.CharField(max_length=100,verbose_name='إذا كان الجواب نعم ما هي الوظيفة؟  ')
    Diseases = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name='هل تعاني من أي أمراض؟  ')
    Black_List = models.BooleanField(default=False,verbose_name=' القائمة السوداء ')
    First_Approval = models.BooleanField(default=False,verbose_name=' موافقة الموارد البشرية ')
    First_Approval_Note = models.TextField(blank=True,max_length=5000,verbose_name=' ملاحظات الموارد البشرية ')
    Second_Approval = models.BooleanField(default=False,verbose_name='موافقة رئيس القسم ')
    Second_Approval_Note = models.TextField(blank=True,max_length=5000,verbose_name=' ملاحظات رئيس القسم')
    Coworker_Ask = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل لديك مانع من سؤال المعرفين أو أصحاب العمل السابقين عنك ؟  ')
    Interview_Date = models.DateTimeField(blank=True,default=datetime.now,verbose_name=' تحديد تاريخ المقابلة')
    HR_Interview_Approval = models.BooleanField(default=False,verbose_name=' موافقة الموارد البشرية لتاريخ المقابلة ')
    Warranty = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل يمكنك إحضار كفالة عدلية ', null=True)
    Car_License_Type = models.ForeignKey(License_Type, on_delete=models.SET_NULL, null=True,verbose_name=' فئة الرخصة')
    Experience_Years = models.IntegerField(verbose_name='عدد سنوات الخبرة')
    Waiting_List = models.BooleanField(default=False,verbose_name='قائمة ألإنتظار ')
    resume = models.FileField(upload_to='documents/',verbose_name='السيرة الذاتية ')
    


    class Meta:
        verbose_name = _('طلبات التوظيف')
        verbose_name_plural = _('طلبات التوظيف')


    def __str__(self):
        return self.Name



class Qualification(models.Model):
    Qualification_Application= models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Qualification',verbose_name='المؤهلات الأكاديمية')
    Major = models.CharField(max_length=100,verbose_name='التخصص ')
    Degree = models.CharField(max_length=100,verbose_name=' المؤهل العلمي')
    University = models.CharField(max_length=100,verbose_name=' اسم الجامعة')
    Graduation_Date = models.DateField(default=datetime.now,verbose_name='تاريخ التخرج')


    def __str__(self):
        return self.Qualification_Application.Name

    class Meta:
        verbose_name = _('المؤهلات الأكاديمية ')
        verbose_name_plural = _('المؤهلات الأكاديمية ')

    


class Language(models.Model):
    Language_Application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Language',verbose_name='اللغات')
    Language_Name = models.ForeignKey(Lang, on_delete=models.SET_NULL, null=True,verbose_name='اللغة ')
    Type_Conversation = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='محادثة')
    Type_Writing = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name=' كتابة')
    Type_Reading = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='قراءة')

    def __str__(self):
        return self.Language_Name.name

    class Meta:
        verbose_name = _('اللغات ')
        verbose_name_plural = _('اللغات ')

class Computer_Skill(models.Model):
    Computer_Skill_Application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Computer_Skill',verbose_name='برامج الحاسوب')
    Skill = models.CharField(max_length=100,verbose_name=' برنامج الحاسوب')
    Level = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='المهارة')

    def __str__(self):
        return self.Skill

    class Meta:
        verbose_name = _('مهارات الحاسوب ')
        verbose_name_plural = _('مهارات الحاسوب ')


class Previous_Company(models.Model):
    Previous_Company_Application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Previous_Company',verbose_name='السجل الوظيفي')
    Name = models.CharField(max_length=100,verbose_name=' إسم الشركة السابقة')
    Address = models.CharField(max_length=100,verbose_name=' عنوان الشركة')
    Phone = models.IntegerField( null=True,verbose_name=' رقم هاتف الشركة')
    Duration_From = models.DateField(default=datetime.now,verbose_name=' تاريخ بدءالعمل ')
    Duration_To = models.DateField(default=datetime.now,verbose_name=' تاريخ إنتهاء العمل')
    Position = models.CharField(max_length=100,verbose_name=' المسمى الوظيفي')
    Start_Salary = models.IntegerField( null=True,verbose_name=' الراتب عند البداية')
    Last_Salary = models.IntegerField( null=True,verbose_name='الراتب عند النهاية ')
    Maneger = models.CharField(max_length=100,verbose_name=' المدير المباشر ')
    Reason = models.TextField(max_length=5000,verbose_name='سبب ترك العمل ')

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = _('السجل الوظيفي  ')
        verbose_name_plural = _('السجل الوظيفي  ')



class Training(models.Model):
    Training_Application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Training',verbose_name='الدورات التدريبية')
    Name = models.CharField(max_length=100,verbose_name='اسم الدورة التدريبية ')
    Location = models.CharField( null=True,max_length=100,verbose_name=' مكان انعقاد الدورة')
    Institute = models.CharField(max_length=100,verbose_name='الجهة التدريبية ')
    Duration_From = models.DateField(default=datetime.now,verbose_name=' تاريخ بدء الدورة')
    Duration_To = models.DateField(default=datetime.now,verbose_name='تاريخ الانتهاء ')



    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _(' الدورات التدريبية  ')
        verbose_name_plural = _(' الدورات التدريبية  ')

class Previous_Coworker(models.Model):
    Previous_Coworker_Application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Previous_Coworker',verbose_name='المعرفين')
    Name = models.CharField(max_length=100,verbose_name='الاسم ')
    Address = models.CharField(max_length=100,verbose_name='مكان العمل ')
    Phone = models.IntegerField( null=True,verbose_name='رقم الهاتف ')
    Position = models.CharField(max_length=100,verbose_name='المسمى الوظيفي')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('المعرفين  ')
        verbose_name_plural = _('المعرفين  ')
    









# Application form apply for all


class Application_Form(models.Model):
    NID = models.CharField(max_length=10,verbose_name='الرقم الوطني',error_messages={'required': 'Please let us know what to call you!'})
    Email = models.EmailField(max_length=100,verbose_name='البريد الإلكتروني ')
    Birth_Date = models.DateField(default=datetime.now,verbose_name='  تاريخ الميلاد')
    Name = models.CharField(max_length=100,verbose_name=' الاسم')
    Create_Date = models.DateField(auto_now_add=True,verbose_name=' تاريخ التقديم')
    Socility_Status = models.CharField(choices=[('Married', 'متزوج'),('Single', 'أعزب')],default='Single',max_length=10,verbose_name='الحالة الاجتماعية ')
    Birth_Location = models.CharField(max_length=100,verbose_name=' مكان الولادة')
    City = models.CharField(max_length=100,verbose_name=' المدينة')
    Location = models.CharField(max_length=100,verbose_name='الموقع ')
    Phone_Num = models.IntegerField(verbose_name='الخلوي ')
    Nationality = models.CharField(max_length=100,verbose_name='الجنسية ')
    Car_License = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل لديك رخصة سواقة')
    Have_Car = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل تملك سيارة')
    Last_Job_Desc = models.TextField(max_length=5000,verbose_name=' شرح أخر وظيفة')
    Current_Salary = models.IntegerField( null=True,verbose_name=' الراتب الحالي')
    Expected_Salary = models.IntegerField( null=True,verbose_name='الراتب المطلوب ')
    Available_Date = models.DateField(default=datetime.now,verbose_name=' التاريخ الذي تستطيع الالتحاق فيه بالعمل')
    Relative_Frinds = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name='هل لديك اصدقاء او معارف يعملون او كانوا يعملون في شركة مجموعة منير سختيان   ')
    Relative_Frinds_Job = models.CharField(max_length=100,verbose_name='إذا كان الجواب نعم ما هي الوظيفة؟  ')
    Diseases = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name='هل تعاني من أي أمراض؟  ')
    Black_List = models.BooleanField(default=False,verbose_name=' القائمة السوداء ')
    First_Approval = models.BooleanField(default=False,verbose_name=' موافقة الموارد البشرية ')
    First_Approval_Note = models.TextField(blank=True,max_length=5000,verbose_name=' ملاحظات الموارد البشرية ')
    Second_Approval = models.BooleanField(default=False,verbose_name='موافقة رئيس القسم ')
    Second_Approval_Note = models.TextField(blank=True,max_length=5000,verbose_name=' ملاحظات رئيس القسم')
    Coworker_Ask = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل لديك مانع من سؤال المعرفين أو أصحاب العمل السابقين عنك ؟  ')
    Interview_Date = models.DateTimeField(blank=True,default=datetime.now,verbose_name=' تحديد تاريخ المقابلة')
    HR_Interview_Approval = models.BooleanField(default=False,verbose_name=' موافقة الموارد البشرية لتاريخ المقابلة ')
    Warranty = models.CharField(blank=True,choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل يمكنك إحضار كفالة عدلية', null=True)
    Car_License_Type = models.ForeignKey(License_Type, on_delete=models.SET_NULL, null=True,verbose_name=' فئة الرخصة')
    Experience_Years = models.IntegerField(verbose_name='عدد سنوات الخبرة')
    Waiting_List = models.BooleanField(default=False,verbose_name='قائمة ألإنتظار ')
    resume = models.FileField(upload_to='documents/',verbose_name='السيرة الذاتية ')
    


    class Meta:
        verbose_name = _(' طلبات التوظيف العشوائية')
        verbose_name_plural = _('طلبات التوظيف العشوائية')


    def __str__(self):
        return self.Name



class Qualification_Form(models.Model):
    Qualification_Application= models.ForeignKey(Application_Form, on_delete=models.SET_NULL, null=True,related_name='Qualification',verbose_name='المؤهلات الأكاديمية')
    Major = models.CharField(max_length=100,verbose_name='التخصص')
    Degree = models.CharField(max_length=100,verbose_name='المؤهل العلمي')
    University = models.CharField(max_length=100,verbose_name='اسم الجامعة')
    Graduation_Date = models.DateField(default=datetime.now,verbose_name='تاريخ التخرج')
    

    def __str__(self):
        return self.Qualification_Application.Name

    class Meta:
        verbose_name = _('المؤهلات الأكاديمية')
        verbose_name_plural = _('المؤهلات الأكاديمية')

    


class Language_Form(models.Model):
    Language_Application = models.ForeignKey(Application_Form, on_delete=models.SET_NULL, null=True,related_name='Language',verbose_name='اللغات')
    Language_Name = models.ForeignKey(Lang, on_delete=models.SET_NULL, null=True,verbose_name='اللغة')
    Type_Conversation = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='محادثة')
    Type_Writing = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='كتابة')
    Type_Reading = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='قراءة')

    def __str__(self):
        return self.Language_Name.name

    class Meta:
        verbose_name = _('اللغات ')
        verbose_name_plural = _('اللغات ')

class Computer_Skill_Form(models.Model):
    Computer_Skill_Application = models.ForeignKey(Application_Form, on_delete=models.SET_NULL, null=True,related_name='Computer_Skill',verbose_name='برامج الحاسوب')
    Skill = models.CharField(max_length=100,verbose_name='برنامج الحاسوب')
    Level = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='المهارة')

    def __str__(self):
        return self.Skill

    class Meta:
        verbose_name = _('مهارات الحاسوب')
        verbose_name_plural = _('مهارات الحاسوب')


class Previous_Company_Form(models.Model):
    Previous_Company_Application = models.ForeignKey(Application_Form, on_delete=models.SET_NULL, null=True,related_name='Previous_Company',verbose_name='السجل الوظيفي')
    Name = models.CharField(max_length=100,verbose_name='إسم الشركة السابقة')
    Address = models.CharField(max_length=100,verbose_name='عنوان الشركة')
    Phone = models.IntegerField( null=True,verbose_name='رقم هاتف الشركة')
    Duration_From = models.DateField(default=datetime.now,verbose_name='تاريخ بدءالعمل ')
    Duration_To = models.DateField(default=datetime.now,verbose_name='تاريخ إنتهاء العمل')
    Position = models.CharField(max_length=100,verbose_name='المسمى الوظيفي')
    Start_Salary = models.IntegerField( null=True,verbose_name='الراتب عند البداية')
    Last_Salary = models.IntegerField( null=True,verbose_name='الراتب عند النهاية')
    Maneger = models.CharField(max_length=100,verbose_name='المدير المباشر ')
    Reason = models.TextField(max_length=5000,verbose_name='سبب ترك العمل ')
    

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = _('السجل الوظيفي  ')
        verbose_name_plural = _('السجل الوظيفي  ')


class Training_Form(models.Model):
    Training_Application = models.ForeignKey(Application_Form, on_delete=models.SET_NULL, null=True,related_name='Training',verbose_name='الدورات التدريبية')
    Name = models.CharField(max_length=100,verbose_name='اسم الدورة التدريبية')
    Location = models.CharField( null=True,max_length=100,verbose_name=' مكان انعقاد الدورة')
    Institute = models.CharField(max_length=100,verbose_name='الجهة التدريبية')
    Duration_From = models.DateField(default=datetime.now,verbose_name='تاريخ بدء الدورة')
    Duration_To = models.DateField(default=datetime.now,verbose_name='تاريخ الانتهاء ')


    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _(' الدورات التدريبية  ')
        verbose_name_plural = _(' الدورات التدريبية  ')

class Previous_Coworker_Form(models.Model):
    Previous_Coworker_Application = models.ForeignKey(Application_Form, on_delete=models.SET_NULL, null=True,related_name='Previous_Coworker',verbose_name='المعرفين')
    Name = models.CharField(max_length=100,verbose_name='الاسم')
    Address = models.CharField(max_length=100,verbose_name='مكان العمل')
    Phone = models.IntegerField( null=True,verbose_name='رقم الهاتف')
    Position = models.CharField(max_length=100,verbose_name='المسمى الوظيفي')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('المعرفين  ')
        verbose_name_plural = _('المعرفين  ')
    



