"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v
from dashboard import views as dv

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),  # <-- added
    path("dashboard", dv.dashboard, name="dashboard"),  # <-- added
    path('', include("django.contrib.auth.urls")),  # <-- added
]

from django.urls import include

urlpatterns += [
    path('recipeapp/', include('recipeapp.urls')),
    path('dashboard/', include('dashboard.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='recipeapp/', permanent=True)),
]

# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)