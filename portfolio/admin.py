from django.contrib import admin
from .models import Contact,Project

# Register your models here.
class ContactAdminModel(admin.ModelAdmin):
    list_display = ('name','email','message')
    
class ProjectsAdminModel(admin.ModelAdmin):
    list_display =('title','description')

admin.site.register(Contact, ContactAdminModel)  # register your tables in the admin dashboard
admin.site.register(Project, ProjectsAdminModel)