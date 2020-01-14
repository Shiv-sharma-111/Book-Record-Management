from django.shortcuts import render
from BRMapp.forms import NewBookForm,SearchForm
from BRMapp.models import Book
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.

def viewBooks(request):
    books = Book.objects.all()
    res=render(request,'BRMapp/view_book.html',{'books':books})
    return res

def editBook(request):
     book = Book.objects.get(id=request.GET['bookid'])
     fields= {'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
     form = NewBookForm(initial=fields)
     res = render(request,'BRMapp/edit_book.html', {'form':form, 'book':book})
     return res

def deleteBook(request):
    bookid = request.GET['bookid']
    book = Book.objects.get(id=bookid)
    book.delete()
    return HttpResponseRedirect('view-books')

def searchBook(request):
    form = SearchForm()
    res = render(request,'BRMapp/search_book.html', {'form':form})
    return res

def search(request):
    form = SearchForm(request.POST)
    books = Book.objects.filter(title= form.data['title'])
    res = render(request, 'BRMapp/search_book.html', {'books':books, 'form':form})
    return res

def edit(request):
    if request.method=="POST":
        form = NewBookForm(request.POST)
        book= Book()
        book.id=request.POST['bookid']
        book.title = form.data['title']
        book.price = form.data['price']
        book.author= form.data['author']
        book.publisher = form.data['publisher']
        book.save()

    return HttpResponseRedirect('view-books')

def newBook(request):
    form = NewBookForm()
    res = render(request,'BRMapp/new_book.html',{'form':form})
    return res

def add(request):
    if request.method == "POST":
        form = NewBookForm(request.POST)
        book = Book()
        book.title= form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    s="Record Stored <br> <a href='/BRMapp/view-books'> View All Books</a>"
    return HttpResponse(s)
