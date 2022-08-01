from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from recipeapp.models import Recipe


class UpdateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

