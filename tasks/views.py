from django.shortcuts import render


def index(request):
    return render(request, 'tasks/index.html')


def users(request):
    return render(request, 'tasks/users.html')


def login(request):
    return render(request, 'tasks/login.html')


def create(request):
    return render(request, 'tasks/create.html')
