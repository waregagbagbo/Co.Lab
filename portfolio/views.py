import json
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
import urllib.request
from .forms import ContactForm
from .models import *
# create the views

def index(request): # home view
    return render(request,'pages/index.html')


def about(request):  # about view
    return render(request,'pages/about.html')


def projects(request): # projects view
    return render(request,'pages/about.html')


def contact(request):
    # get / initializesource  a post request from the user
    if request.method == 'POST':
        # create an instance of the class/object
        fom = ContactForm(request.POST)
        # check validity of the object form
        if fom.is_valid():
            # do something
            fom.save()
            return HttpResponse('Thank you')
        else:
            fom = ContactForm() # returns a GET request
        context ={
            'fom':fom,
        }
        
    return render(request,'pages/contact.html',context)


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
        


