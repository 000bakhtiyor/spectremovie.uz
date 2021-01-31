from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.

def home(request):

    context = {

    "Movies"  : Movies.objects.all()[0:5],
    }


    return render(request, 'movies/index.html', context)
    



def movies(request):
    context = {
        "action_movies":Movies.objects.all()[Movies.objects.all().genre=="1"]
    }
    return render(request, "movies/movies.html", context)

def treller(request):
    return render(request, 'movies/treller.html')


def aboutus(request):

	return render(request, 'movies/about-us.html')