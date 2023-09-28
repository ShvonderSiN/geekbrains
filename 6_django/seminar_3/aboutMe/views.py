from django.http import HttpRequest
from django.shortcuts import render
from faker import Faker

faker = Faker()


def index(request: HttpRequest) -> render:
    context = {
        'title': 'Главная страница',
    }
    return render(request, template_name='aboutMe/index.html', context=context)


def about_me(request: HttpRequest) -> render:
    context = {
        'name': 'Sergei',
        'surname': 'Shekin',
    }
    return render(request, template_name='aboutMe/about_me.html', context=context)
