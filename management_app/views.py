from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    return render(request, 'management_app/dashboard.html')


def list_victim(request):
    return render(request, 'management_app/list_victim.html')


