from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Recipe

def home(request):
    #View the home page
    return render(request, 'home.html')

def browse(request):
    #View the browse recipe page

    #Get the recipes from the model file, then pass them to the browse recipe HTML template
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }


    return render(request, 'browse.html', context=context)

