from django.shortcuts import render,redirect
from .models import *
from .admin import *
from .serilizer import *
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view(['DELETE','PUT','GET',"POST"])

def technologyblog(request):
    if request.method=="GET":
        data=Blog.objects.all()
        form=blog(data,many=True)
        return Response(form.data,status=status.HTTP_200_OK)
    else:
        form=blog(data=request.data)
        if form.is_valid():
            form.save()
            print('done')
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

def show(request):
    data=Blog.objects.all()
    return render(request,'home.html',{'data':data})

def readmore(request,id):
    alldata=Blog.objects.get(id=id)
    return render(request,'readmore.html',{'alldata':alldata})

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:

            messages.warning(' invalid username or password ')
            return redirect('login')
def logout(request):
    auth.logout(request)
    return redirect('login')
            
        
       
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'username already exist')
                return redirect('signup')
            elif User.objects.create_user(username=username,password=pass1):
                messages.success(request,'account created succesfully')
                return redirect('login')
        else:
            messages.warning(request,'password doesnot match')
            return redirect('signup')
    
    

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        if search:
            info=Blog.objects.filter(Blog_name__contains=search)
            return render(request,'home.html',{'info':info})
        else:
            messages.warning(request,'invalid search')
            return redirect('home')
    else:
        return redirect('home')