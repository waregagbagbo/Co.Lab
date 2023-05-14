import json
from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponseRedirect
import urllib.request
from .forms import ContactMeForm
from .models import  Contact
from django.contrib import messages # for messaging
import requests
from jokeapi import Jokes
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


def about(request):  # about view
    return render(request,'pages/about.html')


def projects(request): # projects view
    return render(request,'pages/about.html')


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


def weather(request): 
    if request.method == 'POST':
        # get the city name fro the api
        city = request.POST.get('London','True')
        
        # fetch informationusing the API
        source = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=3b8dc39f762c805cedd65b91051b5190").read()
  
        # convert json data file into python dict
        list_of_data = json.loads(source)
        
        # create dict and convert to string
        context ={
            'city': city,
            'country_code':str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon'])+ ''+ str(list_of_data['coord']['lat']),
            'temp': str(list_of_data['main']['temp']) + 'k',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),            
            
        }
    else:
        context ={}
        
    # push context dta to the template
    return render(request,'pages/weather.html', context)


def podcast(request):
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&type=single"
    querystring = {
                   "format":"json",
                   #"contains":"C%23",
                   "idRange":"0-150",
                   "amount": 6,
                   "blacklistFlags":"nsfw,racist"}
    
    

    #"X-RapidAPI-Key": "8ad0683ba1msh4c14b47abe52a3bp1608f0jsn7fcfea9b9564",
	#"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
    #}
    response = requests.get(url, params=querystring)
    data = response.json()
    context = {
        "data":data,
    }
    
    return render(request,'pages/podcast.html',context)
     