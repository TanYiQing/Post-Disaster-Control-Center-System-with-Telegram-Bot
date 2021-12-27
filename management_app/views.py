from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    return render(request, 'management_app/dashboard.html')


def list_victim(request):
    return render(request, 'management_app/list_victim.html')


def add_victim(request):
    return render(request, 'management_app/add_victim.html')


def edit_victim(request):
    return render(request, 'management_app/edit_victim.html')

