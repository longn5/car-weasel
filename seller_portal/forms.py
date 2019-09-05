from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text='Required')
    bis_name = forms.CharField(max_length=100, help_text='Business Name')
    street = forms.CharField(max_length=100, help_text='Street')
    city = forms.CharField(max_length=100, help_text='City')
    state = forms.CharField(max_length=2, help_text='State (ex. WA)')
    zipcode = forms.CharField(max_length=5, help_text='Zipcode')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'bis_name',
            'street',
            'city',
            'state',
            'zipcode',
            'password1',
            'password2'
        )