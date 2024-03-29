
from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            return render(response, "register/register.html", {"form": form})
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
