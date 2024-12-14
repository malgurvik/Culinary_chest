from django import template
from recipes.models import Categories

register = template.Library()


@register.simple_tag()
def get_recipe_categories():
    return Categories.objects.all()
