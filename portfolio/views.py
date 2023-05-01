from django.shortcuts import render, HttpResponse
# Create your views here.
# create the views

def index(request):
    #return HttpResponse('This is my home')
    return render(request,'pages/index.html')
