from .import views # imports the views function
from django.urls import path # fetches the path from the settings


# set the urls 
urlpatterns = [
    path('',views.index, name="index"),
    path('about', views.about, name="about"),
    path('projects', views.about, name="projects"),
    path('contact', views.about, name="contact"),
    path('podcasts',views.podcasts, name="podcasts"),
    
    
    
]
