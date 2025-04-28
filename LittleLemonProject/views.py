from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'snippets/home.html')

def about(request):
    return render(request,'snippets/about.html')