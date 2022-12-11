"""JobApplicationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from apps.application.views import *
from apps.userprofile.views import Profile
from apps.userauth.views import *
from django.conf.urls.i18n import i18n_patterns
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView




# customizing admin interface
admin.site.site_header = 'نظام التوظيف ألإلكتروني'
admin.site.site_title = ' نظام التوظيف'
admin.site.index_title = ' نظام التوظيف'

urlpatterns = [


    path('admin/', include('django_admin_filter.urls')),
    path('admin/', admin.site.urls),
    path('jobs/', include('apps.job.urls')),
    path('application/', include('apps.application.urls')),
    path('', RedirectView.as_view(url='jobs/', permanent=True)),
    path('editor/', include('django_summernote.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('login/', include('apps.userauth.urls')),
    path('signup/', SignUpView.as_view(),name='signup' ),
    path('', include('django.contrib.auth.urls')),
    path('',include('apps.userprofile.urls')),
    #path("api/", include("apps.api.urls")),
    #path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    #path("api-auth/", include("rest_framework.urls")),
    #path("api/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    #path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    #path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
    #url_name="schema"), name="swagger-ui"),
    


    
    


]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    



