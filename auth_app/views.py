import datetime

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_process
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect
from auth_app.forms import UserCreationForm
from auth_app.models import CustomUser

from django.http import HttpResponse


def register(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'POST':
        print(req.POST['ic'])

        ic = req.POST['ic']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        password = req.POST['password']
        confirm_password = req.POST['confirm_password']

        ic_year = int(ic[0] + ic[1])
        ic_month = int(ic[2] + ic[3])
        ic_day = int(ic[4] + ic[5])

        valid_date = True
        try:
            datetime.datetime(int(ic_year), int(ic_month), int(ic_day))
        except ValueError:
            valid_date = False

        if not valid_date:
            messages.error(req, 'Please try again with a valid IC Number')
            return redirect('register')
        if not ic.isnumeric():
            messages.error(req, 'IC Number has to be a number')
            return redirect('register')
        if len(ic) < 12:
            messages.error(req, 'IC Number are less than 12 digits')
            return redirect('register')
        if len(ic) > 12:
            messages.error(req, 'IC Number are greater than 12 digits')
            return redirect('register')
        if password != confirm_password:
            messages.error(req, 'Passwords did not match')
            return redirect('register')

        try:
            user = CustomUser.objects.create_user(
                ic=ic, password=password, first_name=first_name, last_name=last_name)
        except Exception as e:
            return HttpResponse(e)
        return redirect('login')

    return render(req, 'auth_app/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        ic = request.POST['ic']
        password = request.POST['password']
        user = authenticate(request, ic=ic, password=password)
        if user is not None:
            login_process(request, user)

            try:
                has_profile = user.profile is not None
                if has_profile:
                    return redirect('/')

            except:
                print('user has no profile')
                return redirect('add_profile')

            ...
        else:
            # Return an 'invalid login' error message.
            messages.error(request, f'failed to login')
            return redirect('login')
    return render(request, 'auth_app/customlogin.html')
