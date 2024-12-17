from django import forms
from recipes.models import Recipes

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('name',
                  'description',
                  'ingredients',
                  'portions',
                  'instructions',
                  'cooking_time_hours',
                  'cooking_time_minutes',
                  'image',
                  'category')