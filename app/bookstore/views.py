from django.shortcuts import render, redirect

from .forms import *
from .models import *


def books_list(request):
    booklist = Books.objects.all()
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        booklist = booklist.filter(title=search)
    context = {'booklist': booklist}
    return render(request, 'bookstore/books.html', context=context)


def book(request, index):
    book_dis = Books.objects.get(pk=index)
    comments = Comments.objects.filter(book_id=index)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author_comm = request.user
            form.book = book_dis
            form.save()
            return redirect(book, index)
    else:
        form = CommentForm()
    context = {
        'book_dis': book_dis,
        'comments': comments,
        'form': form
    }
    return render(request, 'bookstore/book.html', context=context)


def author(request, index):
    author_dis = Authors.objects.get(pk=index)
    context = {'author_dis': author_dis}
    return render(request, 'bookstore/author.html', context=context)


def author_list(request, index):
    au_list = Authors.objects.filter(id=index)
    book_au = Books.objects.filter(author_id=index)
    context = {
        'au_list': au_list,
        'book_au': book_au
    }
    return render(request, 'bookstore/author_list.html', context=context)


def add_book(request):
    if request.method == 'POST':
        form = BookAdd(request.POST)
        if form.is_valid():
            try:
                Books.objects.create(**form.cleaned_data)
                return redirect('books')
            except:
                form.add_error(None, 'Ошибка добавления книги')
    else:
        form = BookAdd()
    context = {'form': form}
    return render(request, 'bookstore/addbook.html', context=context)

