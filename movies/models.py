from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release = models.DateField()
    poster = models.ImageField(default='default_poster.jpg', upload_to='posters/')
    genre = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.pk})
    
