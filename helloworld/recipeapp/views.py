from django.shortcuts import render
from .models import Recipe
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def home(request):
    total_recipes = Recipe.objects.all().count()
    context = {
        "title":"Homepage",
        "total_recipes":total_recipes,
    }  
        
    return render(request, "templates/home.html", context)
	
def browse(request):
	recipes = Recipe.objects.all()
	return render(request,'templates/browse.html',{'recipes': recipes})