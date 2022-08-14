from dataclasses import fields
import imp
from django import forms
from .models import RecipeReview

class AddRating(forms.ModelForm):
    class Meta:
        model=RecipeReview
        fields=('review_rating', 'user',)