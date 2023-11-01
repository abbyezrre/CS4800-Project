from django.shortcuts import render
from django.http import HttpRequest

def map(request):
    template = "Map/map.html"
    return render(request, template)

def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")