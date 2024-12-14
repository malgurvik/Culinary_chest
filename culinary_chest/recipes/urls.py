from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path("", views.catalog, name="index"),
    path("recipe/", views.recipe, name="recipe"),
]