# core/views.py
from django.shortcuts import render


def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию; 
    # выводить её в шаблон пользовательской страницы 404 мы не станем.
    return render(request, 'core/404.html', status=404)


def page_403(request, exception):
    return render(request, 'core/403.html', status=403)


def csrf_failure(request, reason=''):
    return render(request, 'core/403_csrf.html', status=403)
