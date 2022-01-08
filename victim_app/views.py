from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from victim_app.models import Victim


def add_profile(request):

    if request.method == "POST":
        name = request.POST['name']
        ic = request.POST['icNum']
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
        
        victim = Victim(ic=ic,name=name,phone=phone, is_kir=is_kir, salary=salary,
                                address1=address1, address2=address2, city=city, mukim=mukim, parlimen=parlimen,
                                state=state, poskod=poskod)
        victim.save()
        return redirect('list_user')

    return render(request, 'victim_app/add_profile.html')


def list_user(request):
    # victim_list = Victim.objects.all().order_by("-ic")
    return render(request, 'victim_app/list_user.html',
                  # context={'victim_list': victim_list}
                  )


def edit_profile(request):
    # victim = get_object_or_404(Victim,id=id)
    if request.method == "POST":
        name = request.POST['name']
        ic = request.POST['icNum']
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

        # victim.name = name
        # victim.ic = ic
        # victim.phone = phone
        # victim.is_kir = is_kir
        # victim.salary = salary
        # victim.address1 = address1
        # victim.address2 = address2
        # victim.city = city
        # victim.mukim = mukim
        # victim.parlimen = parlimen
        # victim.state = state
        # victim.poskod = poskod
        #
        # victim.save()
        respond = "Edit Successful"
        return redirect('list_victim')
    
    return render(request, 'victim_app/edit_profile.html')


def victim_dashboard(request):
    return render(request, 'victim_app/victim_dashboard.html')


def request_assistance(request):
    return render(request, 'victim_app/victim_request_assistance.html')


def edit_assistance(request):
    return render(request, 'victim_app/victim_edit_assistance.html')


def view_assistance(request):
    return render(request, 'victim_app/list_victim_assistance.html')