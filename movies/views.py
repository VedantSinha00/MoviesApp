from typing import Any
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView, 
                                    CreateView, 
                                    UpdateView,
                                    DeleteView)
from .models import Movie
from reviews.models import Review
from django import forms
from datetime import date


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/home.html'
    context_object_name = 'movies'
    ordering = ['-created']
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Movie.objects.filter(title__icontains=query).order_by('-created')
        return Movie.objects.all().order_by('-created')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['reviews']=Review.objects.filter(movie=self.object).order_by('-created')
        return context
    
class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'director', 'release', 'genre', 'description', 'poster']
    template_name = 'movies/movie_form.html'
    context_object_name = 'movie'

    def get_initial(self):
        initial = super().get_initial()
        initial['release'] = date.today()  # Set today's date as the initial value for release field
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['release'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['title', 'director', 'release', 'genre', 'description', 'poster']
    template_name = 'movies/movie_form.html'
    context_object_name = 'movie'

    def get_initial(self):
        initial = super().get_initial()
        initial['release'] = date.today()  # Set today's date as the initial value for release field
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['release'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.user:
            return True
        return False
    
class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    success_url = '/'

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.user:
            return True
        return False