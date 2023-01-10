from django.shortcuts import render

# Create your views here.

from .models import Book,cateogry


def all_books(request):
    all=Book.objects.all()
    context={'books':all}
    return render (request,'books.html',context)
