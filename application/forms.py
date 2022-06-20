
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
       # 'Q_Degree': forms.TextInput(attrs={'placeholder':' الشهادة', 'class': 'form-control'}),
       # 'Q_Major': forms.TextInput(attrs={'placeholder':' التخصص', 'class': 'form-control'}),
       # 'Q_University': forms.TextInput(attrs={'placeholder':' الجامعة', 'class': 'form-control'}),
       # 'Q_Graduation_Date': forms.TextInput(attrs={'placeholder':' تاريخ التخرج', 'class': ' date form-control'}),
        'L_Language': forms.TextInput(attrs={'class': 'form-control'}),
        'L_Type_Conversation': forms.Select(attrs={'class': 'form-select'}),
        'L_Type_Writing': forms.Select(attrs={ 'class': 'form-select'}),
        'L_Type_Reading': forms.Select(attrs={ 'class': 'form-select'}),
        'C_Computer_Skill': forms.TextInput(attrs={'class': 'form-control'}),
        'C_Computer_Level': forms.Select(attrs={ 'class': 'form-select'}),

        'Company_Prev_Name': forms.TextInput(attrs={'placeholder':' إسم الشركة السابقة', 'class': 'form-control'}),
        'Company_Prev_Address': forms.TextInput(attrs={'placeholder':' عنوان الشركة السابقة', 'class': 'form-control'}),
        'Company_Prev_Phone': forms.TextInput(attrs={'placeholder':' رقم الهاتف', 'class': 'form-control'}),
        'Company_Prev_Duration_From':forms.DateInput(attrs={'class': 'date form-control'}),
        'Company_Prev_Duration_To': forms.DateInput(attrs={ 'class': 'date form-control'}),
        'Company_Prev_Position': forms.TextInput(attrs={'placeholder':' المسمى الوظيفي', 'class': 'form-control'}),
        'Company_Prev_Start_Salary': forms.TextInput(attrs={'placeholder':' الراتب عند البداية', 'class': 'form-control'}),
        'Company_Prev_Last_Salary': forms.TextInput(attrs={'placeholder':' الراتب عند النهاية', 'class': 'form-control'}),
        'Company_Prev_Reason': forms.Textarea(attrs={'placeholder':' سبب ترك العمل', 'class': 'form-control'}),
        'Company_Prev_Maneger': forms.TextInput(attrs={'placeholder':' إسم المدير السابق', 'class': 'form-control'}),

        'T_Training_Name': forms.TextInput(attrs={'placeholder':' اسم الدورة التدريبية', 'class': 'form-control'}),
        'T_Training_Duration_From': forms.DateInput(attrs={'placeholder':' تاريخ بدء الدورة ', 'class': ' date form-control'}),
        'T_Training_Duration_To': forms.DateInput(attrs={'placeholder':'  تاريخ إنتهاء الدورة', 'class': ' date form-control'}),
        'T_Training_Location': forms.TextInput(attrs={'placeholder':' مكان انعقاد الدورة', 'class': 'form-control'}),
        'T_Training_Institute': forms.TextInput(attrs={'placeholder':' الجهة التدريبية', 'class': 'form-control'}),

        'Prev_Coworker_Name': forms.TextInput(attrs={ 'placeholder':'  إسم المعرف','class': 'form-control'}),
        'Prev_Coworker_Address': forms.TextInput(attrs={ 'placeholder':' عنوان لبمعرف','class': 'form-control'}),
        'Prev_Coworker_Phone': forms.TextInput(attrs={ 'placeholder':' رقم  المعرف','class': 'form-control'}),
        'Prev_Coworker_Position': forms.TextInput(attrs={ 'placeholder':' المسمى الوظيفي للمعرف','class': 'form-control'}),
        'Last_Job_Desc': forms.Textarea(attrs={ 'placeholder':'اشرح المهام الرئيسية التي كنت تؤديها في آخر وظيفة لك','class': 'form-control'}),


        'Coworker_Ask': forms.Select(attrs={ 'class': 'form-select'}),

        'Current_Salary': forms.TextInput(attrs={ 'class': 'form-control'}),
        'Expected_Salary': forms.TextInput(attrs={ 'class': 'form-control'}),

        'Available_Date': forms.DateInput(attrs={ 'class': ' date form-control'}),
        'Relative_Frinds': forms.Select(attrs={ 'class': 'form-select'}),
        'Relative_Frinds_Job': forms.TextInput(attrs={ 'class': 'form-control'}),
        'Diseases': forms.Select(attrs={ 'class': 'form-select'}),


        
        
        }
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        #self.fields['NID'].error_messages = {'required': 'FAS:DJFASKL:DJF'}


        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'The field ddd{fieldname} is required'.format(
                fieldname=field.label)}


