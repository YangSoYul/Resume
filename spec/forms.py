from django.forms import widgets
from .models import applicant
from django import forms

class CreateApplyForm(forms.ModelForm):
    class Meta:
        model = applicant
        fields = ['name','age','introduce','gender','photo']
        widgets={
            'name':forms.TextInput(
                attrs={
                    'class':'form-control'
            }
        ),
            'age':forms.TextInput(
                attrs={
                    'class':'form-control'
            }
        ),
            'introduce':forms.Textarea(
                attrs={
                    'class':'form-control'
            }
        ),
    }