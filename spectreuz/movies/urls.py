# ushbu sahifa yaratilgan.

from django.urls import path

# movies appning views.py dagi home funksiyasini chaqirilmoqda.

from . import views


urlpatterns = [

    path('', views.home, name='movies-index'),
    path('movies', views.movies, name="movies-page"),
    path('treller', views.treller, name="trellers-page"),
    path('aboutus', views.aboutus, name='about-us'),
<<<<<<< HEAD
    path('topmovies', views.topmovies, name="topmovi-page")

=======
    path('topmovies', views.topmovies, name='top-movies')
>>>>>>> 9f1e15a30d4d3493d42176e09fd43a910da79d64
]
