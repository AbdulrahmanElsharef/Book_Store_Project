from django.contrib import admin
from django.urls import path
from .views import all_books, book_detail, add_book, edit_book, del_book

urlpatterns = [

    path('books', all_books),
    path('books/add', add_book),
    path('books/<slug:book_slug>', book_detail),
    path('books/<slug:book_slug>/edit', edit_book),
    path('books/<slug:book_slug>/del', del_book),
]
