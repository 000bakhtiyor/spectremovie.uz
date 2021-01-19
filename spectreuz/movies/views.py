from django.shortcuts import render

from .models import *

# Create your views here.

def home(request):

    context = {

    "Slider"  : Slider.objects.all(),
    "Movies"  : Movies.objects.all(),
    "Premyera": Premyera.objects.all(),
    "PostsForMainMenu" : PostsForMainMenu.objects.all(),

    }


    return render(request, 'index.html', context)