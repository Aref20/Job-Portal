from django.urls import path
from . import views
from application.views import ApplicationCreateView
urlpatterns = [
    #path('apply/<int:pk>', ApplicationCreateView.as_view(), name='apply'),
]