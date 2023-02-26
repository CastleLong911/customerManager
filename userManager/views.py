from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def loginPage(request):
    return render(request, 'login.html')

def loginUser(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['mem_userid']
        password = request.POST['mem_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, '아이디 혹은 비밀번호가 틀렸습니다.')
            return redirect('/')


def logoutUser(request):
    logout(request)
    return render(request, 'login.html')