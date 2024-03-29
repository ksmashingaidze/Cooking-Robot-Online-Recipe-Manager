
from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import UpdateForm
from .forms import RecipeForm
from recipeapp.models import Recipe
from recipeapp.models import FavoriteRecipe
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        if FavoriteRecipe.objects.filter(user=request.user.username).exists():  # Check if the current user has any custom lists
            # Pass the custom lists
            favoritelist = FavoriteRecipe.objects.filter(user=request.user.username)
            favoritelistcount = FavoriteRecipe.objects.filter(user=request.user.username).count()
            # favoritelist.save()
            context = {
                'favoritelist': favoritelist,
                'favoritelistcount': favoritelistcount

            }

        else:
            #Pass nothing, if the user has no custom lists
            favoritelist = FavoriteRecipe.objects.filter(user=request.user.username)
            favoritelistcount = FavoriteRecipe.objects.filter(user=request.user.username).count()
            #favoritelist.save()
            context = {
                'favoritelist': favoritelist,
                'favoritelistcount': favoritelistcount
            }

        return render(request, "dashboard.html", context=context)
    else:
        return redirect("/")
    return render(request, "home.html")

# def userprofile(request):
    # if request.user.is_authenticated:
        # return render(request, "userprofile.html")
    # else:
        # return redirect("/")
    # return render(request, "home.html")

def userprofile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UpdateForm(request.POST, instance=request.user, initial={'username': request.user.username, 'email': request.user.email, 'password1': request.user.password, 'password2': request.user.password})
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect("/login")
                # return render(request,"register/registration",{"message":"The profile information just changed please login again!"})
                # return render(request, "userprofile.html", {"form": form,"message":"The new information was saved"})
            else:
                return render(request, "userprofile.html", {"form": form})
            # return redirect("/")
        else:
            form = UpdateForm(initial={'username': request.user.username, 'email': request.user.email, 'password1': request.user.password, 'password2': request.user.password})
            return render(request, "userprofile.html", {"form": form})
    else:
        return redirect("/login")


def addrecipe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, "addrecipe.html", {"form": form})
            else:
                return render(request, "addrecipe.html", {"form": form})
            # return redirect("/")
        else:
            form = RecipeForm()
            return render(request, "addrecipe.html", {"form": form})
    else:
        return redirect("/")


