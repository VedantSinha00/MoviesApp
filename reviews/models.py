from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from django.urls import reverse

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - {self.rating}'
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.movie.pk})
    
