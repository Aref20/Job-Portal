
from application.models import Application
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
        'Application_NID': forms.TextInput(attrs={'placeholder':'الرقم الوطني ', 'class': 'form-control'}),
        'Application_Name': forms.TextInput(attrs={'placeholder':' الاسم: (ثلاث مقاطع) ', 'class': 'form-control'}),
        'Application_Email': forms.TextInput(attrs={'placeholder':' البريد الإلكتروني ', 'class': 'form-control','type':'email'}),
        'Application_Birth_Date': DateTimePickerInput(),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة  ', 'class': 'form-control'}),
        'Application_Location': forms.TextInput(attrs={'placeholder':'الموقع  ', 'class': 'form-control'}),
        'Application_Phone_Num': forms.TextInput(attrs={'placeholder':'الخلوي  ', 'class': 'form-control'}),
        'Application_Nationality': forms.TextInput(attrs={'placeholder':'الجنسية  ', 'class': 'form-control'}),
        'Application_Car_License': forms.Select(attrs={'class':'form-control'}),
        'Application_Socility_Status': forms.Select(attrs={'class':'form-control'}),
        'Application_Have_Car': forms.Select(attrs={'class':'form-control'}),
        'Application_Birth_Location': forms.TextInput(attrs={'placeholder':' مكان الولادة  ', 'class': 'form-control'}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة', 'class': 'form-control'}),
        'Application_Q_Degree': forms.TextInput(attrs={'placeholder':' الشهادة', 'class': 'form-control'}),
        'Application_Q_Major': forms.TextInput(attrs={'placeholder':' التخصص', 'class': 'form-control'}),
        'Application_Q_University': forms.TextInput(attrs={'placeholder':' الجامعة', 'class': 'form-control'}),
        'Application_Q_Graduation_Date': forms.TextInput(attrs={'placeholder':' تاريخ التخرج', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['Application_NID'].error_messages = {'required': 'FAS:DJFASKL:DJF'}


        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'The field ddd{fieldname} is required'.format(
                fieldname=field.label)}


