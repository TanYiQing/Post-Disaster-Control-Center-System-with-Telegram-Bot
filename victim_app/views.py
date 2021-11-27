from django.shortcuts import render
from victim_app.models import Address, Profile


def victim(request):
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

        if not Profile.objects.filter(ic=icNum).exists():
            victimProfile = Profile(ic=icNum, name=name, phone=phone, is_kir=is_kir, salary=salary)
            victimProfile.save()
            victimAddress = Address(address1=address1, address2=address2, city=city, mukim=mukim, parlimen=parlimen,
                                    state=state, poskod=poskod)
            victimAddress.save()
            respond = "{} has been successfully add to the list.".format(name)
            return render(request, 'victim_app/victim.html', {"status": respond})
        else:
            respond = "Fail. This ic number is already exist. Please insert again."
            return render(request, 'victim_app/victim.html', {"status": respond})
    return render(request, 'victim_app/victim.html')


def victim_report(request):
    victim_list = Profile.objects.all().order_by("-ic")
    victim_address = Address.objects.all()
    return render(request, 'victim_app/victim_report.html',
                  context={'victim_list': victim_list, 'victim_address': victim_address})


def victim_detail(request, ic):
    victim_profile = Profile.objects.get(pk=ic)
    victim_address = Address.objects.get(pk=id)

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

        victim_profile.ic = icNum
        victim_profile.name = name
        victim_profile.phone = phone
        victim_profile.is_kir = is_kir
        victim_profile.salary = salary
        victim_address.address1 = address1
        victim_address.address2 = address2
        victim_address.city = city
        victim_address.mukim = mukim
        victim_address.parlimen = parlimen
        victim_address.state = state
        victim_address.poskod = poskod

        victim_profile.save()
        victim_address.save()
        victim_list = Profile.objects.all().order_by("-ic")
        victim_address = Address.objects.all()
        return render(request, 'victim_app/victim_report.html', context={'victim_list': victim_list, 'victim_address': victim_address})

    return render(request, 'victim_app/victim_detail.html', context={'victim': victim})
