from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse("Hello World!")
    #return render(request,'home.html')
    return render(request,'home.html',{'name':'Makar4nd'})

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])

    res = val1 + val2

    return render(request,'result.html',{'result':res})
