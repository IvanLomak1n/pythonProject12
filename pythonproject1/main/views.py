from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("ПРИВЕТ ЛЮЮЮБИИИМАААЯЯЯЯ.")

def about(request):
    return HttpResponse("<h4>Страница про нас.<h4>")

def contacts(request):
    return HttpResponse("<h4>Контакты.<h4>")

def blog(request):
    return HttpResponse("<h4>Блог.<h4>")

def новости(request):
    return HttpResponse("<h4>Новости.<h4>")
