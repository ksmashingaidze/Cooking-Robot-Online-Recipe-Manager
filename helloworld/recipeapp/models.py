# Create your models here.

from django.db import models
from django.urls import reverse

# class MyModelName(models.Model):
    # """A typical class defining a model, derived from the Model class."""

    # Fields
    #my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # …

    # Metadata. You can order the data based on meta data
    #class Meta:
        #ordering = ['-my_field_name']

    # Methods
    # def get_absolute_url(self):
        # """Returns the URL to access a particular instance of MyModelName."""
        # return reverse('model-detail-view', args=[str(self.id)])

    # def __str__(self):
        # """String for representing the MyModelName object (in Admin site etc.)."""
        # return self.my_field_name

# Create a new record using the model's constructor.
# record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
# record.save()

class Recipe(models.Model):
    """Model representing the recipe name."""
    recipe_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)
    utensils = models.CharField(max_length=500)
    prep_directions = models.CharField(max_length=1000)
    prep_time_min = models.FloatField(max_length=100)
    cook_time_min = models.FloatField(max_length=100)
    cook_setting = models.CharField(max_length=100)
    calories = models.IntegerField()
    rating = models.IntegerField()
    #paginate_by = 6

    class Meta:
        ordering = ['recipe_name', 'rating']

    #def get_absolute_url(self):
        #"""Returns the URL to access a particular author instance."""
        #return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.recipe_name}, {self.author}'

# Create a new record using the model's constructor.
#record = Recipe(recipe_name="Feta Eggs",
#               author = "Stephen",
#                ingredients = "1 tablespoon butter, 1/4 cup chopped onion, 4 eggs beaten, 1/4 cup chopped tomatoes, 2 tablespoons crumbled feta cheese, salt and pepper",
#                utensils = "knife, fork, spatula",
#                prep_directions = "Melt butter in a skillet over medium heat. Saute onions until translucent. Pour in eggs. Cook, stirring occasionally to scramble. When eggs appear almost done, stir in chopped tomatoes and feta cheese, and season with salt and pepper. Cook until cheese is melted.",
#                prep_time_min = 10,
#                cook_time_min = 5,
#                cook_setting = "Medium",
#                calories = 116,
#                rating = 3,
#)
# Save the object into the database.
#record.save()
RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class RecipeReview(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    review_rating=models.CharField(choices=RATING,max_length=150)

    def get_recipereview(self):
        return self.review_rating