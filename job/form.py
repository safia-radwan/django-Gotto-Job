from django import forms

from .models import  applyer ,job

class applyform(forms.ModelForm):
    class Meta:
        model=applyer
        fields=['name','age','Email','cv','cover_letter']

class jobform(forms.ModelForm):
    class Meta:
        model=job
        fields='__all__'
        exclude=('slug','owner')