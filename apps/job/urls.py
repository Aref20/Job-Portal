from django.urls import path

from apps.job.views import JobsListView, JobDetailView
from apps.application.views import *

app_name = 'apps.job'
urlpatterns = [
    path('', JobsListView.as_view(), name='jobs'),
    path('<int:pk>', CreateViewApplication.as_view(), name='job_detail'),
]