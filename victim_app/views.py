from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from victim_app.models import Victim
from assistance_app.models import Assistance, AssistanceType
import re   
from django.contrib import messages
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
        request.session['apply_victim'] = [ic,phone]
        return redirect('victim_request_assistance')

    return render(request, 'victim_app/add_profile.html')


# def list_user(request):
#     # victim_list = Victim.objects.all().order_by("-ic")
#     return render(request, 'victim_app/list_user.html',
#                   # context={'victim_list': victim_list}
#                   )


# def edit_profile(request):
#     # victim = get_object_or_404(Victim,id=id)
#     if request.method == "POST":
#         name = request.POST['name']
#         ic = request.POST['icNum']
#         phone = request.POST["phone"]
#         is_kir = str(request.POST["is_kir"])
#         salary = request.POST["salary"]
#         address1 = request.POST["address1"]
#         address2 = request.POST["address2"]
#         city = request.POST["city"]
#         mukim = request.POST["mukim"]
#         parlimen = request.POST["parlimen"]
#         state = request.POST["state"]
#         poskod = request.POST["poskod"]

#         # victim.name = name
#         # victim.ic = ic
#         # victim.phone = phone
#         # victim.is_kir = is_kir
#         # victim.salary = salary
#         # victim.address1 = address1
#         # victim.address2 = address2
#         # victim.city = city
#         # victim.mukim = mukim
#         # victim.parlimen = parlimen
#         # victim.state = state
#         # victim.poskod = poskod
#         #
#         # victim.save()
#         respond = "Edit Successful"
#         return redirect('list_victim')
    
#     return render(request, 'victim_app/edit_profile.html')


def victim_dashboard(request):
    if request.method == 'POST':
        search_victim = request.POST['search']
        pattern = re.compile("^[0-9]{12}@[0-9]*$")
        data = pattern.match(search_victim)
        if not data:
            print('regex doesnt match')
            # return error
            messages.error(request,"please follow the required format")
            return redirect('victim_dashboard')
        data = data.string.split('@')
        try:
            victimFound = Victim.objects.get(ic=data[0], phone=data[1])
        except:
            victimFound = None
        finally:
            if victimFound:
                request.session['apply_victim'] = data
            elif (not victimFound and 'apply_victim' in request.session):
                del request.session['apply_victim']
            
        if not victimFound:
            messages.error(request,"victim not found")
            return redirect('victim_dashboard')
        if len(victimFound.assistance_list.all()) > 0:
            return redirect('victim_view_assistance')
        return redirect('victim_request_assistance')
                    
    return render(request, 'victim_app/victim_dashboard.html',)


def request_assistance(request):
    if not ("apply_victim" in request.session):
        return redirect('victim_dashboard')
    data = request.session['apply_victim']
    
    try:
        victimFound = Victim.objects.get(ic=data[0], phone=data[1])
    except:
        victimFound = None
        return redirect('victim_dashboard')
    if request.method == 'POST':
        requested_assistance_type = AssistanceType.objects.get(id=request.POST['assistance_type'])
        assistance = Assistance(victim_number= request.POST['victim_num'], remark= request.POST['remark'])
        assistance.assistance_type = requested_assistance_type
        assistance.victim = victimFound
        assistance.save()
        
    assistance_type = AssistanceType.objects.all()
    return render(request, 'victim_app/victim_request_assistance.html', {'victim': victimFound, 'assistance_type': assistance_type})


def edit_assistance(request, id):
    if not ("apply_victim" in request.session):
        return redirect('victim_dashboard')
    data = request.session['apply_victim']
    
    try:
        victimFound = Victim.objects.get(ic=data[0], phone=data[1])
    except:
        victimFound = None
        return redirect('victim_dashboard')
    victim_assistance = victimFound.assistance_list.get(id=id)
    assistance_type_list = AssistanceType.objects.all()
    if request.method == 'POST':
        # update assistance
        assistance_type = AssistanceType.objects.get(
            id=int(request.POST['assistance_type']))
        victim_assistance.assistance_type = assistance_type
        victim_assistance.victim_number = request.POST['victimnumber']
        victim_assistance.remark = request.POST['remark']
        victim_assistance.save()
        return redirect('victim_view_assistance')
        
    return render(request, 'victim_app/victim_edit_assistance.html', {'victim_assistance': victim_assistance, 'assistance_type_list': assistance_type_list})


def view_assistance(request):
    if not ("apply_victim" in request.session):
        return redirect('victim_dashboard')
    data = request.session['apply_victim']
    
    try:
        victimFound = Victim.objects.get(ic=data[0], phone=data[1])
    except:
        victimFound = None
        return redirect('victim_dashboard')
    victim_assistance_list = victimFound.assistance_list.all()
    return render(request, 'victim_app/list_victim_assistance.html',{'victim':victimFound,'victim_assistance_list': victim_assistance_list})