from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def stocks(request):
    return HttpResponse("This works!")
def mutualfunds(request):
    return HttpResponse("This works too!")