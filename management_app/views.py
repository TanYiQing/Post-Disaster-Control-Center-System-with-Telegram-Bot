from django.contrib.auth.decorators import user_passes_test
from victim_app.models import Victim
from assistance_app.models import Assistance, AssistanceType
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def dashboard(request):
    return render(request, 'management_app/dashboard.html')


@login_required
def list_victim(request):
    victims = Victim.objects.all()
    return render(request, 'management_app/list_victim.html', {'victims': victims})


@login_required
def view_victim_assistance(request, id):
    victim = get_object_or_404(Victim, id=id)
    victim_assistance_list = victim.assistance_list.all()
    # update is_approved
    if request.method == 'POST':
        assistance_id = request.POST['assistance_id']
        updated_assistance = victim_assistance_list.get(id=assistance_id)
        updated_assistance.is_approved = not updated_assistance.is_approved
        updated_assistance.save()

    return render(request, 'management_app/view_victim_assistance.html', {'victim': victim, 'victim_assistance_list': victim_assistance_list})

@login_required
def delete_victim_assistance(request, id):
    victim = get_object_or_404(Victim, id=id)
    if request.method == 'POST':
        assistance_id = request.POST['assistance_id']
        victim_assistance = victim.assistance_list.get(id=assistance_id)
        victim_assistance.delete()
    return redirect('view_victim_assistance', id=id)


@login_required
def edit_victim_assistance(request, victim_id, assistance_id):
    victim = get_object_or_404(Victim, id=victim_id)
    victim_assistance = victim.assistance_list.get(id=assistance_id)
    assistance_types = AssistanceType.objects.all()
    if request.method == 'POST':
        print(request.POST)
        # update victim
        victim.phone = request.POST['phone']
        victim.salary = request.POST['salary']
        victim.is_kir = request.POST['household'] == 'Yes'
        victim.address1 = request.POST['address1']
        victim.address2 = request.POST['address2']
        victim.poskod = request.POST['postcode']
        victim.city = request.POST['city']
        victim.state = request.POST['state']
        victim.parlimen = request.POST['parlimen']
        victim.mukim = request.POST['mukim']
        victim.save()

        # update assistance
        assistance_type = AssistanceType.objects.get(
            id=int(request.POST['assistance_type']))
        victim_assistance.assistance_type = assistance_type
        victim_assistance.victim_number = request.POST['victimnumber']
        victim_assistance.remark = request.POST['remark']
        victim_assistance.save()

    return render(request, 'management_app/edit_victim_assistance.html', {'victim': victim, 'victim_assistance': victim_assistance, 'assistance_types': assistance_types})


# @user_passes_test(lambda user: user.is_staff)
# def add_victim(request):
#     return render(request, 'management_app/add_victim.html')


# # @user_passes_test(lambda user: user.is_staff)
# def edit_victim(request):
#     return render(request, 'management_app/edit_victim.html')
