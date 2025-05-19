from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Username...',
            'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password...',
            'class': 'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600'
        })
    )

# Custom validator for username
def validate_username(value):
    pattern = r'^[a-zA-Z0-9_]{5,20}$'
    if not re.match(pattern, value):
        raise ValidationError('Username must be 5-20 characters long and contain only letters, numbers, or underscores.')

# Custom validator for password
# Custom validator for password (updated with special character requirement)
def validate_password(value):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    if not re.match(pattern, value):
        raise ValidationError(
            'Password must be at least 8 characters long and contain at least one letter, one number, and one special character.'
        )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[validate_password]
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    username = forms.CharField(
        validators=[validate_username]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")
        
        return cleaned_data
