import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    temlate_name = 'app/time.html'
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    context = {
        'msg': current_time
    }

    return render(request, temlate_name, context)


def workdir_view(request):
    x = os.listdir()
    files = {index + 1: file for index, file in enumerate(x)}
    context = {'files': files}
    template_name = 'app/workdir.html'

    return render(request, template_name, context)

