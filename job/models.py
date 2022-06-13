from enum import Enum
from django.db import models

# Create your models here.


class Job_Status(Enum):

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class Job(models.Model):
    job_title = models.CharField(max_length=300)
    job_description = models.TextField(max_length=5000)
    job_department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    job_post_date = models.DateField(auto_now_add=True)
    job_vacancy = models.IntegerField(default=0, null=True,blank=True)
    job_salary = models.IntegerField(default=0, null=True,blank=True)
    job_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    job_experience_min = models.IntegerField(default=0, null=True,blank=True)
    job_experience_max = models.IntegerField(default=0, null=True,blank=True)
    job_nature = models.ForeignKey('Job_Nature', on_delete=models.SET_NULL, null=True)
    job_status = models.CharField(max_length=255, choices=Job_Status.choices(),default=Job_Status.ACTIVE)

    def __str__(self):
        return self.job_title

    

class Department(models.Model):
    department_name = models.CharField(max_length=300)

    def __str__(self):
        return self.department_name


class Location(models.Model):
    location_name = models.CharField(max_length=300)

    def __str__(self):
        return self.location_name

class Job_Nature(models.Model):
    Job_Nature_name = models.CharField(max_length=300)

    def __str__(self):
        return self.Job_Nature_name



