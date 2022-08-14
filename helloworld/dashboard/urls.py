from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('addrecipe', views.addrecipe, name='addrecipe'),
    
]

