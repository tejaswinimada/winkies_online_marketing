from django.shortcuts import render,redirect
from .models import *
from ss import views 
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.

def index(request):
    return render(request,"index.html")
def registration(request):
    if request.method  == "POST":
        username = request.POST.get("username")
        password= request.POST.get("password")
        email= request.POST.get("email")
        print(username,password,email)
        if Admin.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("registration")
        if Admin.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("registration")
        print(username,password,email)
        hashed_password = make_password(password)
        user = Admin.objects.create(
        username = username,
        email = email,
        password = hashed_password 
        )
        user.save()
        return redirect('login1')
    return render(request,"registration.html")

def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username= username,password = password) 
        print(user)
        print(username,password)
        if user is not None:
            login(request,user)
            messages.success(request, "Login successful")
            return redirect('items_details')
        else:
            messages.error(request,"invalid username or password")
            return redirect('login1')
    return render(request,'login1.html')



@login_required
def items_details(request):
    items  = Items.objects.all()
    require=Requirements.objects.all()
    return render(request, 'distributor_detail.html', {'items':items,'require':require})
def requirements(request):
    if request.method=="POST":

        item_name=request.POST.get('item_name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        require=Requirements.objects.create(item_name=item_name,quantity=quantity,price=price)
        require.save()
        return redirect('items_details')
    return render (request,"requirements.html")
    