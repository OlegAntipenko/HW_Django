import datetime
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render


def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django !")


def usname(request, name):
    return HttpResponse(f"Hello {name}!")


def date(request, value=0):
    now = datetime.datetime.now()
    if value == 0:
        return HttpResponse(now.strftime("%d-%m-%Y"))
    elif value == 'year':
        return HttpResponse(now.strftime("%Y"))
    elif value == 'month':
        return HttpResponse(now.strftime("%m"))
    elif value == 'day':
        return HttpResponse(now.strftime("%d"))
    else:
        return HttpResponseNotFound(f"Не верное значение запроса : {value}")
