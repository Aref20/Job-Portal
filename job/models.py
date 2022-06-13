from django.db import models

# Create your models here.

class Job(models.Model):
    job_title = models.CharField(max_length=300)
    job_description = models.TextField(max_length=5000)
    job_department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    job_post_date = models.DateTimeField(auto_now_add=True)
    job_vacancy = models.IntegerField(default=0, null=True,blank=True)
    job_salary = models.IntegerField(default=0, null=True,blank=True)
    job_location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    job_experience_min = models.IntegerField(default=0, null=True,blank=True)
    job_experience_max = models.IntegerField(default=0, null=True,blank=True)
    job_nature = models.CharField(max_length=100, null=True,blank=True)

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
