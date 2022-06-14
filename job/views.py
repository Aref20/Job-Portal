from django.shortcuts import render

from django.views.generic import ListView,DetailView

from job.models import Job

# Create your views here.
class JobsListView(ListView):
        model = Job
        context_object_name = 'jobs_list'
        template_name = 'index.html'
        paginate_by = 5
        


class JobDetailView(DetailView):
        model = Job
        context_object_name = 'job'
        template_name = 'job_detail.html'
