# ushbu sahifa yaratilgan.

from django.urls import path

# movies appning views.py dagi home funksiyasini chaqirilmoqda.

from . import views
from .views import MovieListView

urlpatterns = [

    path('', views.home, name='movies-index'),
    path('movies', MovieListView.as_view(), name="movies-page"),
    path('treller', views.treller, name="trellers-page"),
    path('aboutus', views.aboutus, name='about-us'),

]
