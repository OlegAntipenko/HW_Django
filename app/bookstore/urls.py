from django.urls import path
from bookstore.views import *

urlpatterns = [
    path('books/books_list/', books_list, name="books"),
    path('books/<int:index>/', book, name="book"),
    path('books/addbook/', add_book, name="addbook"),
    path('books/author/<int:index>/', author, name="author"),
    path('books/author_list/<int:index>/', author_list, name="author_list"),
]