from django import forms
from .models import *
from django.forms.models import inlineformset_factory

    


class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):
    #username = forms.CharField(max_length=32,widget=forms.TextInput(attrs={'disabled': True}))
    #first_name = forms.CharField(max_length=32,widget=forms.TextInput(attrs={'placeholder':' الاسم: (ثلاث مقاطع) ', 'class': 'form-control'}))
    #email = forms.EmailField(max_length=64,widget=forms.TextInput(attrs={'placeholder':' البريد الإلكتروني ', 'class': 'form-control','type':'email'}))
    class Meta:
        model = UserProfile
        fields = '__all__'
        User = forms.CharField(disabled=True)
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




class QualificationForm(forms.ModelForm):

        class Meta:
            model = Qualification
            fields = '__all__'
            widgets = {
                'Degree': forms.TextInput(attrs={'placeholder':' المؤهل العلمي ', 'class': 'form-control','required': True}),
                'University': forms.TextInput(attrs={'placeholder':'اسم الجامعة/الكلية/المدرسة ', 'class': 'form-control','required': True}),
                'Graduation_Date': forms.DateInput(attrs={'placeholder':'تاريخ التخرج  ', 'class': 'date form-control','required': True}),
                'Major': forms.TextInput(attrs={'placeholder':'التخصص  ', 'class': 'form-control','required': True}),

            }

class LanguageForm(forms.ModelForm):

        class Meta:
            model = Language
            fields = '__all__'
            widgets = {
                'Language_Name': forms.Select(attrs={'class': 'form-select','required': True}),
                'Type_Conversation': forms.Select(attrs={'class': 'form-select'}),
                'Type_Writing': forms.Select(attrs={ 'class': 'form-select'}),
                'Type_Reading': forms.Select(attrs={ 'class': 'form-select'}),
            }

class Computer_SkillForm(forms.ModelForm):

        class Meta:
            model = Computer_Skill
            fields = '__all__'
            widgets = {
                'Skill': forms.TextInput(attrs={'class': 'form-control','required': True}),
                'Level': forms.Select(attrs={ 'class': 'form-select'}),

            }

class Previous_CompanyForm(forms.ModelForm):

        class Meta:
            model = Previous_Company
            
            fields = '__all__'
            exclude = ('Previous_Company_Profile','id',)
            widgets = {

                'Name': forms.TextInput(attrs={'placeholder':' إسم الشركة السابقة', 'class': 'form-control','required': True}),
                'Address': forms.TextInput(attrs={'placeholder':' عنوان الشركة السابقة', 'class': 'form-control','required': True}),
                'Phone': forms.NumberInput(attrs={'placeholder':' رقم الهاتف', 'class': 'form-control','required': True}),
                'Duration_From':forms.DateInput(attrs={'class': 'date form-control','required': True}),
                'Duration_To': forms.DateInput(attrs={ 'class': 'date form-control','required': True}),
                'Position': forms.TextInput(attrs={'placeholder':' المسمى الوظيفي', 'class': 'form-control','required': True}),
                'Start_Salary': forms.NumberInput(attrs={'placeholder':' الراتب عند البداية', 'class': 'form-control','required': True}),
                'Last_Salary': forms.NumberInput(attrs={'placeholder':' الراتب عند النهاية', 'class': 'form-control','required': True}),
                'Maneger': forms.TextInput(attrs={'placeholder':' إسم المدير السابق', 'class': 'form-control','required': True}),
                'Reason': forms.Textarea(attrs={'placeholder':' سبب ترك العمل', 'class': 'form-control','required': True}),
            }



class TrainingForm(forms.ModelForm):

        class Meta:
            model = Training
            fields = '__all__'
            widgets = {
                'Name': forms.TextInput(attrs={'placeholder':' اسم الدورة التدريبية', 'class': 'form-control','required': True}),
                'Duration_From': forms.DateInput(attrs={'placeholder':' تاريخ بدء الدورة ', 'class': ' date form-control','required': True}),
                'Duration_To': forms.DateInput(attrs={'placeholder':'  تاريخ إنتهاء الدورة', 'class': ' date form-control','required': True}),
                'Location': forms.TextInput(attrs={'placeholder':' مكان انعقاد الدورة', 'class': 'form-control','required': True}),
                'Institute': forms.TextInput(attrs={'placeholder':' الجهة التدريبية', 'class': 'form-control','required': True}),
            }

class Previous_CoworkerForm(forms.ModelForm):

        class Meta:
            model = Previous_Coworker
            fields = '__all__'
            widgets = {
                'Name': forms.TextInput(attrs={ 'placeholder':'  إسم المعرف','class': 'form-control','required': True}),
                'Address': forms.TextInput(attrs={ 'placeholder':' عنوان لبمعرف','class': 'form-control','required': True}),
                'Phone': forms.NumberInput(attrs={ 'placeholder':' رقم  المعرف','class': 'form-control','required': True}),
                'Position': forms.TextInput(attrs={ 'placeholder':' المسمى الوظيفي للمعرف','class': 'form-control','required': True}),
            }



ProfileQualificationFormSet = inlineformset_factory(
     UserProfile, Qualification, form=QualificationForm,
      extra=1, can_delete=True
     )

ProfileLanguageFormSet = inlineformset_factory(
     UserProfile, Language, form=LanguageForm,
      extra=1, can_delete=True
     )

ProfileComputer_SkillFormSet = inlineformset_factory(
     UserProfile, Computer_Skill, form=Computer_SkillForm,
      extra=1, can_delete=True
     )

ProfilePrevious_CompanyFormSet = inlineformset_factory(
     UserProfile, Previous_Company, form=Previous_CompanyForm,
      extra=1, can_delete=True
     )

ProfileTrainingFormSet = inlineformset_factory(
     UserProfile, Training, form=TrainingForm,
     extra=1, can_delete=True
     )

ProfilePrevious_CoworkerFormSet = inlineformset_factory(
     UserProfile, Previous_Coworker, form=Previous_CoworkerForm,
      extra=1, can_delete=True
     )















