from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter
app_name = 'apps.api'


router = SimpleRouter()
router.register("jobs", JobViewSet, basename="jobs")



urlpatterns = [
path("profile/<int:pk>", ProfileAPIListView.as_view(), name="profile_list"),
]

urlpatterns += router.urls