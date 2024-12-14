from django.shortcuts import render
from recipes.models import Categories, Recipes


def catalog(request):
    recipes = Recipes.objects.all()
    context = {"title": "Каталог",
               "recipes": recipes}
    return render(request, "recipes/catalog.html", context)


def recipe(request):
    return render(request, "recipes/recipe.html")
