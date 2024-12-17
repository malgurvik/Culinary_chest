from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path("search/", views.catalog, name="search"),
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("recipe/<slug:recipe_slug>/", views.recipe_detail, name="recipe"),
    path("add/", views.add_recipe, name="add"),
]
