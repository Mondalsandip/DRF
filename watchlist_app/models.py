from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_publish_date=models.DateField(auto_now_add=True)
# class Like(Page):
#     likes=models.IntegerField()



class StreamPlatform(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return self.name




class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform=models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title
    