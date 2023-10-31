from django.shortcuts import render

def map(request):
    template = "Map/map.html"
    return render(request, template)