from django.db import models
from job.models import Job
from datetime import date, datetime    
from django.utils import timezone

# Create your models here.



class Application(models.Model):
    Application_NID = models.CharField(max_length=10,verbose_name='الرقم الوطني',error_messages={'required': 'Please let us know what to call you!'})
    Application_Email = models.EmailField(max_length=100)
    Application_Birth_Date = models.DateField(default=timezone.now())
    Application_Name = models.CharField(max_length=100)
    Application_Create_Date = models.DateField(auto_now_add=True)
    Application_Socility_Status = models.CharField(choices=[('Married', 'متزوج'),('Single', 'أعزب')],default='Single',max_length=10)
    Application_Birth_Location = models.CharField(max_length=100,blank=True)
    Application_City = models.CharField(max_length=100)
    Application_Location = models.CharField(max_length=100,blank=True)
    Application_Phone_Num = models.IntegerField()
    Application_Nationality = models.CharField(max_length=100)
    Application_Car_License = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Application_Have_Car = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Application_Job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    Application_Last_Job_Desc = models.TextField(max_length=5000)
    Application_Current_Salary = models.IntegerField(default=0, null=True,blank=True)
    Application_Expected_Salary = models.IntegerField(default=0, null=True,blank=True)
    Application_Available_Date = models.DateField(default=timezone.now())
    Application_Relative_Frinds = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Application_Relative_Frinds_Job = models.CharField(max_length=100)
    Application_Diseases = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    
    Application_L_Language = models.CharField(max_length=100)
    Application_L_Type_Conversation = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)
    Application_L_Type_Writing = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)
    Application_L_Type_Reading = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)

    Application_C_Computer_Skill = models.CharField(max_length=100)
    Application_C_Computer_Level = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)

    Application_Company_Prev_Name = models.CharField(max_length=100)
    Application_Company_Prev_Address = models.CharField(max_length=100)
    Application_Company_Prev_Phone = models.IntegerField(default=0, null=True,blank=True)
    Application_Company_Prev_Duration_From = models.DateField(default=timezone.now())
    Application_Company_Prev_Duration_To = models.DateField(default=timezone.now())
    Application_Company_Prev_Position = models.CharField(max_length=100)
    Application_Company_Prev_Start_Salary = models.IntegerField(default=0, null=True,blank=True)
    Application_Company_Prev_Last_Salary = models.IntegerField(default=0, null=True,blank=True)
    Application_Company_Prev_Reason = models.TextField(max_length=5000)
    Application_Company_Prev_Maneger = models.CharField(max_length=100)


    Application_T_Training_Name = models.CharField(max_length=100)
    Application_T_Training_Duration_From = models.DateField(default=timezone.now())
    Application_T_Training_Duration_To = models.DateField(default=timezone.now())
    Application_T_Training_Location = models.CharField( null=True,blank=True,max_length=100)
    Application_T_Training_Institute = models.CharField(max_length=100)

    Application_Prev_Coworker_Name = models.CharField(max_length=100)
    Application_Prev_Coworker_Address = models.CharField(max_length=100)
    Application_Prev_Coworker_Phone = models.IntegerField(default=0, null=True,blank=True)
    Application_Prev_Coworker_Position = models.CharField(max_length=100)

    Application_Coworker_Ask = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Application_Black_List = models.BooleanField(default=False, blank=True)
    Application_First_Approval = models.BooleanField(default=False, blank=True)
    Application_First_Approval_Note = models.TextField(max_length=5000, blank=True)
    Application_Second_Approval = models.BooleanField(default=False,blank=True)
    Application_Second_Approval_Note = models.TextField(max_length=5000, blank=True)



    #Qualification_Application= models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Application_Qualification')
    #Qualification_Degree = models.CharField(max_length=100)
    #Qualification_University = models.CharField(max_length=100)
    #Qualification_Graduation_Date = models.DateField()
    #Qualification_Major = models.CharField(max_length=100)


#class Qualification(models.Model):









