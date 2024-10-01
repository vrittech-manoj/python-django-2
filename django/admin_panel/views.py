from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

# Create your views here.

def index(request):
    return render(request,"admin_panel/index.html")


def product(request):
    products = Product.objects.all()
 
    context = {
        'products':products
    }
    return render(request,"admin_panel/products.html",context)

def account(request):
    return render(request,"admin_panel/accounts.html")

def admin_login(request):
    return render(request,"admin_panel/login.html")


def AddProduct(request):
    return render(request,"admin_panel/add-product.html")