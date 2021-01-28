from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.

def home(request):

    context = {

    "Movies"  : Movies.objects.all(),
    }


    return render(request, 'movies/index.html', context)
    

class MovieListView(ListView):
    model = Movies
    template_name = 'movies/movies.html'   
    context_object_name="movies" 


def treller(request):
    return render(request, 'movies/treller.html')