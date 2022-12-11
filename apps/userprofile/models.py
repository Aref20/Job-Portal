
from django.db import models
from datetime import date, datetime    
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.job.models import Language 
from django.utils.html import format_html
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from apps.job.models import Job
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,verbose_name=' ألإسم',null = True)
    NID = models.CharField(max_length=10,verbose_name='الرقم الوطني',error_messages={'required': 'Please let us know what to call you!'})
    image = models.ImageField( upload_to='profile_images/',verbose_name='الصورة الشخصية',null = True,blank=True)
    Birth_Date = models.DateField(default=datetime.now,verbose_name='  تاريخ الميلاد')
    Create_Date = models.DateField(auto_now_add=True,verbose_name=' تاريخ ألإنشاء')
    Socility_Status = models.CharField(choices=[('Married', 'متزوج'),('Single', 'أعزب')],default='Single',max_length=10,verbose_name='الحالة الاجتماعية ')
    Birth_Location = models.CharField(max_length=100,verbose_name=' مكان الولادة')
    City = models.CharField(max_length=100,verbose_name=' المدينة')
    Location = models.CharField(max_length=100,verbose_name='الموقع ')
    Phone_Num = models.IntegerField(verbose_name='الخلوي ',null = True)
    Nationality = models.CharField(max_length=100,verbose_name='الجنسية ')
    Car_License = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل لديك رخصة سواقة')
    Have_Car = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل تملك سيارة')
    Last_Job_Desc = models.TextField(max_length=5000,verbose_name=' شرح أخر وظيفة')
    Current_Salary = models.IntegerField( null=True,verbose_name=' الراتب الحالي')
    Expected_Salary = models.IntegerField( null=True,verbose_name='الراتب المطلوب ')
    Available_Date = models.DateField(default=datetime.now,verbose_name=' التاريخ الذي تستطيع الالتحاق فيه بالعمل')
    Relative_Frinds = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name='هل لديك اصدقاء او معارف يعملون او كانوا يعملون في شركة مجموعة منير سختيان   ')
    Relative_Frinds_Job = models.CharField(max_length=100,verbose_name='إذا كان الجواب نعم ما هي الوظيفة؟  ',null = True,blank=True)
    Diseases = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name='هل تعاني من أي أمراض؟  ')
    Coworker_Ask = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل لديك مانع من سؤال المعرفين أو أصحاب العمل السابقين عنك ؟  ')
    Warranty = models.CharField(blank=True,choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3,verbose_name=' هل يمكنك إحضار كفالة عدلية ', null=True)
    Car_License_Type = models.ForeignKey('License_Type', on_delete=models.SET_NULL, null=True,blank=True,verbose_name=' فئة الرخصة')
    Experience_Years = models.IntegerField(verbose_name='عدد سنوات الخبرة',null = True)
    Position = models.CharField(max_length=100,verbose_name='المسمى الوظيفي',null=True)
    resume = models.FileField(upload_to='documents/',verbose_name='السيرة الذاتية ')
    Profile_Job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True,blank =True,related_name="PJ",verbose_name=' الوظيفة')
    Black_List = models.BooleanField(default=False,verbose_name=' القائمة السوداء ')







    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
            if created:
                UserProfile.objects.create(user=instance)

    #@receiver(post_save, sender=User) #add this
    #def save_user_profile(sender, instance, **kwargs):
      #      instance.userprofile.save()
            
    
    


    class Meta:
        verbose_name = _(' الملفات الشخصية')
        verbose_name_plural = _('الملفات الشخصية')


    def __str__(self):
        return self.user.username



class Qualification(models.Model):
    Qualification_Profile= models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,related_name='Qualification',verbose_name='المؤهلات الأكاديمية')
    Major = models.CharField(max_length=100,verbose_name='التخصص ')
    Degree = models.CharField(max_length=100,verbose_name=' المؤهل العلمي')
    University = models.CharField(max_length=100,verbose_name=' اسم الجامعة')
    Graduation_Date = models.DateField(default=datetime.now,verbose_name='تاريخ التخرج')


    def __str__(self):
        return self.Qualification_Profile.Name

    class Meta:
        verbose_name = _('المؤهلات الأكاديمية ')
        verbose_name_plural = _('المؤهلات الأكاديمية ')

    


class UserLanguage(models.Model):
    Language_Profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,related_name='UserLanguage', null=True,verbose_name='اللغات')
    Language_Name = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True,verbose_name='اللغة ')
    Type_Conversation = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='محادثة')
    Type_Writing = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name=' كتابة')
    Type_Reading = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='قراءة')

    def __str__(self):
        return self.Language_Name.name

    class Meta:
        verbose_name = _('اللغات ')
        verbose_name_plural = _('اللغات ')

class Computer_Skill(models.Model):
    Computer_Skill_Profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,related_name='Computer_Skill',verbose_name='برامج الحاسوب')
    Skill = models.CharField(max_length=100,verbose_name=' برنامج الحاسوب')
    Level = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12,verbose_name='المهارة')

    def __str__(self):
        return self.Skill

    class Meta:
        verbose_name = _('مهارات الحاسوب ')
        verbose_name_plural = _('مهارات الحاسوب ')


class Previous_Company(models.Model):
    Previous_Company_Profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,related_name='Previous_Company',verbose_name='السجل الوظيفي')
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
    Training_Profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,related_name='Training',verbose_name='الدورات التدريبية')
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
    Previous_Coworker_Profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,related_name='Previous_Coworker',verbose_name='المعرفين')
    Name = models.CharField(max_length=100,verbose_name='الاسم ')
    Address = models.CharField(max_length=100,verbose_name='مكان العمل ')
    Phone = models.IntegerField( null=True,verbose_name='رقم الهاتف ')
    Position = models.CharField(max_length=100,verbose_name='المسمى الوظيفي')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('المعرفين  ')
        verbose_name_plural = _('المعرفين  ')

        
class License_Type(models.Model):
    Name = models.CharField(max_length=100,verbose_name=' فئة الرخصة')


    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = _('فئة الرخصة ')
        verbose_name_plural = _('فئة الرخصة ')


