from django.shortcuts import render
import datetime


import assistance_app.models
from django.shortcuts import render
from assistance_app.models import *
from django.contrib import messages


def add(request):
    return render(request, 'assistance_app/add.html')
    # if request.method == "POST":
    #     ic_no = request.POST["ic_no"]
    #     name = request.POST["name"]
    #     hp_no = request.POST["hp_no"]
    #
    #     ic_year = int(ic_no[0] + ic_no[1])
    #     ic_month = int(ic_no[2] + ic_no[3])
    #     ic_day = int(ic_no[4] + ic_no[5])
    #
    #     valid_date = True
    #     try:
    #         datetime.datetime(int(ic_year), int(ic_month), int(ic_day))
    #     except ValueError:
    #         valid_date = False
    #
    #     if not Victim.objects.filter(ic_no=ic_no).exists():
    #         if valid_date:
    #             victim = App_Victim.models.Victim(ic_no=ic_no, name=name, hp_no=hp_no)
    #             victim.save()
    #             messages.success(request, "{} registered as victim".format(name))
    #         else:
    #             messages.error(request, "Invalid IC number, please try again")
    #     else:
    #         messages.error(request, "IC Number registered before")



