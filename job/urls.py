from django.urls import path

from job.views import JobsListView, JobDetailView
from application.views import ApplicationCreateView

urlpatterns = [
    path('', JobsListView.as_view(), name='jobs'),
    path('<int:pk>', JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/apply', ApplicationCreateView.as_view(), name='apply'),
    #path('UploadFile', views.UploadFile, name='UploadFile'),
]