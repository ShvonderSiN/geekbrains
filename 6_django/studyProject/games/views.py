from random import choice, randint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

import logging
from .forms import GameForm, GAMES

logger = logging.getLogger(__name__)


def coins(request: HttpRequest, count: int) -> HttpResponse:
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(("Орел", "Решка"))
    context = {"title": "Все выпавшие варианты Орла и Решки", "res": res}
    return render(request, template_name="games/game.html", context=context)


def cube(request, count: int) -> HttpResponse:
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(("Один", "Два", "Три", "Четыре", "Пять", "Шесть"))
    context = {"title": "Все выпавшие варианты Кубика", "res": res}
    return render(request, template_name="games/game.html", context=context)


def random_number(request, count: int) -> HttpResponse:
    res = {}
    for num in range(1, count + 1):
        res[num] = randint(1, 100)
    context = {"title": "Все случайные числа", "res": res}
    return render(request, template_name="games/game.html", context=context)


def game_form(request) -> HttpResponse:
    if request.method == "POST":
        form = GameForm(request.POST)
        title = "Error"
        if form.is_valid():
            game = form.cleaned_data["game"]
            attempts = form.cleaned_data["attempts"]
            logger.info(f"Recieved {game}, {attempts}")

            if game == "C":
                return coins(request, attempts)
            elif game == "B":
                return cube(request, attempts)
            else:
                return random_number(request, attempts)

    else:
        form = GameForm()
        title = "Choose the game"
    context = {"title": title, "form": form}

    return render(request, template_name="games/index.html", context=context)
