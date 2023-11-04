from django.shortcuts import render
from django.http import HttpRequest

def map(request):
    template = "map.html"
    return render(request, template)

def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

def clubs(request):
    return render(request, "hub.html")

def post(request):
    return render(request, "posting.html")