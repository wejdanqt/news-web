from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()


class RegistrationForm(UserCreationForm):
    name = forms.CharField(label='Name')
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(
        label='Phone Number')
    national_id = forms.CharField(label='National Id')
    date_of_birth = forms.DateField(required=True, label='Date of Birth',
                                    widget=forms.DateInput(attrs={
                                        'placeholder': 'Birth Date',
                                        'class': 'form-control',
                                        'type': 'date',
                                    }))

    class Meta:
        model = get_user_model()
        fields = ['name', 'email', 'national_id', 'phone_number', 'date_of_birth',
                  'password1', 'password2']
