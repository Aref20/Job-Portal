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
from application.views import *



# customizing admin interface
admin.site.site_header = 'نظام التوظيف ألإلكتروني'
admin.site.site_title = ' نظام التوظيف'
admin.site.index_title = ' نظام التوظيف'

urlpatterns = [

    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', include('django_admin_filter.urls')),
    path('admin/', admin.site.urls),
    path('apply/',ApplicationFormCreateView.as_view() ,name='applyform'),
    path('jobs/', include('job.urls')),
    path('application/', include('application.urls')),
    path('', RedirectView.as_view(url='jobs/', permanent=True)),
    path('editor/', include('django_summernote.urls')),
    path('chaining/', include('smart_selects.urls')),


]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
