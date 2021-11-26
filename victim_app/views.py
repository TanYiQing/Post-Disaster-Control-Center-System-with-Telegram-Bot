from django.shortcuts import render
from django.http import HttpResponse


def victim(request):
    return render(request, 'victim_app/victim.html')




