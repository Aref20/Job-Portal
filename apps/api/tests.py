from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from job.models import *
from django.contrib.auth.models import Group,User
class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.job = Job.objects.create(
        title=Title.objects.get(id=1),
        post_date='2022-1-1',
        vacancy="1",
        salary="1325",
        Education=Degree.objects.get(id=1),
        department=Group.objects.get(id=1),
        location="Jordan",
        experience_min="2",
        experience_max="4",
        nature="Full Time",
        langs=Language.objects.get(id=1),
        status="ACTIVE",
        expiration_date='2022-1-1',
        required_competencies="9781735467221",
        Career_Level=Career_Level.objects.get(id=1),
        other="9781735467221",
        created_by=User.objects.get(id=1),
        )
    def test_api_listview(self):
        response = self.client.get(reverse("job_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Job.objects.count(), 1)
        self.assertContains(response, self.job)