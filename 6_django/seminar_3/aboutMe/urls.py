from django.urls import path
from .views import index, about_me

urlpatterns = [
    path('', index, name='index'),
    path('about/', about_me, name='about_me'),
]
