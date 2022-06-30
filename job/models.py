from asyncio import create_task
from datetime import timezone
from .enum import *
from django.db import models
from django.contrib.auth.models import Group,User
from datetime import date, datetime    
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.




class Job(models.Model):
    title = models.ForeignKey('Title', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=3000)
    department = models.ForeignKey(Group,on_delete=models.SET_NULL, null=True,related_name="groub")
    #department_person = ChainedForeignKey(User, chained_field="department",chained_model_field="department",)# chaining fileds
    post_date = models.DateField(auto_now_add=True)
    vacancy = models.IntegerField(blank=True)
    salary = models.IntegerField( blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    experience_min = models.IntegerField(blank=True)
    experience_max = models.IntegerField(blank=True)
    nature = models.ForeignKey('Nature', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=Status.choices(),default=Status.ACTIVE)
    expiration_date = models.DateTimeField(default=datetime.now)
    



    #def save(self, *args, **kwargs):
        #if self.expiration_date >= datetime.now():
        #self.status = Status.INACTIVE
        


    def __str__(self):
        return self.title.name


    


class Location(models.Model):
    location_name = models.CharField(max_length=300)

    def __str__(self):
        return self.location_name

class Nature(models.Model):
    Nature_name = models.CharField(max_length=300)

    def __str__(self):
        return self.Nature_name

class Title(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name

#class Department_Person(models.Model):
   # DepartmentPerson= models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,related_name='DepartmentPerson')
   # name = models.CharField(max_length=300)
   # email = models.EmailField(max_length=300)



