from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = {"name":"Suzanne"}
    return render(request,'index.html',data)

def Suzanne(request):
    return render(request,'Suzanne.html') 
