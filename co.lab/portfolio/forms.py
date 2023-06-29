# import the user contact model
from .models import *
# import the form fields from the 
from django import forms
from django.forms import ModelForm


class ContactMeForm(forms.ModelForm):
        
    class Meta:
        model = Contact
        fields = ['name','email','message']
        