import json
from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponseRedirect
import urllib.request
from .forms import ContactMeForm
from .models import Contact, Project
from django.contrib import messages # for messaging
import requests
from django.core.mail import send_mail, BadHeaderError



# create the views
def index(request):
    if request.method == 'GET':
        # create an instance of the class/object 
        form = ContactMeForm()
    else:
        form = ContactMeForm(request.POST)
    # check validity of the object form
        if form.is_valid():
            # do something
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name,email,message, ["admin@example.com"])
                
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponse("success")
        
    return render(request,'pages/index.html',{'form':form})



def jokes(request):
    url ="https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
	"X-RapidAPI-Key": "8ad0683ba1msh4c14b47abe52a3bp1608f0jsn7fcfea9b9564",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
 }
    response = requests.get(url, headers=headers).text
    #final_response = print(response.json())           
    context ={
        "final_response":response,
    }    
    return render(request,'pages/jokes.html',context)
     