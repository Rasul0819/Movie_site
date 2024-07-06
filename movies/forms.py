from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . import models
from django.contrib.auth.models import User
class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]
        

        