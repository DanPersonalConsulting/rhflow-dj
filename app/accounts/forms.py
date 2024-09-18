from django import forms
from django.forms import ModelForm
from django import forms
from .models import User


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email',  'is_active', 'is_staff']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class UserAvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']