import json
from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponseRedirect
import urllib.request
from .forms import ContactMeForm
from .models import Contact, Project
from django.contrib import messages # for messaging
import requests
from jokeapi import Jokes
import asyncio


# create the views
def index(request):
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


def tools(request): # projects view
    Projects = Project.objects.all()
    
    return render(request,'pages/index.html')


def contact(request):
    # get / initializesource  a post request from the user
    '''if request.method == 'POST':
        # create an instance of the class/object
        form = ContactMeForm(request.POST)
        # check validity of the object form
        if form.is_valid():
            # do something
            form.save()
            return HttpResponseRedirect('Thank you')
    else:
        form = ContactMeForm() # returns a GET request
    return render(request,'pages/contact.html', {'form':form})'''


async def jokes(request):
    j = await Jokes()  # Initialise the class
    jok = await j.get_joke(category=['programming', 'christmas','dark'])  # Will return a joke that fits in either the programming or dark category.
    if jok["type"] == "single": # Print the joke
       print(jok["jok"])
    else:
        print(jok["setup"])
        print(jok["delivery"])    
    response = asyncio.run(jokes())        
    context ={
        "response":response,
    }    
    return render(request,'pages/jokes.html',context)
     