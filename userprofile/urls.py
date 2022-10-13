
from django.urls import path
from django.contrib.auth import views as auth_views
from userprofile.views import Profile


app_name = 'userprofile'
urlpatterns = [
path('profile/<int:pk>', Profile.as_view(),name="Profile"),
    
]