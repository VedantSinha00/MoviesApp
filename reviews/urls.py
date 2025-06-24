from django.urls import path
from . import views
from .views import (
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)


urlpatterns = [
    path('create/<int:movie_id>/', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]