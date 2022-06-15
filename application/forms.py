
from application.models import Application
from django import forms

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
        'Application_NID': forms.TextInput(attrs={'placeholder':'الرقم الوطني '}),
        'Application_Name': forms.TextInput(attrs={'placeholder':' الاسم: (ثلاث مقاطع) '}),
        'Application_Email': forms.TextInput(attrs={'placeholder':' البريد الإلكتروني '}),
        'Application_Birth_Date': forms.DateField(widget=forms.DateInput(attrs={'placeholder':'تاريخ الميلاد '})),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة  '}),
        'Application_Location': forms.TextInput(attrs={'placeholder':'الموقع  '}),
        'Application_Phone_Num': forms.TextInput(attrs={'placeholder':'الخلوي  '}),
        'Application_Nationality': forms.TextInput(attrs={'placeholder':'الجنسية  '}),
        'Application_Car_License': forms.Select(),
        'Application_Socility_Status': forms.Select(),
        'Application_Have_Car': forms.Select(),
        'Application_Birth_Location': forms.TextInput(attrs={'placeholder':' مكان الولادة  '}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة'}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة'}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة'}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة'}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة'}),
        }