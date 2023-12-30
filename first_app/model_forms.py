from django import forms
from .import models
class ContactForms2(forms.ModelForm):
    class Meta:
        model=models.StudentModel
        fields="__all__"
