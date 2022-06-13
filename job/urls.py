from django.urls import path

from job.views import JobsListView, JobDetailView

urlpatterns = [
    path('', JobsListView.as_view(), name='jobs'),
    path('<int:pk>', JobDetailView.as_view(), name='job_detail'),
]