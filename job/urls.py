from django.urls import path

from job.views import JobsListView, JobDetailView
from application.views import *


urlpatterns = [
    path('', JobsListView.as_view(), name='jobs'),
    path('<int:pk>', PostCommentView.as_view(), name='job_detail'),
    #path('<int:pk>/apply', PostCommentView.as_view(), name='apply'),
    #path('UploadFile', views.UploadFile, name='UploadFile'),
]