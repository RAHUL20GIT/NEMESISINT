from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import NewUser


class CreateUserForm(UserCreationForm):

    address = forms.CharField(max_length=100)
    class Meta:
        model=NewUser
        fields=('username','email','password1','password2','address')




