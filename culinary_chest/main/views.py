from django.http import HttpResponse
from django.shortcuts import render
from recipes.models import Recipes


def index(request):
    recipe = Recipes.objects.all().order_by('-id')[:6]
    context = {
        "title": "Кулинарный Сундучок",
        "recipes": recipe,
    }
    return render(request, 'main/index.html', context)
