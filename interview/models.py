from email.mime import application
from django.db import models
from application.models import *

# Create your models here.

class Interview(models.Model):
    interview_application = models.OneToOneField(Application, on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(auto_now_add=True)
    commitment = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    MSG_knowledge = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    MSG_comp_knowledge = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    self_exp_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    body_exp_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    behaviour = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    asked_q_level = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    eng_lang_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    computer_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)

    working_experience = models.TextField(max_length=3000,blank=True)
    management_leading_cap = models.TextField(max_length=3000,blank=True)
    tech_cap = models.TextField(max_length=3000,blank=True)
    personality = models.TextField(max_length=3000,blank=True)
    prev_work_leave = models.TextField(max_length=3000,blank=True)
    achievements = models.TextField(max_length=3000,blank=True)
    pros = models.TextField(max_length=3000,blank=True)
    cons = models.TextField(max_length=3000,blank=True)
    expected_salary = models.IntegerField(max_length=100,default=0)
    work_time = models.DateTimeField(default=datetime.now)
    note = models.TextField(max_length=3000,blank=True)
    hiring_Recommendation = models.CharField(choices=[('Yes', 'نعم'),('No', 'لا')],default='No',max_length=3)


      
    def __str__(self):
        return self.interview_application.Name



