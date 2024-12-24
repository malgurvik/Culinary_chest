from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.urls import reverse
from django.http import HttpResponseRedirect
from recipes.models import Categories, Recipes
from recipes.forms import RecipeForm, RecipeCommentsForm


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

    if request.method == "POST":
        form = RecipeCommentsForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            form.save()
            return HttpResponseRedirect(reverse('recipes:recipe', args=(recipe_slug,)))
    else:
        form = RecipeCommentsForm()

    comments = recipe.comments.all()
    ingredients = recipe.ingredients.split('\n')
    instructions = recipe.instructions.split('\n')

    context = {"title": "Детали",
               "recipe": recipe,
               "ingredients": ingredients,
               "instructions": instructions,
               "comments": comments,
               "form": form}
    return render(request, "recipes/recipe.html", context)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))

    else:
        form = RecipeForm()

    context = {
        "title": "Добавление рецепта",
        "form": form
    }
    return render(request, "recipes/add_recipe.html", context)
