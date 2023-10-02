from django.urls import path
from .views import coins, cube, random_number, game_form

urlpatterns = [
    path("coins/<int:count>", coins, name="coins"),
    path("cube/<int:count>", cube, name="cube"),
    path("random/<int:count>", random_number, name="random_number"),
    path("", game_form, name="game_form"),
]
