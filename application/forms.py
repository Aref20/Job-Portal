
from application.models import Application
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
        'Application_NID': forms.TextInput(attrs={'placeholder':'الرقم الوطني ', 'class': 'form-control'}),
        'Application_Name': forms.TextInput(attrs={'placeholder':' الاسم: (ثلاث مقاطع) ', 'class': 'form-control'}),
        'Application_Email': forms.TextInput(attrs={'placeholder':' البريد الإلكتروني ', 'class': 'form-control','type':'email'}),
        'Application_Birth_Date': forms.DateInput(attrs={'class' :' date  form-control '}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة  ', 'class': 'form-control'}),
        'Application_Location': forms.TextInput(attrs={'placeholder':'الموقع  ', 'class': 'form-control'}),
        'Application_Phone_Num': forms.NumberInput(attrs={'placeholder':'الخلوي  ', 'class': 'form-control'}),
        'Application_Nationality': forms.TextInput(attrs={'placeholder':'الجنسية  ', 'class': 'form-control'}),
        'Application_Car_License': forms.Select(attrs={'class':'form-control'}),
        'Application_Socility_Status': forms.Select(attrs={'class':'form-control'}),
        'Application_Have_Car': forms.Select(attrs={'class':'form-control'}),
        'Application_Birth_Location': forms.TextInput(attrs={'placeholder':' مكان الولادة  ', 'class': 'form-control'}),
        'Application_City': forms.TextInput(attrs={'placeholder':' المحافظة', 'class': 'form-control'}),
        'Application_Q_Degree': forms.TextInput(attrs={'placeholder':' الشهادة', 'class': 'form-control'}),
        'Application_Q_Major': forms.TextInput(attrs={'placeholder':' التخصص', 'class': 'form-control'}),
        'Application_Q_University': forms.TextInput(attrs={'placeholder':' الجامعة', 'class': 'form-control'}),
        'Application_Q_Graduation_Date': forms.TextInput(attrs={'placeholder':' تاريخ التخرج', 'class': ' date form-control'}),
        'Application_L_Language': forms.Select(attrs={'class': 'form-control'}),
        'Application_L_Type_Conversation': forms.Select(attrs={'class': 'form-control'}),
        'Application_L_Type_Writing': forms.Select(attrs={ 'class': 'form-control'}),
        'Application_L_Type_Reading': forms.Select(attrs={ 'class': 'form-control'}),
        'Application_C_Computer_Skill': forms.TextInput(attrs={'class': 'form-control'}),
        'Application_C_Computer_Level': forms.Select(attrs={ 'class': 'form-control'}),

        'Application_Company_Prev_Name': forms.TextInput(attrs={'placeholder':' إسم الشركة السابقة', 'class': 'form-control'}),
        'Application_Company_Prev_Address': forms.TextInput(attrs={'placeholder':' عنوان الشركة السابقة', 'class': 'form-control'}),
        'Application_Company_Prev_Phone': forms.TextInput(attrs={'placeholder':' رقم الهاتف', 'class': 'form-control'}),
        'Application_Company_Prev_Duration_From':forms.DateInput(attrs={'placeholder':' تاريخ الإلتحاق بالشركة السابقة', 'class': 'date form-control'}),
        'Application_Company_Prev_Duration_To': forms.DateInput(attrs={'placeholder':' تاريخ المغادرة', 'class': 'date form-control'}),
        'Application_Company_Prev_Position': forms.TextInput(attrs={'placeholder':' المسمى الوظيفي', 'class': 'form-control'}),
        'Application_Company_Prev_Start_Salary': forms.TextInput(attrs={'placeholder':' الراتب عند البداية', 'class': 'form-control'}),
        'Application_Company_Prev_Last_Salary': forms.TextInput(attrs={'placeholder':' الراتب عند النهاية', 'class': 'form-control'}),
        'Application_Company_Prev_Reason': forms.Textarea(attrs={'placeholder':' سبب ترك العمل', 'class': 'form-control'}),
        'Application_Company_Prev_Maneger': forms.TextInput(attrs={'placeholder':' إسم المدير السابق', 'class': 'form-control'}),

        'Application_T_Training_Name': forms.TextInput(attrs={'placeholder':' اسم الدورة التدريبية', 'class': 'form-control'}),
        'Application_T_Training_Duration_From': forms.DateInput(attrs={'placeholder':' تاريخ بدء الدورة ', 'class': ' date form-control'}),
        'Application_T_Training_Duration_To': forms.DateInput(attrs={'placeholder':'  تاريخ إنتهاء الدورة', 'class': ' date form-control'}),
        'Application_T_Training_Location': forms.TextInput(attrs={'placeholder':' مكان انعقاد الدورة', 'class': 'form-control'}),
        'Application_T_Training_Institute': forms.TextInput(attrs={'placeholder':' الجهة التدريبية', 'class': 'form-control'}),

        'Application_Prev_Coworker_Name': forms.TextInput(attrs={ 'placeholder':'  إسم المعرف','class': 'form-control'}),
        'Application_Prev_Coworker_Address': forms.TextInput(attrs={ 'placeholder':' عنوان لبمعرف','class': 'form-control'}),
        'Application_Prev_Coworker_Phone': forms.TextInput(attrs={ 'placeholder':' رقم  المعرف','class': 'form-control'}),
        'Application_Prev_Coworker_Position': forms.TextInput(attrs={ 'placeholder':' المسمى الوظيفي للمعرف','class': 'form-control'}),
        'Application_Last_Job_Desc': forms.Textarea(attrs={ 'placeholder':'اشرح المهام الرئيسية التي كنت تؤديها في آخر وظيفة لك','class': 'form-control'}),


        'Application_Coworker_Ask': forms.Select(attrs={ 'class': 'form-control'}),

        'Application_Current_Salary': forms.TextInput(attrs={ 'class': 'form-control'}),
        'Application_Expected_Salary': forms.TextInput(attrs={ 'class': 'form-control'}),

        'Application_Available_Date': forms.DateInput(attrs={ 'class': ' date form-control'}),
        'Application_Relative_Frinds': forms.TextInput(attrs={ 'class': 'form-control'}),
        'Application_Relative_Frinds_Job': forms.TextInput(attrs={ 'class': 'form-control'}),
        'Application_Diseases': forms.Select(attrs={ 'class': 'form-control'}),


        
        
        }
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['Application_NID'].error_messages = {'required': 'FAS:DJFASKL:DJF'}


        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'The field ddd{fieldname} is required'.format(
                fieldname=field.label)}


