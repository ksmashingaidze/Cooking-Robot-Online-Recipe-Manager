from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Recipe
from django.db.models import Q
from django.core.paginator import Paginator

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
    paginator = Paginator(recipes,6) #Show 6 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context2 = {
        'recipes': recipes,
        'page_obj': page_obj,
    }
    


    return render(request, 'browse.html', context=context2)

def search(request):
    recipes=Recipe.objects.all()
    query=request.GET.get("q")
    queryset=Recipe.objects.filter(Q(recipe_name__icontains=query))
    return render(request,'search.html',{'queryset':queryset})
    #total=results.count()
    #paginator=Paginator(results,3)
    #page=request.GET.get("page")
    #try:
     #   results=paginator.page(page)
    #except PageNotAnInteger:
     #   results=paginator.page(1)
    #except EmptyPage:
     #   results=paginator.page(paginator.num_pages)
    #context3={
     #   "topic":topic,
    #   "page":page,
     #   "total":total,
      #  "query":query,
       # "results":results,
    #}

    #return render(request,'search.html',context=context3)
    
    

	
