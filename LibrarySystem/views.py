from django.shortcuts import render
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from .models import *

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# book
@csrf_exempt
def createBook(request):
    try:

        id = request.POST.get('id')
        name = request.POST.get('name')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publisher = request.POST.get('publisher')
        publish_date = request.POST.get('publish_date')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        remaining = request.POST.get('remaining')

        current_book = Book(name=name, author=author) # ...

        current_book.save()
        msg = 'success'

    except Exception as e:
        msg = 'error'
        print(e)

    resp = {'msg': msg}
    return JsonResponse(resp)


@csrf_exempt
def retrieveBook(request):
    try:
        id = request.GET.get('id')

        current_book = Book.objects.get(id=id)

        # original type Book cannot be serializable
        # usually, add all items to a dict
        resp_dict = {}
        resp_dict['name'] = current_book.name
        resp_dict['author'] = current_book.author
        resp_dict['category'] = current_book.category
        resp_dict['publisher'] = current_book.publisher
        resp_dict['publish_date'] = current_book.publish_date
        resp_dict['publish_date'] = current_book.publish_date
        resp_dict['description'] = current_book.description
        resp_dict['amount'] = current_book.amount
        resp_dict['remaining'] = current_book.remaining

        msg = resp_dict

    except Exception as e:
        msg = 'error'
        print(e)

    resp = {'msg': msg}
    return JsonResponse(resp)


@csrf_exempt
def updateBook(request):
    try:
        id = request.POST.get('id')
        name = request.POST.get('name')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publisher = request.POST.get('publisher')
        publish_date = request.POST.get('publish_date')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        remaining = request.POST.get('remaining') 

        current_book = Book.objects.get(id=id)
        current_book.name = name
        current_book.author = author
        # ...
        current_book.save()

        msg = 'success'

    except Exception as e:
        msg = 'error'
        print(e)

    resp = {'msg': msg}
    return JsonResponse(resp)


@csrf_exempt
def deleteBook(request):
    try:
        id = request.POST.get('id')

        current_book = Book.objects.get(id=id)
        current_book.delete()

        msg = 'success'

    except Exception as e:
        msg = 'error'
        print(e)

    resp = {'msg': msg}
    return JsonResponse(resp)