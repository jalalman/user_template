from django.shortcuts import render ,redirect
from . import models
# Create your views here.

def index(request):
    context={
        'users': models.get_all_users()
    }

    return render(request,'index.html',context)

def addUser(request):
    if request.method=='POST':
        models.create_user(request.POST)
        return redirect('/')
    else:
        return redirect('/')

    

def delete_user(request,id):

    models.del_user(id)

    return redirect('/')