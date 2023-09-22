from django.shortcuts import render, HttpResponse
from random import choice, randint
import logging

logger = logging.getLogger(__name__)


def eagle(request):
    logger.info('Орел или Решка')
    res = choice(('Орел', 'Решка'))
    return HttpResponse(f'<h1>Выпало {res}</h1>')


def cube(request):
    logger.info('Игральный Куб')
    res = choice(('Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть'))
    return HttpResponse(f'<h1>Выпало {res}</h1>')


def random_number(request):
    logger.info('Случайное числ')
    return HttpResponse(f'<h1>Случайное число: {randint(0, 100)}</h1>')
