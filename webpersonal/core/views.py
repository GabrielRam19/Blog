from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'about.html')

def contacto(request):
    return render(request,'contact.html')