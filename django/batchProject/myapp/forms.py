from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=user_register
        fields='__all__'

class NotesForm(forms.ModelForm):
    class Meta:
        model=NotesClass
        fields='__all__'
