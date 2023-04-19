from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name' , 'last_name' ,'username' , 'email' , 'password')