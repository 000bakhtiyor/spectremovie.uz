from django.db import models

# Create your models here.

class Slider(models.Model):

    slider_title = models.CharField(max_length=100)
    caption = models.TextField()
    slider_image = models.ImageField(upload_to ='images/')

    def __str__(self):
        
        return str(self.id) + self.slider_title