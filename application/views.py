from django.shortcuts import render
from django.views.generic import CreateView
from application.models import Application,Qualification
from .forms import ApplicationForm
from job.models import Job
from django.shortcuts import get_object_or_404
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory

# Create your views here.


class QualificationInline(InlineFormSetFactory):
    model = Qualification
    fields = '__all__'

class ApplicationCreateView(CreateWithInlinesView):
    model = Application
    inlines = [QualificationInline,]
    #fields = '__all__'
    template_name = 'apply.html'
    success_url = '../'
    form_class = ApplicationForm
    

    #def get_context_data(self, **kwargs):
        #context = get_object_or_404(Job, pk=self.kwargs['job_id'])
        #kwargs['context'] = context
        #return super().get_context_data(**kwargs)


    def dispatch(self, request, *args, **kwargs):
     self.Job_App = Job.objects.values_list('id').filter(pk=kwargs['job_id'])
     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):#used to submit email
     form.instance.Job_App_id =self.Job_App 
     return super().form_valid(form)





    



