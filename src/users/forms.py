from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
