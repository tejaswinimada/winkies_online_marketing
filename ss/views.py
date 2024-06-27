from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from distributor.models import Requirements
from .utils import *


def home(request):
    return render(request,"home.html")


   

def register(request):
    if request.method  == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        password= request.POST.get("password")
        email= request.POST.get("email")
        address = request.POST.get("address")
        phonenumber = request.POST.get("phonenumber")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        user = User.objects.create(
        username = username,
        first_name = first_name,
        email = email
        )
        user.set_password(password)
        user.save()
        profile = Stockist.objects.create(user=user,phonenumber = phonenumber,address = address)
        profile.save()
        return redirect('login')
    return render(request,"register.html")

def login_view(request):
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
            return redirect("dashboard")
        else:
            messages.error(request,"invalid username or password")
            return redirect('login_view')
    return render(request,'login.html')
@login_required
def dashboard(request):
    if request.user.is_authenticated:
        print("User is authenticated")
    else:
        print("User is not authenticated")
    orders=Orders.objects.all()
    items = Items.objects.all()
    distributors = Distributor.objects.all()
    if request.method == 'POST':
        if 'delete_item_id' in request.POST:
            item_id = request.POST.get('delete_item_id')
            try:
                item_to_delete = get_object_or_404(Items, pk=item_id)
                item_to_delete.delete()
                messages.success(request, "Item deleted successfully")
                return redirect('dashboard')
            except Items.DoesNotExist:
                messages.error(request, "Item not found")

        elif 'delete_distributor_id' in request.POST:
            distributor_id = request.POST.get('delete_distributor_id')
            try:
                distributor_to_delete = get_object_or_404(Distributor, pk=distributor_id)
                distributor_to_delete.delete()
                messages.success(request, "Distributor deleted successfully")
                return redirect('dashboard')
            except Distributor.DoesNotExist:
                messages.error(request, "Distributor not found")        

    return render(request, "dashboard.html", {'items': items,'distributors':distributors,'orders':orders})
        
@login_required
def add_item(request):
    if request.method == "POST":
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        item = Items.objects.create(item_name=item_name,quantity=quantity,price=price)
        item.save()
        
        messages.success(request,"item added succesfully")
        return redirect('dashboard')
    return render(request,'add_item.html')
@login_required
def add_distributor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        area = request.POST.get('area')
        phonenumber = request.POST.get('phonenumber')

        distributors = Distributor.objects.create(name=name,area=area,phonenumber=phonenumber)
        distributors.save()
        
        messages.success(request,"distributor has added succesfully")
        return redirect('dashboard')
    return render(request,'distributors.html')

def logout(request):
    return render(request,'logout.html')

@login_required
def add_orders(request):
    requirements = Requirements.objects.all()
    if request.method == "POST":
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        orders = Orders.objects.create(item_name=item_name, quantity=quantity, price=price)
        orders.save()

         # Fetch requirements from the distributor app
        return render(request, 'orders.html', {'requirements': requirements})

    return render(request, 'orders.html')

        # except Exception as e:
        #     messages.error(request, f"Failed to add order: {e}")
      
@login_required    
def fetch_details(request):
    requirements = Requirements.objects.all()
    return render(request,'fetch_details.html',{'requirements':requirements})
    