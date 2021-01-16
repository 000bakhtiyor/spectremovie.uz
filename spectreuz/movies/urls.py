# ushbu sahifa yaratilgan.

from django.urls import path

# movies appning views.py dagi home funksiyasini chaqirilmoqda.

from . import views

urlpatterns = [

    path('', views.home, name='movies-index')
]
