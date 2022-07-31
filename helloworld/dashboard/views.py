
from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import UpdateForm

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
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
            form = UpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return render(request, "userprofile.html", {"form": form})
            else:
                return render(request, "userprofile.html", {"form": form})
            # return redirect("/")
        else:
            form = UpdateForm()
            return render(request, "userprofile.html", {"form": form})
    else:
        return redirect("/")
        return render(request, "home.html", {"form": form})


def addrecipe(request):
    if request.user.is_authenticated:
        return render(request, "addrecipe.html")
    else:
        return redirect("/")
    return render(request, "home.html")