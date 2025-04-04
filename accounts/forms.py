from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username')

class CustomPasswordChangeForm(PasswordChangeForm):
    pass

class CustomPasswordResetForm(PasswordResetForm):
    pass

class CustomSetPasswordForm(SetPasswordForm):
    pass