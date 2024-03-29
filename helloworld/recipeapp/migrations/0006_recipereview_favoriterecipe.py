# Generated by Django 4.0.6 on 2022-08-12 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0005_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('user', models.CharField(max_length=100)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('recipe', models.ManyToManyField(to='recipeapp.recipe')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
