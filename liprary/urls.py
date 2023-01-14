from django.contrib import admin
from django.urls import path
from .views import Home,add_book,all_books,book_detail,edit_book,del_book,about

urlpatterns = [
    path('home', Home),
    path('about', about),
    path('books', all_books),
    path('books/add',add_book),
    path('books/<slug:book_slug>', book_detail),
    path('books/<slug:book_slug>/edit', edit_book),
    path('books/<slug:book_slug>/del', del_book),
]
