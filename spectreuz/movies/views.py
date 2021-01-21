from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.

def home(request):

    context = {

    "Slider"  : Slider.objects.all(),
    "Movies"  : Movies.objects.all(),
    "Premyera": Premyera.objects.all(),
    "PostsForMainMenu" : PostsForMainMenu.objects.all(),

    }


    return render(request, 'movies/index.html', context)
    

class MovieListView(ListView):
    model = Movies
    template_name = 'movies/movies.html'   
    context_object_name="movies" 


      