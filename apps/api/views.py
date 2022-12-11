from django.shortcuts import render
from rest_framework.generics import *
from rest_framework import permissions 
from apps.job.models import Job
from apps.userprofile.models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .permissions import *
# Create your views here.
# apis/views.py

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAdminOrReadOnlyJob,)


class ProfileAPIListView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthProfile,)
    serializer_class = ProfileSerializer

