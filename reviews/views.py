from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import (ListView,
                                    DetailView, 
                                    CreateView, 
                                    UpdateView,
                                    DeleteView)
from .models import Review
from movies.models import Movie
from django.urls import reverse_lazy

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'reviews/review_form.html'
    context_object_name = 'review'

    def form_valid(self, form):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.get(pk=movie_id)
        form.instance.movie = movie 
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'reviews/review_form.html'
    context_object_name = 'review'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False
    
class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    context_object_name = 'review'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.movie.pk})
    

