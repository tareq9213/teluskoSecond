from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'home.html')

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = int(val1+val2)

    return render(request,'result.html', {'result':res})

