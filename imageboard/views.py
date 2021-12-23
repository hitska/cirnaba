from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")

def board(request, board_name):
    return HttpResponse("Board")

def thread(request, board_name, thread_id):
    return HttpResponse("Thread")
