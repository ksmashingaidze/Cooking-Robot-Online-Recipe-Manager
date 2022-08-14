from django.contrib import admin

# Register your models here.

#from .models import
from .models import Recipe
from django.contrib import admin
from .models import RecipeReview,Recipe,FavoriteRecipe

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeReview)
admin.site.register(FavoriteRecipe)
