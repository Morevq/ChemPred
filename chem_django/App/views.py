from django.shortcuts import render
from django.http import JsonResponse
from time import sleep

'''
если простыми словами, то text - это то,
что мы получили на вход с фронта,
эту информацию мы можем как-то тут обработать
и вернуть обратно на бэк
'''
def ajax_handler(request):
    text = request.GET.get('search_text', '') #получение данных с фронта
    context = {
        'status': 'ok',
        'data': f'Hello! Вы искали "{text}"'
    } #то, что мы возвращаем на фронт
    return JsonResponse(context) #отправка данных на фронт


def index(request):
    '''то, что мы возвращаем на фронт на глувную страницу,
        тут это название страницы и заголовок,
        но это можно поменять'''
    context = {
        'pagename': 'Пример работы'
    }
    return render(request, 'index.html', context) #отправка данных на фронт
