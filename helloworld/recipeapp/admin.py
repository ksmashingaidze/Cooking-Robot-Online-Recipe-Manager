from django.contrib import admin
from .models import RecipeReview,Recipe
# Register your models here.

#from .models import Author, Genre, Book, BookInstance
from .models import Recipe

admin.site.register(Recipe)
admin.site.register(RecipeReview)

