
from django.urls import path
from django.contrib.auth import views as auth_views
from userprofile.views import *


app_name = 'userprofile'
urlpatterns = [
path('',Profile.as_view(),name="profile"),
    
]