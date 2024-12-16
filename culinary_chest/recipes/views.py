from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from recipes.models import Categories, Recipes


def catalog(request, category_slug=None):
    query = request.GET.get('q')

    if category_slug == 'all':
        recipes = Recipes.objects.all()
    elif query:
        # recipes = Recipes.objects.filter(name__search=query)
        vector = SearchVector('name', 'description')
        query = SearchQuery(query)
        recipes = Recipes.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')

    else:
        recipes = get_list_or_404(Recipes.objects.filter(category__slug=category_slug))

    context = {"title": "Каталог",
               "recipes": recipes}
    return render(request, "recipes/catalog.html", context)


def recipe_detail(request, recipe_slug):
    recipe = get_object_or_404(Recipes.objects.prefetch_related('comments__user'), slug=recipe_slug)
    comments = recipe.comments.all()
    ingredients = recipe.ingredients.split('\n')
    instructions = recipe.instructions.split('\n')

    context = {"title": "Детали",
               "recipe": recipe,
               "ingredients": ingredients,
               "instructions": instructions,
               "comments": comments}
    return render(request, "recipes/recipe.html", context)
