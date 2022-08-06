from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo
# Create your views here.

def index(request):
    if request.method == "POST" :
        form = TodoForm(request.POST or None) # created instance
        if form.is_valid(): #form an object created
           form.save()
           return redirect('index')
        else:
            print('Invalid form')
    else: 
        data = Todo.objects.all #data is key where data is stored
        return render(request, 'index.html',{'data':data}) #with html rendering data also


