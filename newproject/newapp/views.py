from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def printhello(request):
    return render(request,'sample.html')
