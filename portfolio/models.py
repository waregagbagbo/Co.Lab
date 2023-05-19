from django.db import models
# create contact form model

class Contact(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20)
    message = models.TextField(blank=False, null=True, max_length=100)
    
    class Meta:
        verbose_name_plural = 'contact'
        
    def __str__(self):
        #return self.name
        return '%s %s' % (self.name, self.email)

class Projects(models.Model):
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='static/images/', null=True)
    
    class Meta:
        verbose_name = 'Projects'
        
    def __str__(self):
        return '%s %s' % (self.title, self.description)