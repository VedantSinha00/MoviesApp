from django.urls import path
from .views import (
    MovieListView, 
    MovieDetailView, 
    MovieCreateView, 
    MovieUpdateView,
    MovieDeleteView
)
from . import views

urlpatterns = [
    path('', MovieListView.as_view(), name='movies-home'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/new/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),
]
