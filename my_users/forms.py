from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class MyUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        required=True
    )

    last_name = forms.CharField(
        label='Last Name',
        required=True
    )

    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]


class MyUserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]


class MyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
