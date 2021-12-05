from django.shortcuts import render, redirect

import assistance_app.models
from .forms import AssistanceForm
from .models import Assistance, AssistanceType
from django.contrib import messages


def request_assistance(request):
    if request.method == 'POST':
        assistance_form = AssistanceForm(request.POST)
        if assistance_form.is_valid():
            data = assistance_form.cleaned_data
            victim_number = data['victim_number']
            assistance_type = AssistanceType.objects.filter(name=data['assistance_type'])[0]
            remark = data['remark']
            assistance = Assistance(victim_number=victim_number, remark=remark)
            assistance.assistance_type = assistance_type
            assistance.user = request.user
            assistance.save()
            messages.success(request, "request has been sent successfully")

        return redirect('/assistance/create')
    if request.method == 'GET':
        assistance_form = AssistanceForm()
        return render(request, 'assistance_app/request.html', {'assistance_form': assistance_form})


def list_assistance_type(request):
    assistance = Assistance.objects.all()
    return render(request, 'assistance_app/list.html', {'assistance': assistance})


def edit_assistance_type(request, id):
    assistance = AssistanceType.objects.get(pk=id)
    return render(request, 'assistance_app/edit_user.html', {'assistance': assistance})


def add(request):
    if request.method == 'POST':
        name = request.POST["name"]
        ic_no = request.POST["ic_no"]
        victim_num = request.POST["victim_num"]
        assistance_type = int(request.POST["assistance_type"])
        print(assistance_type)
        # assistance_type = AssistanceType.objects.filter(name=AssistanceType.name)
        remark = request.POST["remark"]
        assistance = Assistance(name=name, ic=ic_no, victim_number=victim_num, remark=remark, assistance_type_id=assistance_type)
        Assistance.assistance_type = assistance_type
        assistance.user = request.user
        assistance.save()
    assistance_type = AssistanceType.objects.all()
    return render(request, 'assistance_app/add.html', {'assistance_type': assistance_type})

