from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse('Home 2')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')       
