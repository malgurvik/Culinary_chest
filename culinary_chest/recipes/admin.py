from django.contrib import admin

from recipes.models import Categories, Recipes, Comments

# admin.site.register(Categories)
# admin.site.register(Recipes)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Comments)
