from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Recipe

def home(request):
    #View the home page

    # Get the recipes from the model file, then pass them to the browse recipe HTML template
    recipes = Recipe.objects.all()
    recipe1 = recipes[0]
    recipe2 = recipes[1]
    recipe3 = recipes[2]
    context = {
        'recipe1': recipe1,
        'recipe2': recipe2,
        'recipe3': recipe3,
    }

    return render(request, 'home.html', context=context)

def browse(request):
    #View the browse recipe page

    #Get the recipes from the model file, then pass them to the browse recipe HTML template
    recipes = Recipe.objects.all()
    context2 = {
        'recipes': recipes,
    }


    return render(request, 'browse.html', context=context2)

