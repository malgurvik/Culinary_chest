from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Categories, Recipes
from django.db.models import Q


def catalog(request, category_slug=None):
    query = request.GET.get('q')

    if category_slug == 'all':
        recipes = Recipes.objects.all()
    elif query:
        if query.isdigit():
            recipes = Recipes.objects.filter(id=int(query))

        keywords = [word for word in query.split() if len(word) > 2]
        q_objects = Q()

        for token in keywords:
            q_objects |= Q(name__icontains=token)
            q_objects |= Q(description__icontains=token)
        recipes = Recipes.objects.filter(q_objects)
        print(q_objects)

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
