from asyncio import create_task
from datetime import timezone
from .enum import *
from django.db import models
from django.contrib.auth.models import Group,User
from datetime import date, datetime    
from smart_selects.db_fields import ChainedManyToManyField,ChainedForeignKey
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=300,verbose_name=' اللغة')
    class Meta:
        verbose_name = _('اللغات  ')
        verbose_name_plural = _(' اللغات ')

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=300,verbose_name='الدرجة العلمية')

    class Meta:
        verbose_name = _(' الدرجة العلمية')
        verbose_name_plural = _(' الدرجة العلمية ')

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.ForeignKey('Title', on_delete=models.SET_NULL, null=True,verbose_name='عنوان الوظيفة ')
    description = models.TextField(max_length=3000,verbose_name='الوصف ')
    post_date = models.DateField(auto_now_add=True,verbose_name=' تاريخ الانشاء')
    vacancy = models.IntegerField(blank=True,verbose_name='الشواغر ')
    salary = models.IntegerField( blank=True,verbose_name='الراتب ')
    Education = models.ForeignKey(Degree,on_delete=models.SET_NULL, null=True,verbose_name='الدرجة العلمية ')
    department = models.ForeignKey(Group,on_delete=models.SET_NULL, null=True,verbose_name=' القسم')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True,verbose_name='الموقع ')
    experience_min = models.IntegerField(blank=True,verbose_name='الخبرة من')
    experience_max = models.IntegerField(blank=True,verbose_name='الخبرة الى ')
    nature = models.ForeignKey('Nature', on_delete=models.SET_NULL, null=True,verbose_name='طبيعة العمل ')
    langs =  models.ManyToManyField(Language, null=True,verbose_name='اللغات ')
    status = models.CharField(max_length=255, choices=Status.choices(),default=Status.ACTIVE,verbose_name='حالة الوظيفة ')

    expiration_date = models.DateTimeField(default=datetime.now,verbose_name='تاريخ إنتهاء الوظيفة ')
    
    def __str__(self):
        return self.title.name


    class Meta:
        verbose_name = _(' الوظائف ')
        verbose_name_plural = _(' الوظائف ')


class Location(models.Model):
    location_name = models.CharField(max_length=300,verbose_name=' الموقع')

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name = _(' الموقع ')
        verbose_name_plural = _(' الموقع ')

class Nature(models.Model):
    Nature_name = models.CharField(max_length=300,verbose_name=' طبيعة العمل')

    def __str__(self):
        return self.Nature_name

    class Meta:
        verbose_name = _(' طبيعة العمل ')
        verbose_name_plural = _(' طبيعة العمل ')

class Title(models.Model):
    name = models.CharField(max_length=300,verbose_name=' عنوان الوظيفة')
    department = models.ForeignKey(Group,on_delete=models.SET_NULL, null=True,verbose_name=' القسم')
    department_person = ChainedManyToManyField(
        User,
        verbose_name='department_person',
        horizontal=True,
        chained_field="department",
        chained_model_field="groups", blank=True, null=True,related_name='usertitle')# chaining fileds


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = _(' عنوان الوظيفة ')
        verbose_name_plural = _(' عنوان الوظيفة ')


class Career_Level(models.Model):
    level = models.CharField(max_length=300,verbose_name='  مستوى الخبرة')

    class Meta:
        verbose_name = _('مستوى الخبرة ')
        verbose_name_plural = _(' مستوى الخبرة ')

    def __str__(self):
        return self.level








class Request_Job(models.Model):
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True,verbose_name='الموقع ')
    department = models.ForeignKey(Group,on_delete=models.SET_NULL, null=True,verbose_name=' القسم')
    title = models.ForeignKey('Title', on_delete=models.SET_NULL, null=True,verbose_name='عنوان الوظيفة ')
    level = models.ForeignKey('Career_Level',on_delete=models.SET_NULL, null=True,verbose_name='  مستوى الخبرة')
    experience_min = models.IntegerField(blank=True,verbose_name='الخبرة من')
    experience_max = models.IntegerField(blank=True,verbose_name='الخبرة الى ')
    Education = models.ForeignKey(Degree,on_delete=models.SET_NULL, null=True,verbose_name='الدرجة العلمية ')
    language = models.ManyToManyField('Language', null=True,verbose_name='اللغة ')
    required_competencies = models.TextField(max_length=3000,verbose_name='المهارات المطلوبة ')
    other = models.TextField(max_length=3000,verbose_name=' مهارات أخرى ')

    class Meta:
        verbose_name = _(' طلب وظيفة  ')
        verbose_name_plural = _(' طلب وظيفة  ')





