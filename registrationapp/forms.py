from django import forms
from django.forms import ModelForm
from .models import User,Post

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email' , 'password')

class PostForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
            "placeholder":"Enter your post ",
            }
        ),                   
        label="",
    )
    class Meta:
        model = Post
        exclude = ("user",)