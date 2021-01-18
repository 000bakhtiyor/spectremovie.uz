from django.db import models

# Create your models here.

class Slider(models.Model):

    slider_title = models.CharField(max_length=100)
    caption = models.TextField()
    slider_image = models.ImageField(upload_to ='images/')

    def __str__(self):
        
        return str(self.id) + self.slider_title



class Movies(models.Model):
    caption = models.CharField(max_length=100)
    movie = models.FileField(upload_to="videos/") 
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