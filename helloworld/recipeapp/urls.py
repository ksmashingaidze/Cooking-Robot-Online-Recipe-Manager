from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('browse', views.browse, name='browse'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]

