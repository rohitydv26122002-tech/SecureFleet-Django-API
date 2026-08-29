from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello, world. You are at my project home page")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("hello, world. You are at my project about page")


def contact(request):
    return HttpResponse("hello, world. You are at my project contact page")
