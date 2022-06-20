from enum import Enum
from django.db import models

# Create your models here.


class Status(Enum):

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class Job(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=3000)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField(auto_now_add=True)
    vacancy = models.IntegerField(blank=True)
    salary = models.IntegerField( blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    experience_min = models.IntegerField(blank=True)
    experience_max = models.IntegerField(blank=True)
    nature = models.ForeignKey('Nature', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=Status.choices(),default=Status.ACTIVE)

    def __str__(self):
        return self.title

    

class Department(models.Model):
    department_name = models.CharField(max_length=300)

    def __str__(self):
        return self.department_name


class Location(models.Model):
    location_name = models.CharField(max_length=300)

    def __str__(self):
        return self.location_name

class Nature(models.Model):
    Nature_name = models.CharField(max_length=300)

    def __str__(self):
        return self.Nature_name



