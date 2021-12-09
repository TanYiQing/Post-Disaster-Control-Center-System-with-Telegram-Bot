import datetime
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from victim_app.models import Profile


@login_required(login_url='/login')
def add_profile(request):
    user = request.user
    try:
        has_profile = user.profile is not None
        if has_profile:
            return redirect('edit_profile')
    except:
        print('user has no profile')
        pass

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
        
        victimProfile = Profile(phone=phone, is_kir=is_kir, salary=salary,
                                address1=address1, address2=address2, city=city, mukim=mukim, parlimen=parlimen,
                                state=state, poskod=poskod)
        victimProfile.user = user
        victimProfile.save()
        return redirect('edit_profile')

    return render(request, 'victim_app/add_profile.html')


@login_required(login_url='/login')
def list_user(request):
    victim_list = Profile.objects.all().order_by("-ic")
    return render(request, 'victim_app/list_user.html',
                  context={'victim_list': victim_list})


@login_required(login_url='/login')
def edit_profile(request):
    user = request.user
    try:
        has_profile = user.profile is not None
        if not has_profile:
            return redirect('add_profile')
    except:
        print('user has no profile')
        pass
    victim_profile = user.profile
    if request.method == "POST" and (victim_profile != None):
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

        victim_profile.phone = phone
        victim_profile.is_kir = is_kir
        victim_profile.salary = salary
        victim_profile.address1 = address1
        victim_profile.address2 = address2
        victim_profile.city = city
        victim_profile.mukim = mukim
        victim_profile.parlimen = parlimen
        victim_profile.state = state
        victim_profile.poskod = poskod

        victim_profile.save()
        respond = "Edit Successful"
        return render(request, 'victim_app/edit_profile.html', context={'victim_profile': victim_profile})

    return render(request, 'victim_app/edit_profile.html', context={'victim_profile': victim_profile})


def delete_profile(request):
    context = {}
    if "ic" in request.GET:
        ic = request.GET["ic"]
        icd = get_object_or_404(Profile, ic=ic)
        context["victim"] = icd

        if "action" in request.GET:
            icd.delete()
            context["status"] = str(icd.name) + " Removed Successfully"
    return render(request, 'victim_app/delete_profile.html', context)
