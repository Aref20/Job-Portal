
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
        'resume': forms.FileInput(attrs={ 'class': 'form-control'}),
        
        
        }




class QualificationForm(forms.ModelForm):

        class Meta:
            model = Qualification
            fields = '__all__'
            widgets = {
                'Degree': forms.TextInput(attrs={'placeholder':' المؤهل العلمي ', 'class': 'form-control','required': True}),
                'University': forms.TextInput(attrs={'placeholder':'اسم الجامعة/الكلية/المدرسة ', 'class': 'form-control'}),
                'Graduation_Date': forms.DateInput(attrs={'placeholder':'تاريخ التخرج  ', 'class': 'date form-control'}),
                'Major': forms.TextInput(attrs={'placeholder':'التخصص  ', 'class': 'form-control'}),

            }

class LanguageForm(forms.ModelForm):

        class Meta:
            model = Language
            fields = '__all__'
            widgets = {
                'Language_Name': forms.TextInput(attrs={'class': 'form-control'}),
                'Type_Conversation': forms.Select(attrs={'class': 'form-select'}),
                'Type_Writing': forms.Select(attrs={ 'class': 'form-select'}),
                'Type_Reading': forms.Select(attrs={ 'class': 'form-select'}),
            }

class Computer_SkillForm(forms.ModelForm):

        class Meta:
            model = Computer_Skill
            fields = '__all__'
            widgets = {
                'Skill': forms.TextInput(attrs={'class': 'form-control'}),
                'Level': forms.Select(attrs={ 'class': 'form-select'}),

            }

class Previous_CompanyForm(forms.ModelForm):

        class Meta:
            model = Previous_Company
            fields = '__all__'
            widgets = {

                'Name': forms.TextInput(attrs={'placeholder':' إسم الشركة السابقة', 'class': 'form-control'}),
                'Address': forms.TextInput(attrs={'placeholder':' عنوان الشركة السابقة', 'class': 'form-control'}),
                'Phone': forms.NumberInput(attrs={'placeholder':' رقم الهاتف', 'class': 'form-control'}),
                'Duration_From':forms.DateInput(attrs={'class': 'date form-control'}),
                'Duration_To': forms.DateInput(attrs={ 'class': 'date form-control'}),
                'Position': forms.TextInput(attrs={'placeholder':' المسمى الوظيفي', 'class': 'form-control'}),
                'Start_Salary': forms.NumberInput(attrs={'placeholder':' الراتب عند البداية', 'class': 'form-control'}),
                'Last_Salary': forms.NumberInput(attrs={'placeholder':' الراتب عند النهاية', 'class': 'form-control'}),
                'Reason': forms.Textarea(attrs={'placeholder':' سبب ترك العمل', 'class': 'form-control'}),
                'Maneger': forms.TextInput(attrs={'placeholder':' إسم المدير السابق', 'class': 'form-control'}),

            }


class TrainingForm(forms.ModelForm):

        class Meta:
            model = Training
            fields = '__all__'
            widgets = {
                'Name': forms.TextInput(attrs={'placeholder':' اسم الدورة التدريبية', 'class': 'form-control'}),
                'Duration_From': forms.DateInput(attrs={'placeholder':' تاريخ بدء الدورة ', 'class': ' date form-control'}),
                'Duration_To': forms.DateInput(attrs={'placeholder':'  تاريخ إنتهاء الدورة', 'class': ' date form-control'}),
                'Location': forms.TextInput(attrs={'placeholder':' مكان انعقاد الدورة', 'class': 'form-control'}),
                'Institute': forms.TextInput(attrs={'placeholder':' الجهة التدريبية', 'class': 'form-control'}),
            }

class Previous_CoworkerForm(forms.ModelForm):

        class Meta:
            model = Previous_Coworker
            fields = '__all__'
            widgets = {
                'Name': forms.TextInput(attrs={ 'placeholder':'  إسم المعرف','class': 'form-control'}),
                'Address': forms.TextInput(attrs={ 'placeholder':' عنوان لبمعرف','class': 'form-control'}),
                'Phone': forms.NumberInput(attrs={ 'placeholder':' رقم  المعرف','class': 'form-control'}),
                'Position': forms.TextInput(attrs={ 'placeholder':' المسمى الوظيفي للمعرف','class': 'form-control'}),
            }

ApplicationQualificationFormSet = inlineformset_factory(
     Application, Qualification, form=QualificationForm,
      #extra=2, can_delete=True
     )

ApplicationLanguageFormSet = inlineformset_factory(
     Application, Language, form=LanguageForm,
      extra=2, can_delete=True
     )

ApplicationComputer_SkillFormSet = inlineformset_factory(
     Application, Computer_Skill, form=Computer_SkillForm,
      extra=2, can_delete=True
     )

ApplicationPrevious_CompanyFormSet = inlineformset_factory(
     Application, Previous_Company, form=Previous_CompanyForm,
      extra=2, can_delete=True
     )

ApplicationTrainingFormSet = inlineformset_factory(
     Application, Training, form=TrainingForm,
     extra=2, can_delete=True
     )

ApplicationPrevious_CoworkerFormSet = inlineformset_factory(
     Application, Previous_Coworker, form=Previous_CoworkerForm,
      extra=2, can_delete=True
     )









   # def __init__(self, *args, **kwargs):
     #   super(ApplicationForm, self).__init__(*args, **kwargs)
        #self.fields['NID'].error_messages = {'required': 'FAS:DJFASKL:DJF'}


        # if you want to do it to all of them
     #   for field in self.fields.values():
     #       field.error_messages = {'required':'The field ddd{fieldname} is required'.format(
     #           fieldname=field.label)}


