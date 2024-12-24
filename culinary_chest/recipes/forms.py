from django import forms
# from django.utils.text import slugify
from recipes.models import Recipes, Comments


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('name',
                  'slug',
                  'description',
                  'ingredients',
                  'portions',
                  'instructions',
                  'cooking_time_hours',
                  'cooking_time_minutes',
                  'image',
                  'category')

    # def clean_slug(self):
    #     slug = self.cleaned_data.get('slug')
    #     name = self.cleaned_data.get('name')
    #     if not slug:
    #         slug = slugify(name)
    #     return slug


class RecipeCommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)