from django.db import models

# Create your models here.




class Movies(models.Model):
    genre_choices = ( 
    ("1", "Action"), 
    ("2", "Comedy"), 
    ("3", "Drama"), 
    ("4", "Fantasy"), 
    ("5", "Mystery"), 
    ("6", "Romance"), 
    ("7", "Horror"), 
    ("8", "Teen"),
)     


    caption = models.CharField(max_length=100)
    movie = models.FileField(upload_to="videos/") 
    details = models.TextField(blank=True)
    genre = models.CharField(max_length=20, choices=genre_choices, default="1")
    poster = models.ImageField(upload_to="posters/", default="/media/card.jfif")


    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
        
    def __str__(self):
        return self.caption     




class CardsForTrailer(models.Model):        
    card_caption = models.CharField(max_length=200)
    card_image = models.ImageField(upload_to='images/imagesforcards/')

    def __str__(self):
        return self.card_caption