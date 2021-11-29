from django.shortcuts import render, redirect
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

    assistance_type = AssistanceType.objects.all()

    return render(request, 'assistance_app/list.html', {'assistanceType': assistance_type})


def edit_assistance_type(request, id):

    assistance = AssistanceType.objects.get(pk=id)

    # if request.method == "POST":
    #     name = request.POST["name"]
    #     ic = request.POST["ic"]
    #     phone = request.POST["phone"]
    #
    #     resident.icNo = ic
    #     resident.name = name
    #     resident.phone = phone
    #     resident.save()
    #
    #     status = "Changes Saved Successfully"
    #     return render(request, 'App_Resident/editdata.html', {'resident': resident, 'status': status})

    return render(request, 'assistance_app/edit_user.html', {'assistance': assistance})
      
      
def add(request):
    if request.method == 'POST':
        name = request.POST["name"]
        ic_no = request.POST["ic_no"]
        victim_num = request.POST["victim_num"]
        assistance_type = request.POST["assistance_type"]
        assistance_date = request.POST["assistance_date"]
        created_at = request.POST["created_at"]
        updated_at = request.POST["updated_at"]
        remark = request.POST["remark"]
    return render(request, 'assistance_app/add.html')

