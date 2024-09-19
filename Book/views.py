from django.shortcuts import render
from .models import Book


def book_detail(request):
    book = Book.objects.first()  # Just show the first book for simplicity
    return render(request, 'book_detail.html', {'book': book})

