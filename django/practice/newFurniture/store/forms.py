from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=UserRegister
        fields=('username','mobile','password','confirmPassword')

class feedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'