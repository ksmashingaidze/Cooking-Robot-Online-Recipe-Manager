from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from .forms import AddRating
from .models import Recipe
from .models import RecipeReview
from .models import FavoriteRecipe
from django.db.models import Q
from django.core.mail import send_mail as sm
from django.conf import settings
from django.forms.models import model_to_dict
import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    # View the home page
    
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
        recipes = Recipe.objects.filter(recipe_name__icontains=query, rating__range=(
            1, rate), cook_time_min__range=(0, time))
    elif rate and time:
        recipes = Recipe.objects.filter(rating__range=(
            1, rate), cook_time_min__range=(0, time))
    paginator = Paginator(recipes, 3)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    context2 = {
        'newRecepie': results,
    }
    return render(request, 'browse.html', context=context2)


def detail(request, id):
    # View the detail page

    # Get the recipes from the model file, then pass them to the browse recipe HTML template
    selected_recipe = Recipe.objects.get(id=id)
    instructions = selected_recipe.prep_directions.split(".")  # Separate instruction text into steps using full stops.
    step_count = len(instructions)
    desired_size = step_count - 1
    for i in range(0, step_count - desired_size):  # Remove the full stop
        instructions.pop()

    for i in range(0, desired_size):
        instructions[i] = "Step " + str(i+1) + ": " + instructions[i]

    ratingForm = AddRating
    context = {
        'selected_recipe': selected_recipe,
        'form': ratingForm,
        'instructions': instructions

    }

    return render(request, 'detail.html', context=context)


def send_emails(request, pk):

    if request.method == 'POST':
        my_email = request.POST.get('email')
        # my_id = request.POST.get('id')
        selected_receipe = Recipe.objects.get(id=pk)
        full_message = ""
        for v, k in model_to_dict(selected_receipe).items():
            full_message += str(v) + " :" + str(k) + " \n"

        full_message += "\n" + "Link: " + "http://52.55.27.17/recipeapp/detail/"+str(pk) + " \n"

        sm(subject="Recipe from team hello",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[my_email],
            fail_silently=False,)

        return HttpResponse(f"Recipe sent to user")

def saved_rating(request,pid):
    recipe=Recipe.objects.get(pk=pid)
    if RecipeReview.objects.filter(user = request.user.username, recipe = recipe).exists(): # Check if the current user has already rated the current recipe
        # Overwrite the current user's rating for this recipe
        RecipeReview.objects.filter(user = request.user.username, recipe = recipe).delete()
        rate = RecipeReview.objects.create(
            recipe=recipe,
            user=request.user.username,
            review_rating=request.POST['review_rating'],
        )
    else:
        # Create a new recipe review object
        rate=RecipeReview.objects.create(
            recipe=recipe,
            user=request.user.username,
            review_rating=request.POST['review_rating'],
        )
    review_count = 0;
    review_total = 0;
    for item in RecipeReview.objects.filter(recipe = recipe):
        review_count = review_count + 1
        review_total = review_total + item.review_rating
    recipe.rating = review_total/review_count
    recipe.save()
    return JsonResponse({'bool':True})

def added_list(request,pid):
    if request.method == 'POST':
        recipe = Recipe.objects.get(pk=pid)
        username = request.user.username
        name = request.POST.get('name')
        if FavoriteRecipe.objects.filter(name=name, user=request.user.username).exists():  # Check if the current user has already created a list with the same name
            # Add the chosen recipe to the list that already exists
            existinglist = FavoriteRecipe.objects.get(name=name, user=request.user.username)
            existinglist.save()
            existinglist.recipe.add(recipe)

        else:
            existinglist = FavoriteRecipe(name=name, user=request.user.username)
            existinglist.save()
            existinglist.recipe.add(recipe)

    return redirect("/dashboard")