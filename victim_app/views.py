import datetime
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from victim_app.models import Victim


@login_required(login_url='/login')
def add_profile(request):

    if request.method == "POST":
        phone = request.POST["phone"]
        is_kir = str(request.POST["is_kir"])
        salary = request.POST["salary"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        mukim = request.POST["mukim"]
        parlimen = request.POST["parlimen"]
        state = request.POST["state"]
        poskod = request.POST["poskod"]
        
        victim = Victim(phone=phone, is_kir=is_kir, salary=salary,
                                address1=address1, address2=address2, city=city, mukim=mukim, parlimen=parlimen,
                                state=state, poskod=poskod)
        victim.save()
        return redirect('edit_profile')

    return render(request, 'victim_app/add_profile.html')


@login_required(login_url='/login')
def list_user(request):
    victim_list = Victim.objects.all().order_by("-ic")
    return render(request, 'victim_app/list_user.html',
                  context={'victim_list': victim_list})


@login_required(login_url='/login')
def edit_profile(request, id):
    victim = get_object_or_404(Victim,id=id)
    if request.method == "POST":
        phone = request.POST["phone"]
        is_kir = str(request.POST["is_kir"])
        salary = request.POST["salary"]
        address1 = request.POST["address1"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        mukim = request.POST["mukim"]
        parlimen = request.POST["parlimen"]
        state = request.POST["state"]
        poskod = request.POST["poskod"]

        victim.phone = phone
        victim.is_kir = is_kir
        victim.salary = salary
        victim.address1 = address1
        victim.address2 = address2
        victim.city = city
        victim.mukim = mukim
        victim.parlimen = parlimen
        victim.state = state
        victim.poskod = poskod

        victim.save()
        respond = "Edit Successful"
        return render(request, 'victim_app/edit_profile.html', context={'victim': victim})

    return render(request, 'victim_app/edit_profile.html', context={'victim': victim})


def delete_profile(request,id):
    context = {}
    if "ic" in request.GET:
        id = request.GET["ic"]
        icd = get_object_or_404(Victim, id=id)
        context["victim"] = icd

        if "action" in request.GET:
            icd.delete()
            context["status"] = str(icd.name) + " Removed Successfully"
    return render(request, 'victim_app/delete_profile.html', context)
