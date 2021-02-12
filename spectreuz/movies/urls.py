# ushbu sahifa yaratilgan.

from django.urls import path

# movies appning views.py dagi home funksiyasini chaqirilmoqda.

from . import views


urlpatterns = [

    path('', views.home, name='movies-index'),
    path('movies', views.movies, name="movies-page"),
    path('treller', views.treller, name="trellers-page"),
    path('aboutus', views.aboutus, name='about-us'),
    path('topmovies', views.topmovies, name="topmovi-page")

]
