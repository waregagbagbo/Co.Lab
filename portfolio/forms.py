# import the user contact model
from .models import *
# import the form fields from the model
from django.forms import ModelForm


class ContactForm(ModelForm):
        
    class Meta:
        model = Contact
        fields = ['name','email','message']
        