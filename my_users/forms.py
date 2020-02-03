from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
