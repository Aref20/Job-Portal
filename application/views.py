from django.shortcuts import render
from django.views.generic import CreateView
from application.models import Application
from .forms import ApplicationForm
from job.models import Job

# Create your views here.

class ApplicationCreateView(CreateView):
    model = Application
    #fields = '__all__'
    template_name = 'apply.html'
    success_url = '../'
    form_class = ApplicationForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobid"] = Job.id
        return context

    



