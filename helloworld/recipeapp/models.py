# Create your models here.

from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    """Model representing the recipe name."""
    recipe_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)
    utensils = models.CharField(max_length=500)
    prep_directions = models.CharField(max_length=1000)
    prep_time_min = models.FloatField(max_length=100)
    cook_time_min = models.FloatField(max_length=100)
    cook_setting = models.CharField(max_length=100)
    calories = models.IntegerField()
    rating = models.DecimalField(max_digits=13, decimal_places=1)
    image = models.ImageField(blank=True, upload_to='recipe_images')

    class Meta:
        ordering = ['recipe_name', 'rating']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.recipe_name}, {self.author}'

RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)

class RecipeReview(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    review_rating = models.DecimalField(max_digits=13, decimal_places=1, choices=RATING)
    user = models.CharField(max_length=100)

    def get_recipereview(self):
        return self.review_rating

class FavoriteRecipe(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ManyToManyField(Recipe)
    user = models.CharField(max_length=100)


    class Meta:
        ordering = ['name']


