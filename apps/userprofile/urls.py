
from django.urls import path
from django.contrib.auth import views as auth_views
from apps.userprofile.views import Profile


app_name = 'apps.userprofile'
urlpatterns = [
path('profile/<int:pk>', Profile.as_view(),name="Profile"),
    
]