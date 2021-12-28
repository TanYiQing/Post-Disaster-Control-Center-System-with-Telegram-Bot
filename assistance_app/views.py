from django.shortcuts import render, redirect

import assistance_app.models
from .forms import AssistanceForm
from .models import Assistance, AssistanceType
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def list_assistance_type(request):
    assistances = request.user.assistance_list.all()
    return render(request, 'assistance_app/list.html', {'assistances': assistances})


@login_required(login_url='/login')
def edit_assistance_type(request, id):
    try:
        my_assistance = request.user.assistance_list.get(id=id)
    except:
        return redirect('list_assistance_type')

    if request.method == 'POST':
        victim_num = request.POST["victim_num"]
        assistance_type_id = int(request.POST["assistance_type"])
        remark = request.POST["remark"]
        assistance_type = AssistanceType.objects.get(id=assistance_type_id)
        my_assistance.assistance_type = assistance_type
        my_assistance.remark = remark
        my_assistance.victim_number = victim_num
        my_assistance.save()
        return redirect('list_assistance_type')
    assistance_types = AssistanceType.objects.all()
    return render(request, 'assistance_app/edit_assistance.html',
                  {'my_assistance': my_assistance, 'assistance_types': assistance_types})


@login_required(login_url='/login')
def request_assistance(request):
    try:
        request.user.profile
    except:
        print('user has no profile add first pls')
        return redirect('add_profile')

    if request.method == 'POST':
        victim_num = request.POST["victim_num"]
        assistance_type_id = int(request.POST["assistance_type"])
        remark = request.POST["remark"]
        assistance_type = AssistanceType.objects.get(id=assistance_type_id)
        print(assistance_type)
        assistance = Assistance(victim_number=victim_num, remark=remark)
        assistance.assistance_type = assistance_type
        assistance.user = request.user
        assistance.save()
    assistance_type = AssistanceType.objects.all()
    return render(request, 'assistance_app/request_assistance.html', {'assistance_type': assistance_type})
