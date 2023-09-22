from django.urls import include, path
from . import views

urlpatterns = [
    path('about/', views.about_me, name='about_me'),
    path('', views.index, name='index'),
]
