from django.shortcuts import render

# Create your views here.

def add(request):
    return render(request, 'add.html')

def result(request):
    num1=request.POST['num1']
    num2=request.POST['num2']
    ans=int(num1)+int(num2)
    return render(request, 'result.html', {'ans':ans})