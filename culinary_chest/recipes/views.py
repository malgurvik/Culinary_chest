from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Каталог",
    }
    return render(request, 'recipes/catalog.html', context)


def recipe(request):
    return render(request, 'recipes/recipe.html')
