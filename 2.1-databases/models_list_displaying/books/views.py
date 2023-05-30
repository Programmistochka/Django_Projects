from django.shortcuts import render, redirect
from .models import Book


def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def book_info(request, pub_date):
    template = 'books/book_inf.html'
    book = Book.objects.get(pub_date=pub_date)
    context = {'book': book}
    return render(request, template, context)