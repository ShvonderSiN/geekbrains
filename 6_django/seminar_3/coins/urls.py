from django.urls import path
from .views import eagle, cube, random_number

urlpatterns = [
    path('eagle/<int:count>', eagle, name='eagle'),
    path('cube/<int:count>', cube, name='cube'),
    path('random/<int:count>', random_number, name='random_number'),
]
