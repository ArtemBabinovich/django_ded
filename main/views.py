from django.shortcuts import render

'''функция для аналитики сайта'''
# from site_visit_analysis.utils import get_visit_user


def index(request):
    # get_visit_user(request)
    return render(request, 'main.html')
