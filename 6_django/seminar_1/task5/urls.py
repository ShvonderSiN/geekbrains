from django.urls import include, path
from . import views

urlpatterns = [
    path("eagle/", views.eagle, name='eagle'),
    path("cube/", views.cube, name='cube'),
    path("num/", views.random_number, name='num'),
]
