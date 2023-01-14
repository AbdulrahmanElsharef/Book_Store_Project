from django.shortcuts import render, redirect

# Create your views here.

from .models import Book, cateogry
from .forms import BookForms

def Home(request):
    # obj='book1'
    # context={'name':obj}
    return render(request,'index.html')

def about(request):
    # obj='book1'
    # context={'name':obj}
    return render(request,'about.html')


def all_books(request):
    all = Book.objects.all()
    context = {'books': all}
    return render(request, 'books.html', context)


def book_detail(request, book_slug):
    details = Book.objects.get(slug=book_slug)
    context = {"book": details}
    return render(request, 'book_detail.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BookForms()
    context = {'new': form}
    return render(request, 'add_book.html', context)


def edit_book(request, book_slug):
    details = Book.objects.get(slug=book_slug)
    if request.method == 'POST':
        form = BookForms(request.POST, request.FILES, instance=details)
        if form.is_valid():
            form.save()
    else:
        form = BookForms(instance=details)
    context = {'update': form}
    return render(request, 'edit_book.html', context)


def del_book(request, book_slug):
    details = Book.objects.get(slug=book_slug)
    details.delete()
    return redirect('/books')
