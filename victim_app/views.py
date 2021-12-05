import datetime

from django.shortcuts import render, redirect, get_object_or_404
from victim_app.models import Profile


def add_profile(request):
    if request.method == "POST":
        icNum = request.POST["icNum"]
        name = request.POST["name"]
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

        ic_year = int(icNum[0] + icNum[1])
        ic_month = int(icNum[2] + icNum[3])
        ic_day = int(icNum[4] + icNum[5])

        valid_date = True
        try:
            datetime.datetime(int(ic_year), int(ic_month), int(ic_day))
        except ValueError:
            valid_date = False

        if not Profile.objects.filter(ic=icNum).exists():
            if valid_date:
                victimProfile = Profile(ic=icNum, name=name, phone=phone, is_kir=is_kir, salary=salary,
                                        address1=address1, address2=address2, city=city, mukim=mukim, parlimen=parlimen,
                                        state=state, poskod=poskod)
                victimProfile.save()
                respond = "{} has been successfully add to the list.".format(name)
                return render(request, 'victim_app/add_profile.html', {"status": respond})
            else:
                respond = "Invalid IC Number, please try again"
                return render(request, 'victim_app/add_profile.html', {"status": respond})
        else:
            respond = "Fail. This ic number is already exist. Please insert again."
            return render(request, 'victim_app/add_profile.html', {"status": respond})
    return render(request, 'victim_app/add_profile.html')


def list_user(request):
    victim_list = Profile.objects.all().order_by("-ic")
    return render(request, 'victim_app/list_user.html',
                  context={'victim_list': victim_list})


def edit_profile(request, ic):
    victim_profile = Profile.objects.get(pk=ic)
    if request.method == "POST":
        icNum = request.POST["icNum"]
        name = request.POST["name"]
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

        ic_year = int(icNum[0] + icNum[1])
        ic_month = int(icNum[2] + icNum[3])
        ic_day = int(icNum[4] + icNum[5])

        valid_date = True
        try:
            datetime.datetime(int(ic_year), int(ic_month), int(ic_day))
        except ValueError:
            valid_date = False

        if valid_date:
            victim_profile.ic = icNum
            victim_profile.name = name
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
            victim_list = Profile.objects.all().order_by("-ic")
            respond = "Edit Successful"
            return render(request, 'victim_app/list_user.html', context={'status': respond, 'victim_list': victim_list})
        else:
            respond = "Invalid IC Number"
            return render(request, 'victim_app/edit_profile.html', {"status": respond})

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
