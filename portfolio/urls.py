from .import views
from django.urls import path


# set the urls 
urlpatterns = [
    path('',views.index, name="index")
]
