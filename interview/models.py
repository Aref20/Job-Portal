from email.mime import application
from django.db import models
from application.models import *

# Create your models here.

class Interview(models.Model):
    #interview_application = models.ForeignKey(application, on_delete=models.SET_NULL, null=True)
    commitment = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    MSG_knowledge = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    MSG_comp_knowledge = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    self_exp_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    body_exp_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    behaviour = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    asked_q_level = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    eng_lang_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)
    computer_skill = models.CharField(choices=[('Excellent', 'ممتاز'),('Very Good', 'جيد جدا'),('Good', 'جيد'),('Bad', ' غير مقبول')],default='Very Good',max_length=12)


