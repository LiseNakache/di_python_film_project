from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['username', 'first_name', 'last_name', 'email','password']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'signup-username',
        'placeholder': 'username',
        'required': True
      }),
      'password': forms.PasswordInput(attrs={
        'id': 'signup-password',
        'placeholder': 'password',
        'required': True
      }),
      'email': forms.EmailInput(attrs={
            'id': 'signup-password',
            'placeholder': 'email',
            'required': True
      }),
      'first_name': forms.TextInput(attrs={
        'id': 'signup-first_name',
        'placeholder': 'first name',
        'required': True
      }),
      'last_name': forms.TextInput(attrs={
        'id': 'signup-last_name',
        'placeholder': 'last name',
        'required': True
      })
    }

class LoginForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['username', 'password']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'login-username',
        'placeholder': 'username',
        'required': True
      }),
      'password': forms.PasswordInput(attrs={
        'id': 'login-password',
        'placeholder': 'password',
        'required': True
      })
    }