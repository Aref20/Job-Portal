from django.shortcuts import render
from django.views.generic import CreateView
from application.models import Application
from .forms import ApplicationForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
# Create your views here.

class ApplicationCreateView(CreateView):
    model = Application
    #fields = '__all__'
    template_name = 'apply.html'
    success_url = '../'
    form_class = ApplicationForm
    def get_form(self):
        form = super().get_form()
        form.fields['Application_Birth_Date'].widget = DateTimePickerInput()
        return form
    



