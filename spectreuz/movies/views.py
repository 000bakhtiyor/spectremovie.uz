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
        "action_movies":Movies.objects.all().filter(genre="1")[0:6]
    }
    return render(request, "movies/movies.html", context)

def treller(request):
    return render(request, 'movies/treller.html')


def aboutus(request):

	return render(request, 'movies/about-us.html')

def topmovies(request):
<<<<<<< HEAD
=======
    
>>>>>>> 9f1e15a30d4d3493d42176e09fd43a910da79d64

    return render(request, 'movies/top-movies.html')