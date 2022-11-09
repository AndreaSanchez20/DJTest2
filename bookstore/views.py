import requests

from ast import For
from django.shortcuts import render
from http.client import HTTPResponse
from django.http import HttpResponse

import json

booksList=[
    {
    'id': '1',
    'title': 'Book1',
    'description': 'Duro de matar'
    },
    {
    'id': '2',
    'title': 'Book2',
    'description': 'Jue-'
    },
    ]



def book(request, pk):
    bookObj = None
    for i in booksList:
        if i['id'] == pk:
            bookObj =i
    return render(request, 'bookstore/book.html',{'book': bookObj})

#api views

def books(request):
    response = requests.get("http://127.0.0.1:8000/api/books")
    bookListAPI = json.loads(response.text)
    context ={'books':bookListAPI}
    return render(request, "bookstore/books.html", context)

