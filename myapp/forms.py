# myapp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
