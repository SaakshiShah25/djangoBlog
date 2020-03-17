from django import forms
from django.forms import ModelForm
from .models import Add

class AddForm(forms.ModelForm):
    class Meta:
        model =Add
        fields=[
            'title',
            'author',
            'content',
            #'img',
        ]
    
    