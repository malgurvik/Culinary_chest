from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Culinary Chest",
    }
    return render(request, 'main/index.html', context)
