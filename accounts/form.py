from dataclasses import field
from django import forms
from .models import User


class RegisterUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['username','email','password','confirm_password']
        
    def clean(self):
        cleaned_data=super(RegisterUserForm,self).clean()
        password=cleaned_data['password']
        confirm_password=cleaned_data['confirm_password']
        if password!=confirm_password:
            raise forms.ValidationError('Password does not match.')