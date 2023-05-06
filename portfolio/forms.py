# import the user contact model
from .models import Contact
# import the form fields from the model
from django.forms import ModelForm


class ContactForm(ModelForm):
    # declare the fields
    
    class Meta:
        model = 'Contact'
        fields = '__all__'