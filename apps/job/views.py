from django.shortcuts import render

from django.views.generic import ListView,DetailView

from apps.job.models import Job

# Create your views here.
class JobsListView(ListView):
        model = Job
        context_object_name = 'jobs_list'
        template_name = 'index.html'
        paginate_by = 5


        def get_queryset(self):
            queryset = Job.objects.filter(status='ACTIVE')
            return queryset
        

        


class JobDetailView(DetailView):
        model = Job
        context_object_name = 'job'
        template_name = 'job_detail.html'

        def get_context_data(self, **kwargs):
               data = super().get_context_data(**kwargs)
               data['STATUS'] = Job.objects.filter(id=self.object.id).values_list('status',flat=True)[0]


               return data
