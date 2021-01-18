from django.shortcuts import render

from .models import Slider

# Create your views here.

def home(request):

    slides = {

    "Slider": Slider.objects.all()

    }


    return render(request, 'index.html', slides)