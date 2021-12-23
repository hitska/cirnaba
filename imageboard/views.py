from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")

def board(request):
    return HttpResponse("Board")

def thread(request):
    return HttpResponse("Thread")
