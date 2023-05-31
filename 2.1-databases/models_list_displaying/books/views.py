from django.shortcuts import render, redirect
import datetime as DT
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
    try:
        pub_date = DT.datetime.strptime(request.GET.get("book"), '%Y-%m-%d').date()
    except BaseException:
        pub_date = pub_date
    book = Book.objects.get(pub_date=pub_date)
    prev_book = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    
    context = {'book': book,
               'prev_book': prev_book,
               'next_book': next_book}
    
    return render(request, template, context)