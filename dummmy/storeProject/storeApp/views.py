import re

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['cpassword']
        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username Already Exists...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Invalid EmailID...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=pwd, email=email, first_name=fname,
                                                last_name=lname)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password Not Matching...")
            return redirect('register')
    return render(request, 'register.html')


def form(request):
    if request.method == 'POST':
        return redirect('form')
    else:
        messages.info(request, 'invalid')

    return render(request, "form.html")


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwords = request.POST['password']
        user = auth.authenticate(username=uname, password=passwords)
        if user is not None:
            auth.login(request, user)
            return redirect('order')
        else:
            messages.info(request, "Invalid Login Plz Register")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def order(request):
    if request.method == 'POST':
        messages.info(request, "Your Order Placed Successfully")
        return redirect('order')
    return render(request, 'order.html')
