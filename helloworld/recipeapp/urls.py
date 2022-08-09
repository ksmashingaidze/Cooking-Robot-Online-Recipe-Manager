from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse', views.browse, name='browse'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('send_emails/<int:pk>',views.send_emails, name='send_emails'),
    path('save-rating/<int:pid>',views.saved_rating,name='saved_rating')
]
