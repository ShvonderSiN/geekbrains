from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from random import choice, randint


def eagle(request: HttpRequest, count: int) -> render:
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(("Орел", "Решка"))
    context = {"title": "Все выпавшие варианты Орла и Решки", "res": res}
    return render(request, template_name="coins/index.html", context=context)


def cube(request, count: int) -> render:
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(("Один", "Два", "Три", "Четыре", "Пять", "Шесть"))
    context = {"title": "Все выпавшие варианты Кубика", "res": res}
    return render(request, template_name="coins/index.html", context=context)


def random_number(request, count: int) -> render:
    res = {}
    for num in range(1, count + 1):
        res[num] = randint(1, 100)
    context = {"title": "Все случайные числа", "res": res}
    return render(request, template_name="coins/index.html", context=context)
