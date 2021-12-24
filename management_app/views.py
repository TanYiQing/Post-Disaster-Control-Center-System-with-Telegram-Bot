from django.http import HttpResponse
from django.shortcuts import render


def list_victim(request):
    return render(request, 'management_app/list_victim.html')
