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
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
        widgets = {'text':
                   forms.Textarea(
                       attrs={'class':'form_control',
                              'rows':3,
                              'placeholder':'Ваш коммент...'})},
        labels = {'text':''}

        