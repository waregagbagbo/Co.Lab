import json
from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponseRedirect
import urllib.request
from .forms import ContactMeForm
from .models import Contact, Project
from django.contrib import messages # for messaging
import requests



# create the views
def index(request):
    queryset = Project.objects.all()
    if request.method == 'POST':
        # create an instance of the class/object 
        form = ContactMeForm(request.POST)
        # check validity of the object form
        if form.is_valid():
            # do something
            form.save()
            messages.success(request, 'Your object has been saved.')        
            return redirect('/')
    else:
        form = ContactMeForm() # returns a GET request
    return render(request,'pages/index.html',{'form':form})



def jokes(request):
    url ="https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
	"X-RapidAPI-Key": "8ad0683ba1msh4c14b47abe52a3bp1608f0jsn7fcfea9b9564",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
 }
    response = requests.get(url, headers=headers)
    final_response = print(response.json())           
    context ={
        "final":final_response,
    }    
    return render(request,'pages/jokes.html',context)
     