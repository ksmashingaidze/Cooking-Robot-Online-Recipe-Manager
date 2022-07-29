from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Recipe
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
    recipes = Recipe.objects.all()
    query = request.GET.get("name")
    rate = request.GET.get("rate")
    time = request.GET.get("time")
    if query:
        recipes = Recipe.objects.filter(recipe_name__icontains=query,rating__range=(1,rate),cook_time_min__range=(0,time))
    elif rate and time:
        recipes = Recipe.objects.filter(rating__range=(1, rate),cook_time_min__range=(0, time))
    paginator=Paginator(recipes,3)
    page=request.GET.get("page")
    try:
      results=paginator.page(page)
    except PageNotAnInteger:
      results=paginator.page(1)
    except EmptyPage:
      results=paginator.page(paginator.num_pages)
    context2 = {
        'newRecepie': results,
    }
    return render(request, 'browse.html', context=context2)
def detail(request, id):
    #View the detail page

    # Get the recipes from the model file, then pass them to the browse recipe HTML template
    selected_recipe = Recipe.objects.get(id=id)
    context = {
        'selected_recipe': selected_recipe,
    }

    return render(request, 'detail.html', context=context)

def dashboard(request):
    #View the detail page

    

    return render(request, 'dashboard.html')
