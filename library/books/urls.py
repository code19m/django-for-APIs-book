from django.urls import path

from books.models import Book
from .views import BookListView


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]