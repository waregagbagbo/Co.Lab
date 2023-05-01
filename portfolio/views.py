from django.shortcuts import render, HttpResponse
# Create your views here.
# create the views

def index(request): # home view
    return render(request,'pages/index.html')


def about(request):  # about view
    return render(request,'pages/about.html')


def projects(request): # projects view
    return render(request,'pages/about.html')


def contact(request):
    return render(request,'pages/contact.html')


def podcasts(request):
    return render(request,'pages/podcasts.html')



