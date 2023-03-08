from django.shortcuts import render, redirect
from .models import customer
from django.contrib import messages
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.

def loadFind(request):
    print('hello')
    if request.user.is_authenticated:
        data = list(customer.objects.values()[:30])

        data = {'result': data, 'type': '', 'text': '', 'page': customer.objects.count()//30+1}
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
    print('search')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            if request.POST['type'] == '이름':
                page = int(request.POST['page'])
                result = serialize('json', customer.objects.filter(name__icontains=request.POST['text'])[(page-1)*30:page*30])
                data = {'result': result, 'page': customer.objects.filter(name__icontains=request.POST['text']).count() // 30 + 1}
                return JsonResponse(data)
            elif request.POST['type'] == '전화번호':
                page = int(request.POST['page'])
                result = serialize('json', customer.objects.filter(phone_number__icontains=request.POST['text'])[(page - 1) * 30:page * 30])
                data = {'result': result, 'page': customer.objects.filter(phone_number__icontains=request.POST['text']).count() // 30 + 1}
                return JsonResponse(data)
            elif request.POST['type'] == '주소':
                page = int(request.POST['page'])
                result = serialize('json', customer.objects.filter(address__icontains=request.POST['text'])[(page - 1) * 30:page * 30])
                data = {'result': result, 'page': customer.objects.filter(address__icontains=request.POST['text']).count() // 30 + 1}
                return JsonResponse(data)
            elif request.POST['type'] == '생년월일':
                page = int(request.POST['page'])
                result = serialize('json', customer.objects.filter(birth__icontains=request.POST['text'])[(page - 1) * 30:page * 30])
                data = {'result': result, 'page': customer.objects.filter(birth__icontains=request.POST['text']).count() // 30 + 1}
                return JsonResponse(data)
            elif request.POST['type'] == '차량번호':
                page = int(request.POST['page'])
                result = serialize('json', customer.objects.filter(car_number__icontains=request.POST['text'])[(page - 1) * 30:page * 30])
                data = {'result': result, 'page': customer.objects.filter(car_number__icontains=request.POST['text']).count() // 30 + 1}
                return JsonResponse(data)
            elif request.POST['type'] == '기타':
                page = int(request.POST['page'])
                result = serialize('json', customer.objects.filter(etc__icontains=request.POST['text'])[(page - 1) * 30:page * 30])
                data = {'result': result, 'page': customer.objects.filter(etc__icontains=request.POST['text']).count() // 30 + 1}
                return JsonResponse(data)
        except Exception as e:
            print('error : ' + e)

