from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import NewUser
import django_session_timeout



def logoutuser(request):
    logout(request)
    return redirect('lgn')

@login_required(login_url='lgn')
def home(request):
    print(request.user.username)
    identity=request.user.id
    address=NewUser.objects.get(id=identity).address
    email=NewUser.objects.get(id=identity).email
    if(len(email)==0):
        email="NULL"
    if (len(address) == 0):
        address = "NULL"

    context={'address':address,'email':email}
    return render(request, 'app/detail.html',context)

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('pswd')
        print(username)
        print(password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
            return render(request, 'app/login.html')
    return render(request, 'app/login.html')

def register(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('lgn')
        else:
            messages.info(request, 'the passwords dont match')
            return redirect('rgstr')

    context = {'form': form}

    return render(request, 'app/register.html',context)

@login_required(login_url='lgn')
def edit(request):

    if request.method=="POST":
        identity = request.user.id
        user = NewUser.objects.get(id=identity)
        newemail=request.POST.get('email')
        newaddress=request.POST.get('address')
        if(len(newemail)==0):
            newemail=user.email
        if(len(newaddress)==0):
            newaddress=user.address
        user.email=newemail
        user.address=newaddress
        user.save()
        return redirect('home')

    return render(request, 'app/edit.html')

def deleteuser(request):
    identity = request.user.id
    user = NewUser.objects.get(id=identity)
    user.email=""
    user.address=""
    user.save()
    return redirect('home')

def sessionexpired(request):
    messages.info(request, 'SESSION EXPIRED LOGIN AGAIN')
    return redirect('lgn')