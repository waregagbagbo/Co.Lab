from django.db import models

# Create your models here.

# create contact form model

class Contact(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20)
    message = models.TextField(blank=False, null=True, max_length=100)
    
    class Meta:
        verbose_name_plural = 'contact'
        
    def __init__(self):
        return self.name, self.email
