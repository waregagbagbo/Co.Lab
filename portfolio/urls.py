from .import views # imports the views function
from django.urls import path # fetches the path from the settings


# set the urls 
urlpatterns = [
    path('',views.index, name="index"),
    path('jokes',views.jokes, name="jokes"),
   #path('projects', views.about, name="projects"),
   #path('contact', views.contact, name="contact"),
      
]
