from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Fnindex (request):
    return HttpResponse("YOUR PAGE IS LOADING")
def fnnew  (request):
    return render(request,'new.html')   
    
