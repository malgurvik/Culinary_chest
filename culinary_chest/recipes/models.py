from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Recipes(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(
        max_length=100, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    ingredients = models.TextField(null=False, blank=False, verbose_name="Ингридиенты")
    portions = models.IntegerField(blank=True, null=True, verbose_name="Порции")
    instructions = models.TextField(null=False, blank=False, verbose_name="Инструкция")
    cooking_time_hours = models.IntegerField(
        null=True, blank=True, verbose_name="Время приготовления часов"
    )
    cooking_time_minutes = models.IntegerField(
        null=True, blank=True, verbose_name="Время приготовления минут"
    )
    image = models.ImageField(
        upload_to="recipes_images", null=True, blank=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")

    class Meta:
        db_table = "recipes"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = base_slug
            slug = base_slug
            num = 1
            while Recipes.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
            print(slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comments(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'{self.user.username} - {self.recipe.name}'
