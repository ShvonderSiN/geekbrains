from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

text = """Домашнее задание
� Создайте пару представлений в вашем первом приложении:
главная и о себе.
� Внутри каждого представления должна быть переменная
html - многострочный текст с HTML вёрсткой и данными о
вашем первом Django сайте и о вас.
� *Сохраняйте в логи данные о посещении страниц"""


def about_me(request):
    logger.info('сработала главная страница')
    context = {'name': 'Sergei', 'surname': 'Shekin', 'title': 'Обо мне'}
    return render(request, template_name='about_me/about_me.html', context=context)


def index(request):
    logger.info('сработала страница обо мне')
    context = {
        'title': 'Главная страница',
        'text': text
    }

    return render(request, template_name='about_me/index.html', context=context)
