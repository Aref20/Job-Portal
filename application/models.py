from django.db import models
from job.models import Job
from datetime import date, datetime    
from django.utils import timezone

# Create your models here.



class Application(models.Model):
    NID = models.CharField(max_length=10,verbose_name='الرقم الوطني',error_messages={'required': 'Please let us know what to call you!'})
    Email = models.EmailField(max_length=100)
    Birth_Date = models.DateField(default=datetime.now)
    Name = models.CharField(max_length=100)
    Create_Date = models.DateField(auto_now_add=True)
    Socility_Status = models.CharField(choices=[('Married', 'متزوج'),('Single', 'أعزب')],default='Single',max_length=10)
    Birth_Location = models.CharField(max_length=100,blank=True)
    City = models.CharField(max_length=100)
    Location = models.CharField(max_length=100,blank=True)
    Phone_Num = models.IntegerField()
    Nationality = models.CharField(max_length=100)
    Car_License = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Have_Car = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Job_App = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True,blank=True)
    Last_Job_Desc = models.TextField(max_length=5000)
    Current_Salary = models.IntegerField( null=True,blank=True)
    Expected_Salary = models.IntegerField( null=True,blank=True)
    Available_Date = models.DateField(default=datetime.now)
    Relative_Frinds = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Relative_Frinds_Job = models.CharField(max_length=100)
    Diseases = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    
    L_Language = models.CharField(max_length=100)
    L_Type_Conversation = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)
    L_Type_Writing = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)
    L_Type_Reading = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)

    C_Computer_Skill = models.CharField(max_length=100)
    C_Computer_Level = models.CharField(choices=[('Beginner', 'ضعيف'),('Intermediate', 'متوسط'),('Advanced', 'ممتاز')],default='Beginner',max_length=12)

    Company_Prev_Name = models.CharField(max_length=100)
    Company_Prev_Address = models.CharField(max_length=100)
    Company_Prev_Phone = models.IntegerField( null=True,blank=True)
    Company_Prev_Duration_From = models.DateField(default=datetime.now)
    Company_Prev_Duration_To = models.DateField(default=datetime.now)
    Company_Prev_Position = models.CharField(max_length=100)
    Company_Prev_Start_Salary = models.IntegerField( null=True,blank=True)
    Company_Prev_Last_Salary = models.IntegerField( null=True,blank=True)
    Company_Prev_Reason = models.TextField(max_length=5000)
    Company_Prev_Maneger = models.CharField(max_length=100)


    T_Training_Name = models.CharField(max_length=100)
    T_Training_Duration_From = models.DateField(default=datetime.now)
    T_Training_Duration_To = models.DateField(default=datetime.now)
    T_Training_Location = models.CharField( null=True,blank=True,max_length=100)
    T_Training_Institute = models.CharField(max_length=100)

    Prev_Coworker_Name = models.CharField(max_length=100)
    Prev_Coworker_Address = models.CharField(max_length=100)
    Prev_Coworker_Phone = models.IntegerField( null=True,blank=True)
    Prev_Coworker_Position = models.CharField(max_length=100)

    Coworker_Ask = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)
    Black_List = models.BooleanField(default=False, blank=True)
    First_Approval = models.BooleanField(default=False, blank=True)
    First_Approval_Note = models.TextField(max_length=5000, blank=True)
    Second_Approval = models.BooleanField(default=False,blank=True)
    Second_Approval_Note = models.TextField(max_length=5000, blank=True)

    resume = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.Name







class Qualification(models.Model):
    Qualification_Application= models.ForeignKey(Application, on_delete=models.SET_NULL, null=True,related_name='Qualification')
    Degree = models.CharField(max_length=100)
    University = models.CharField(max_length=100)
    Graduation_Date = models.DateField()
    Major = models.CharField(max_length=100)

    def __str__(self):
        return self.Qualification_Application









