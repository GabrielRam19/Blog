from django.shortcuts import render
from .models import project

# Create your views here.
def portafolio(request):
    proyecto=project.objects.all()
    return render(request,'portafolio.html',{'proyecto':proyecto})
