from django.shortcuts import render
from django.views.generic import CreateView
from application.models import Application
from .forms import ApplicationForm
# Create your views here.

class ApplicationCreateView(CreateView):
    model = Application
    #fields = '__all__'
    template_name = 'apply.html'
    success_url = '../'
    form_class = ApplicationForm


