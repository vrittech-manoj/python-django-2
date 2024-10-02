from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin/login/')
def index(request):
    return render(request,"admin_panel/index.html")

@login_required(login_url='/admin/login/')
def product(request):
    products = Product.objects.all()
 
    context = {
        'products':products
    }
    return render(request,"admin_panel/products.html",context)

def account(request):
    return render(request,"admin_panel/accounts.html")

def admin_login(request):
    if request.method == "POST":
        #here will be login process
        print("\n\n","method_name is:", request.method,request.POST,"  ***************\n\n")
        username = request.POST['username']
        password = request.POST['password']
   
        print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            print(" user data get success ")
            return HttpResponse(f"you are going  to login with {username} and {password}")
        else:
            print("invalid password and username")
            return HttpResponse(f"invalid password and username")
        
    else:
        return render(request,"admin_panel/login.html")


def AddProduct(request):
    return render(request,"admin_panel/add-product.html")