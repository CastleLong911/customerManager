from django.shortcuts import render, redirect
from .models import customer
from django.contrib import messages

# Create your views here.

def loadFind(request):
    print('hello')
    if request.user.is_authenticated:
        data = list(customer.objects.values()[:30])
        data = {'result': data}
        return render(request, 'find.html', data)
    else:
        return redirect('login/')

def loadInput(request):
    if request.user.is_authenticated:
        return render(request, 'input.html')

    else:
        return redirect('login/')

def inputCustomer(request):
    if request.method == 'GET':
        return redirect('login/')
    elif request.method == 'POST':
        try:
            c = customer(
                name = request.POST['name'],
                phone_number= request.POST['phoneNumber'],
                sex=request.POST['sex'],
                birth=request.POST['bYear']+request.POST['bMonth'].zfill(2)+request.POST['bDay'].zfill(2),
                address=request.POST['addr1']+' '+request.POST['addr2']+' '+request.POST['addr3'],
                car_number=request.POST['carNumber'],
                etc=request.POST['etc']
            )
            c.save()
            messages.warning(request, '정보 입력 성공')
            return redirect('/')
        except:
            messages.warning(request, '정보 입력 실패')
            return redirect('/input/')

def ajax_search_customer(request):
    if request.method == 'POST':
        return render(request, 'login.html')
    else:
        try:
            pass
        except:
            pass
