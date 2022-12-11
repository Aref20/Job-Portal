from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = ['id','username', 'email','password1','password2']


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
          'username': forms.TextInput(attrs={'placeholder':'  إسم المستخدم ', 'class': 'form-control form-control-lg'}),
          'password': forms.TextInput(attrs={'placeholder':' كلمة السر', 'class': 'form-control form-control-lg'}),
        }

