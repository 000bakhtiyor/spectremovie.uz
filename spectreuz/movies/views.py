from django.shortcuts import render

from .models import Slider, Movies

# Create your views here.

def home(request):

    context = {

    "Slider": Slider.objects.all(),
    "Movies": Movies.objects.all()

    }


    return render(request, 'index.html', context)