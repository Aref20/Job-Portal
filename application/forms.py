
from application.models import *
#from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms
from django.forms.models import inlineformset_factory

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
        'NID': forms.NumberInput(attrs={'placeholder':'الرقم الوطني ', 'class': 'form-control'}),
        'Name': forms.TextInput(attrs={'placeholder':' الاسم: (ثلاث مقاطع) ', 'class': 'form-control'}),
        'Email': forms.TextInput(attrs={'placeholder':' البريد الإلكتروني ', 'class': 'form-control','type':'email'}),
        'Birth_Date': forms.DateInput(attrs={'class' :' date  form-control '}),
        'City': forms.TextInput(attrs={'placeholder':' المحافظة  ', 'class': 'form-control'}),
        'Location': forms.TextInput(attrs={'placeholder':'الموقع  ', 'class': 'form-control'}),
        'Phone_Num': forms.NumberInput(attrs={'placeholder':'الخلوي  ', 'class': 'form-control'}),
        'Nationality': forms.TextInput(attrs={'placeholder':'الجنسية  ', 'class': 'form-control'}),
        'Car_License': forms.Select(attrs={'class':'form-select'}),
        'Socility_Status': forms.Select(attrs={'class':' form-select'}),
        'Have_Car': forms.Select(attrs={'class':'form-select'}),
        'Birth_Location': forms.TextInput(attrs={'placeholder':' مكان الولادة  ', 'class': 'form-control'}),
        'City': forms.TextInput(attrs={'placeholder':' المحافظة', 'class': 'form-control'}),
        'Last_Job_Desc': forms.Textarea(attrs={ 'placeholder':'اشرح المهام الرئيسية التي كنت تؤديها في آخر وظيفة لك','class': 'form-control'}),
        'Coworker_Ask': forms.Select(attrs={ 'class': 'form-select'}),
        'Current_Salary': forms.NumberInput(attrs={ 'class': 'form-control'}),
        'Expected_Salary': forms.NumberInput(attrs={ 'class': 'form-control'}),
        'Available_Date': forms.DateInput(attrs={ 'class': ' date form-control'}),
        'Relative_Frinds': forms.Select(attrs={ 'class': 'form-select'}),
        'Relative_Frinds_Job': forms.TextInput(attrs={ 'class': 'form-control'}),
        'Diseases': forms.Select(attrs={ 'class': 'form-select'}),
        'Warranty': forms.Select(attrs={ 'class': 'form-select'}),
        'Car_License_Type': forms.Select(attrs={ 'class': 'form-select'}),
        'Experience_Years': forms.NumberInput(attrs={ 'class': 'form-control'}),
        'resume': forms.FileInput(attrs={ 'class': 'form-control'}),
        
        
        }
















 