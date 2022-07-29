from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse', views.browse, name='browse'),
    path('detail/<int:id>',views.detail, name='detail'),
    path('dashboard', views.dashboard, name='dashboard'),
]

