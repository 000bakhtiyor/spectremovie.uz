from django.db import models

# Create your models here.

class Slider(models.Model):

    slider_title = models.CharField(max_length=100)
    caption = models.TextField()
    slider_image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        
        return str(self.id) + self.slider_title



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


class Premyera(models.Model):

    premyera_caption = models.CharField(max_length=100)
    premyera_image = models.ImageField(upload_to ='images/premyera/')  

    def __str__(self):
        
        return str(self.id) + self.premyera_caption


class PostsForMainMenu(models.Model):
    
    post_title = models.CharField(max_length=40)
    post_author = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)
    post_description = models.TextField()
    post_full_description = models.TextField()
    post_image = models.ImageField(upload_to ='images/postsformainmenu/')

    def __str__(self):

        return self.post_title + " | " + self.post_author

class CardsForTrailer(models.Model):        
    card_caption = models.CharField(max_length=200)
    card_image = models.ImageField(upload_to='images/imagesforcards/')

    def __str__(self):
        return self.card_caption